import serial
import re
import threading
import queue

class SerialProcessor:
    def __init__(self, port: str, baudrate: int = 4800):
        self.port = port
        self.baudrate = baudrate
        self.serial_conn = None
        self.data_queue = queue.Queue()
        self.stop_event = threading.Event()
        
        self.current_lote = "Desconocido"

    def start_reading(self) -> bool:
        try:
            self.serial_conn = serial.Serial(self.port, self.baudrate, timeout=1)
            self.stop_event.clear()
            thread = threading.Thread(target=self._read_loop, daemon=True)
            thread.start()
            return True
        except serial.SerialException:
            return False

    def stop_reading(self) -> None:
        self.stop_event.set()
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()

    def _read_loop(self) -> None:
        while not self.stop_event.is_set():
            if self.serial_conn.in_waiting:
                raw_bytes = self.serial_conn.readline()
                try:
                    line = raw_bytes.decode('cp858', errors='ignore')
                    clean_line = re.sub(r'[^\x20-\x7E]', '', line).replace('@', '').strip()
                    self._parse_line(clean_line)
                except Exception:
                    pass

    def _parse_line(self, line: str) -> None:
        if not line:
            return

        lote_match = re.search(r'LOTE\s*#\s*(\d+)', line)
        if lote_match:
            self.current_lote = int(lote_match.group(1))
            return

        pieza_match = re.search(r'^(\d+)\s+(\d+(?:\.\d+)?)$', line)
        if pieza_match:
            pieza = int(pieza_match.group(1))
            area = float(pieza_match.group(2))
            
            self.data_queue.put({
                "lote": self.current_lote,
                "pieza": pieza,
                "area": area
            })