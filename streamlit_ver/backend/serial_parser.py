import serial
import re
import threading
import queue

class SerialProcessor:
    def __init__(self, port, baudrate=4800):
        self.port = port
        self.baudrate = baudrate
        self.serial_conn = None
        self.data_queue = queue.Queue()
        self.stop_event = threading.Event()
        
        # State variables for the current operational block
        self.current_lote = None
        self.current_total = None

    def start_reading(self):
        try:
            self.serial_conn = serial.Serial(self.port, self.baudrate, timeout=1)
            self.stop_event.clear()
            thread = threading.Thread(target=self._read_loop, daemon=True)
            thread.start()
            return True
        except serial.SerialException:
            return False

    def stop_reading(self):
        self.stop_event.set()
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()

    def _read_loop(self):
        while not self.stop_event.is_set():
            if self.serial_conn.in_waiting:
                raw_bytes = self.serial_conn.readline()
                try:
                    # Decode replacing invalid chars, then strip ESC codes
                    line = raw_bytes.decode('cp858', errors='replace')
                    clean_line = re.sub(r'[^\x20-\x7E]', '', line).strip()
                    self._parse_line(clean_line)
                except Exception:
                    pass

    def _parse_line(self, line):
        # Match LOTE identifier 
        lote_match = re.search(r'LOTE\s*#\s*(\d+)', line)
        if lote_match:
            self.current_lote = int(lote_match.group(1))
            return

        # Match TOTAL identifier 
        total_match = re.search(r'TOTAL\s*=\s*(\d+(?:\.\d+)?)\s*Dm', line, re.IGNORECASE)
        if total_match:
            self.current_total = float(total_match.group(1))
            return

        # Match Pieza and Area [cite: 1, 2]
        pieza_match = re.search(r'^(\d+)\s+(\d+(?:\.\d+)?)$', line)
        if pieza_match and self.current_lote is not None:
            pieza = int(pieza_match.group(1))
            area = float(pieza_match.group(2))
            
            self.data_queue.put({
                "lote": self.current_lote,
                "pieza": pieza,
                "area": area,
                "total_area": self.current_total # May be None until the end of the batch
            })