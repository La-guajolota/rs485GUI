import serial.tools.list_ports

# List all available serial ports and print their descriptions
ports = serial.tools.list_ports.comports()
if not ports:
	print("No serial ports found.")
else:
	for port in ports:
		print(f"Port: {port.device}, Description: {port.description}")