import argparse
import sys
import serial
from serial.tools import list_ports


def parse_args() -> argparse.Namespace:
	parser = argparse.ArgumentParser(
		description="Lector serial de solo lectura (no transmite datos)."
	)
	parser.add_argument("--port", required=True, help="Puerto serial, por ejemplo COM3")
	parser.add_argument("--baudrate", type=int, default=9600, help="Velocidad en baudios")
	parser.add_argument("--timeout", type=float, default=1.0, help="Timeout de lectura en segundos")
	parser.add_argument(
		"--raw",
		action="store_true",
		help="Muestra bytes en hexadecimal en lugar de texto",
	)
	return parser.parse_args()


def show_ports() -> None:
	ports = list(list_ports.comports())
	if not ports:
		print("No se detectaron puertos seriales.")
		return

	print("Puertos disponibles:")
	for p in ports:
		print(f"- {p.device} | {p.description}")


def main() -> int:
	args = parse_args()

	try:
		with serial.Serial(args.port, args.baudrate, timeout=args.timeout) as ser:
			print(f"Conectado a {ser.port} @ {ser.baudrate} baudios")
			print("Modo: SOLO LECTURA. Presiona Ctrl+C para salir.\n")

			while True:
				data = ser.readline()
				if not data:
					continue

				if args.raw:
					print(data.hex(" "))
				else:
					print(data.decode("utf-8", errors="replace").rstrip("\r\n"))

	except serial.SerialException as error:
		print(f"Error abriendo/leyendo el puerto: {error}")
		show_ports()
		return 1
	except KeyboardInterrupt:
		print("\nLectura detenida por el usuario.")
		return 0


if __name__ == "__main__":
	sys.exit(main())
