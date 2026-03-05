"""
Author  :   Adrián Silva Palafox
Date    :   2026-03-05
Brief   :   Data parser and asynchronous hardware communicator. 
            Executes background polling for RS-232 connected devices and cleans ESC/POS artifacts.
"""
import serial
import re
import threading
import queue

class SerialProcessor:
    """
    Manages the hardware connection to the measurement machine via PySerial.
    
    Reads incoming byte buffers asynchronously, applies Regular Expression patterns 
    to filter non-printable characters, and injects validated data dictionaries 
    into a thread-safe Queue object for external consumption.
    
    Attributes:
        port (str): Hardware string path representing the COM port.
        baudrate (int): Frequency baud rate for serial communication. Defaults to 4800.
        serial_conn (serial.Serial): Active PySerial connection object.
        data_queue (queue.Queue): Thread-safe FIFO stack storing sanitized measurements.
        stop_event (threading.Event): Thread execution control flag.
        current_lote (int or str): Memory state tracking the active batch classification.
    """
    
    def __init__(self, port: str, baudrate: int = 4800):
        """
        Initializes parameter limits and structural components for the processor.
        
        Args:
            port (str): Path of COM serial device.
            baudrate (int, optional): Port speed limit configuration. Defaults to 4800.
        """
        self.port = port
        self.baudrate = baudrate
        self.serial_conn = None
        self.data_queue = queue.Queue()
        self.stop_event = threading.Event()
        
        self.current_lote = "Desconocido"

    def start_reading(self) -> bool:
        """
        Attempts to open the serial port and dispatch a daemon thread for execution.
        
        Returns:
            bool: True if connection establishment and thread assignment are successful. 
                  False if encountering OS SerialException issues.
        """
        try:
            self.serial_conn = serial.Serial(self.port, self.baudrate, timeout=1)
            self.stop_event.clear()
            thread = threading.Thread(target=self._read_loop, daemon=True)
            thread.start()
            return True
        except serial.SerialException:
            return False

    def stop_reading(self) -> None:
        """
        Signals the termination event to the thread and subsequently closes the serial hardware pipeline.
        """
        self.stop_event.set()
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()

    def _read_loop(self) -> None:
        """
        Continuous while-loop restricted to the execution context of the daemon thread.
        Monitors hardware IO cache buffers.
        """
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
        """
        Applies Regex structural mapping against sanitized strings and populates the data queue.
        
        Args:
            line (str): Raw sanitized ASCII string outputted from the hardware.
        """
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