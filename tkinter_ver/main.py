import sys
import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import serial.tools.list_ports
from backend.serial_parser import SerialProcessor
from backend.data_manager import DataManager

def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    return os.path.join(base_path, relative_path)

LOGO_DIR = get_resource_path(os.path.join("docs", "companiesLogos"))
LOGO_LEFT = os.path.join(LOGO_DIR, "scaliniLogo.jpg")
LOGO_RIGHT = os.path.join(LOGO_DIR, "clienteLogo.jpg")
CLIENT_LOGO_SIZE = (250, 150)
SCALINI_LOGO_SIZE = (400, 125)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Terminal de Medición de Cuero")
        self.root.geometry("850x650")
        
        self.data_manager = DataManager()
        self.serial_processor = None
        self.is_running = False
        
        self.logo_left_img = None
        self.logo_right_img = None

        self._setup_ui()
        self._poll_queue()

    def _load_logo(self, path, size):
        if os.path.exists(path):
            try:
                img = Image.open(path)
                img = img.resize(size, Image.LANCZOS)
                return ImageTk.PhotoImage(img)
            except Exception:
                return None
        return None

    def _get_available_ports(self):
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    def _refresh_ports(self):
        current_ports = self._get_available_ports()
        self.port_combo['values'] = current_ports
        if current_ports:
            self.port_combo.current(0)
        else:
            self.port_combo.set("No ports found")

    def _select_directory(self):
        selected_dir = filedialog.askdirectory(initialdir=self.dir_var.get(), title="Seleccionar Directorio")
        if selected_dir:
            self.dir_var.set(selected_dir)

    def _setup_ui(self):
        header_frame = ttk.Frame(self.root)
        header_frame.pack(fill="x", padx=10, pady=10)
        
        self.logo_left_img = self._load_logo(LOGO_LEFT, size=SCALINI_LOGO_SIZE)
        if self.logo_left_img:
            left_logo_label = ttk.Label(header_frame, image=self.logo_left_img)
        else:
            left_logo_label = ttk.Label(header_frame, text="[Logo Empresa]", relief="sunken", width=15, anchor="center")
        left_logo_label.pack(side="left", padx=10)
        
        title_label = ttk.Label(header_frame, text= "MÁQUINA DE MEDICIÓN DE ÁREA DE PIEL\nMODELO 602", font=("Helvetica", 18, "bold"), anchor="center")
        title_label.pack(side="left", expand=True)
        
        self.logo_right_img = self._load_logo(LOGO_RIGHT, size=CLIENT_LOGO_SIZE)
        if self.logo_right_img:
            right_logo_label = ttk.Label(header_frame, image=self.logo_right_img)
        else:
            right_logo_label = ttk.Label(header_frame, text="[Logo Cliente]", relief="sunken", width=15, anchor="center")
        right_logo_label.pack(side="right", padx=10)

        control_frame = ttk.LabelFrame(self.root, text="Control de Sesión")
        control_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(control_frame, text="Directorio de salida:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        
        default_dir = os.path.abspath(os.path.join(os.getcwd(), "sessions"))
        self.dir_var = tk.StringVar(value=default_dir)
        
        self.dir_entry = ttk.Entry(control_frame, textvariable=self.dir_var, state="readonly", width=40)
        self.dir_entry.grid(row=0, column=1, columnspan=2, sticky="w", padx=5, pady=5)
        
        self.dir_btn = ttk.Button(control_frame, text="Examinar...", command=self._select_directory)
        self.dir_btn.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(control_frame, text="Nombre del cliente:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.client_entry = ttk.Entry(control_frame, width=20)
        self.client_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(control_frame, text="Puerto COM:").grid(row=1, column=2, sticky="e", padx=5, pady=5)
        
        self.port_combo = ttk.Combobox(control_frame, state="readonly", width=15)
        self.port_combo.grid(row=1, column=3, sticky="w", padx=5, pady=5)
        self._refresh_ports()

        self.refresh_btn = ttk.Button(control_frame, text="↻ Actualizar", command=self._refresh_ports)
        self.refresh_btn.grid(row=1, column=4, padx=5, pady=5)

        self.start_btn = ttk.Button(control_frame, text="Iniciar Sesión", command=self.start_session)
        self.start_btn.grid(row=1, column=5, padx=5, pady=5)

        self.stop_btn = ttk.Button(control_frame, text="Detener Sesión", command=self.stop_session, state="disabled")
        self.stop_btn.grid(row=1, column=6, padx=5, pady=5)

        data_frame = ttk.LabelFrame(self.root, text="Datos de Medición en Tiempo Real")
        data_frame.pack(fill="both", expand=True, padx=10, pady=10)

        columns = ("lote", "pieza", "area")
        self.tree = ttk.Treeview(data_frame, columns=columns, show="headings")
        self.tree.heading("lote", text="Lote")
        self.tree.heading("pieza", text="Pieza")
        self.tree.heading("area", text="Área (Dm²)")
        
        scrollbar = ttk.Scrollbar(data_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True, padx=5, pady=5)

        self.status_var = tk.StringVar(value="Estado: Esperando conexión...")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief="sunken", anchor="w")
        status_bar.pack(fill="x", side="bottom", padx=10, pady=5)

    def start_session(self):
        client = self.client_entry.get().strip()
        port = self.port_combo.get().strip()
        output_dir = self.dir_var.get().strip()

        if not client or not port or port == "No ports found":
            messagebox.showerror("Error", "El nombre del cliente y un puerto COM válido son obligatorios.")
            return

        self.data_manager.create_session(client, output_dir)
        self.serial_processor = SerialProcessor(port=port)
        
        if self.serial_processor.start_reading():
            self.is_running = True
            self.start_btn.config(state="disabled")
            self.stop_btn.config(state="normal")
            self.client_entry.config(state="disabled")
            self.port_combo.config(state="disabled")
            self.dir_btn.config(state="disabled")
            self.refresh_btn.config(state="disabled")
            self.status_var.set(f"Estado: Conectado a {port} - Sesión activa para {client}")
        else:
            messagebox.showerror("Error", f"No se pudo abrir el puerto {port}.")

    def stop_session(self):
        if self.serial_processor:
            self.serial_processor.stop_reading()
        self.is_running = False
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.client_entry.config(state="normal")
        self.port_combo.config(state="readonly")
        self.dir_btn.config(state="normal")
        self.refresh_btn.config(state="normal")
        self.status_var.set("Estado: Sesión detenida")

    def _poll_queue(self):
        if self.is_running and self.serial_processor:
            while not self.serial_processor.data_queue.empty():
                data = self.serial_processor.data_queue.get()
                
                self.tree.insert("", "end", values=(data["lote"], data["pieza"], data["area"]))
                self.tree.yview_moveto(1)
                
                self.data_manager.append_data(data["lote"], data["pieza"], data["area"])

        self.root.after(100, self._poll_queue)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()