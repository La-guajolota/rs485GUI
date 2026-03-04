import serial 

ser = serial.Serial(
    port='COM3',                   # Device path
    baudrate=4800,                 # Communication speed
    bytesize=serial.EIGHTBITS,     # Data bits (5, 6, 7, 8)
    parity=serial.PARITY_NONE,     # Parity checking
    stopbits=serial.STOPBITS_ONE,  # Stop bits (1, 1.5, 2)
    timeout=1,                     # Read timeout in seconds
    xonxoff=False,                 # Software flow control
    rtscts=False,                  # Hardware (RTS/CTS) flow control
    write_timeout=None,            # Write timeout in seconds
    dsrdtr=False,                  # DSR/DTR flow control
    inter_byte_timeout=None,       # Inter-byte timeout
    exclusive=None                 # Exclusive access (Linux)
)

def read_lines_forever(ser):
    """Read lines continuously with error handling"""
    while True:
        try:
            line = ser.read_until(b'\x1b@') # ESC + '!' as the end of line marker
            if line:
                text = line.decode('utf-8', errors='ignore')
                if text:  # Skip empty lines
                    yield text
        except KeyboardInterrupt:
            print("Keyboard interrupt received.")
            break
        except Exception as e:
            print(f"Read error: {e}")
            break

# Usage

for line in read_lines_forever(ser):
    print(f"Got: {line}")