"""
Serial Parser Module for RS485 Leather Measurement Systems.

This module provides functionality to read and parse data from RS485-connected
measurement devices (e.g., area measurement machines used in leather processing).
It handles asynchronous serial communication and extracts structured data from
the device's output stream.

Typical data format expected from device:
    LOTE # 123          -> Batch identifier
    1    45.50          -> Piece number and area (in Dm²)
    2    38.20
    ...
    TOTAL = 83.70 Dm    -> Batch total area
"""

import serial
import re
import threading
import queue


class SerialProcessor:
    """
    Asynchronous serial port reader and parser for measurement data.
    
    Reads data from an RS485 serial connection in a background thread,
    parses measurement records (lote/pieza/area), and queues them for
    consumption by the UI layer.
    
    Attributes:
        port (str): Serial port path (e.g., '/dev/ttyUSB0', 'COM3').
        baudrate (int): Communication speed in baud.
        data_queue (Queue): Thread-safe queue containing parsed records.
        
    Example:
        processor = SerialProcessor('/dev/ttyUSB0', baudrate=9600)
        if processor.start_reading():
            while True:
                record = processor.data_queue.get()
                print(f"Lote {record['lote']}, Pieza {record['pieza']}: {record['area']} Dm²")
    """
    
    def __init__(self, port: str, baudrate: int = 4800):
        """
        Initialize the serial processor.
        
        Args:
            port: Serial port identifier (e.g., '/dev/ttyUSB0' on Linux, 'COM3' on Windows).
            baudrate: Baud rate for serial communication. Default 9600 matches
                      most industrial measurement devices.
        """
        self.port = port
        self.baudrate = baudrate
        self.serial_conn = None
        self.data_queue = queue.Queue()
        self.stop_event = threading.Event()
        
        # State tracking for multi-line record parsing
        self.current_lote = None   # Active batch number
        self.current_total = None  # Running total for current batch

    def start_reading(self) -> bool:
        """
        Open the serial connection and start the background reader thread.
        
        Returns:
            True if connection established successfully, False on error
            (e.g., port busy, device not found, permission denied).
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
        Signal the reader thread to stop and close the serial connection.
        
        Safe to call multiple times. The background thread will terminate
        gracefully on its next iteration.
        """
        self.stop_event.set()
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()

    def _read_loop(self) -> None:
        """
        Background thread: continuously read and parse incoming serial data.
        
        Runs until stop_event is set. Decodes bytes using CP858 (DOS Latin-1),
        which is common in industrial/POS devices. Strips ESC/POS control
        sequences and non-printable characters before parsing.
        """
        while not self.stop_event.is_set():
            if self.serial_conn.in_waiting:
                raw_bytes = self.serial_conn.readline()
                try:
                    # CP858: DOS code page used by many thermal/industrial printers
                    line = raw_bytes.decode('cp858', errors='ignore')
                    # Remove non-printable chars and ESC/POS artifacts (e.g., '@' from ESC @)
                    clean_line = re.sub(r'[^\x20-\x7E]', '', line).replace('@', '').strip()
                    self._parse_line(clean_line)
                
                    # Debug: show cleaned line
                    print(f"Received line: {clean_line}")  
                except Exception:
                    # Silently ignore malformed data to maintain continuous operation
                    # pass
                    # For debugging purposes, we can print the raw bytes that failed to decode/parse
                    print(f"Error decoding/parsing line: {raw_bytes}")

    def _parse_line(self, line: str) -> None:
        """
        Parse a single line and extract measurement data.
        
        Handles three types of records:
        1. Batch header: "LOTE # 123" -> Sets current_lote
        2. Measurement: "1    45.50" -> Queues record with pieza/area
        3. Batch total: "TOTAL = 83.70 Dm" -> Sets current_total
        
        Args:
            line: Cleaned ASCII string from serial input.
        """
        if not line:
            return

        # Pattern: "LOTE # 123" or "LOTE #123"
        lote_match = re.search(r'LOTE\s*#\s*(\d+)', line)
        if lote_match:
            self.current_lote = int(lote_match.group(1))
            return

        # Pattern: "TOTAL = 123.45 Dm" (case-insensitive)
        total_match = re.search(r'TOTAL\s*=\s*(\d+(?:\.\d+)?)\s*Dm', line, re.IGNORECASE)
        if total_match:
            self.current_total = float(total_match.group(1))
            return

        # Pattern: "1    45.50" (piece number followed by area measurement)
        # Only valid when we have an active batch context
        pieza_match = re.search(r'^(\d+)\s+(\d+(?:\.\d+)?)$', line)
        if pieza_match and self.current_lote is not None:
            pieza = int(pieza_match.group(1))
            area = float(pieza_match.group(2))
            
            # Queue structured record for UI consumption
            self.data_queue.put({
                "lote": self.current_lote,
                "pieza": pieza,
                "area": area,
                "total_area": self.current_total
            })