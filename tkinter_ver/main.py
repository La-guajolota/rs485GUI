"""
Author  :   Adrián Silva Palafox
Date    :   2026-3-4
Brief   :   Main application for the leather measurement terminal. Provides a GUI
            for real-time data display and session management. 
"""
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from backend.serial_parser import SerialProcessor
from backend.data_manager import DataManager

# Path to logo images
LOGO_DIR = os.path.join(os.path.dirname(__file__), "..", "docs", "companiesLogos")
LOGO_LEFT = os.path.join(LOGO_DIR, "scaliniLogo.jpg")
LOGO_RIGHT = os.path.join(LOGO_DIR, "clienteLogo.jpg")
CLIENT_LOGO_SIZE = (250, 150)   # Width x Height for logo display
SCALINI_LOGO_SIZE = (400, 125)  # Size for Scalini logo


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Terminal de Medición de Cuero")
        self.root.geometry("850x650")
        
        self.data_manager = DataManager() # Data manager instance for handling Excel files
        self.serial_processor = None
        self.is_running = False
        
        # Keep references to images to prevent garbage collection
        self.logo_left_img = None
        self.logo_right_img = None

        self._setup_ui()
        self._poll_queue()

    def _load_logo(self, path, size):
        """Load and resize a logo image. Returns None if file not found."""
        if os.path.exists(path):
            try:
                img = Image.open(path)
                img = img.resize(size, Image.LANCZOS)
                return ImageTk.PhotoImage(img)
            except Exception:
                return None
        return None

    def _setup_ui(self):
        # === Header frame with logos ===
        header_frame = ttk.Frame(self.root)
        header_frame.pack(fill="x", padx=10, pady=10)
        
        # Left logo
        self.logo_left_img = self._load_logo(LOGO_LEFT, size=SCALINI_LOGO_SIZE)
        if self.logo_left_img:
            left_logo_label = ttk.Label(header_frame, image=self.logo_left_img)
        else:
            left_logo_label = ttk.Label(header_frame, text="[Logo Empresa]", 
                                        relief="sunken", width=15, anchor="center")
        left_logo_label.pack(side="left", padx=10)
        
        # Title in the center
        title_label = ttk.Label(header_frame, text="Máquina de medir área de piel modelo 602", 
                                font=("Helvetica", 20, "bold"))
        title_label.pack(side="left", expand=True)
        
        # Right logo
        self.logo_right_img = self._load_logo(LOGO_RIGHT, size=CLIENT_LOGO_SIZE)
        if self.logo_right_img:
            right_logo_label = ttk.Label(header_frame, image=self.logo_right_img)
        else:
            right_logo_label = ttk.Label(header_frame, text="[Logo Cliente]", 
                                         relief="sunken", width=15, anchor="center")
        right_logo_label.pack(side="right", padx=10)

        # === Control frame ===
        control_frame = ttk.LabelFrame(self.root, text="Control de Sesión")
        control_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(control_frame, text="Nombre del archivo de sesión:").grid(row=0, column=0, padx=5, pady=5)
        self.client_entry = ttk.Entry(control_frame)
        self.client_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(control_frame, text="Puerto COM:").grid(row=0, column=2, padx=5, pady=5)
        self.port_entry = ttk.Entry(control_frame)
        self.port_entry.insert(0, "COM3")
        self.port_entry.grid(row=0, column=3, padx=5, pady=5)

        self.start_btn = ttk.Button(control_frame, text="Iniciar Sesión", command=self.start_session)
        self.start_btn.grid(row=0, column=4, padx=5, pady=5)

        self.stop_btn = ttk.Button(control_frame, text="Detener Sesión", command=self.stop_session, state="disabled")
        self.stop_btn.grid(row=0, column=5, padx=5, pady=5)

        # === Data frame ===
        data_frame = ttk.LabelFrame(self.root, text="Datos de Medición en Tiempo Real")
        data_frame.pack(fill="both", expand=True, padx=10, pady=10)

        columns = ("lote", "pieza", "area", "total_area")
        self.tree = ttk.Treeview(data_frame, columns=columns, show="headings")
        self.tree.heading("lote", text="Lote")
        self.tree.heading("pieza", text="Pieza")
        self.tree.heading("area", text="Área (Dm²)")
        self.tree.heading("total_area", text="Área Total (Dm²)")
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(data_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.tree.pack(fill="both", expand=True, padx=5, pady=5)

        # === Status bar ===
        self.status_var = tk.StringVar(value="Estado: Esperando conexión...")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief="sunken", anchor="w")
        status_bar.pack(fill="x", side="bottom", padx=10, pady=5)

    def start_session(self):
        client = self.client_entry.get().strip()
        port = self.port_entry.get().strip()

        if not client or not port:
            messagebox.showerror("Error", "El nombre del cliente y el puerto COM son obligatorios.")
            return

        self.data_manager.create_session(client)
        self.serial_processor = SerialProcessor(port=port) # Initialize serial processor instance with specified port
        
        if self.serial_processor.start_reading():
            self.is_running = True
            self.start_btn.config(state="disabled")
            self.stop_btn.config(state="normal")
            self.client_entry.config(state="disabled")
            self.port_entry.config(state="disabled")
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
        self.port_entry.config(state="normal")
        self.status_var.set("Estado: Sesión detenida")

    def _poll_queue(self):
        if self.is_running and self.serial_processor:
            while not self.serial_processor.data_queue.empty():
                data = self.serial_processor.data_queue.get()
                
                # Update UI
                self.tree.insert("", "end", values=(data["lote"], data["pieza"], data["area"], data["total_area"]))
                self.tree.yview_moveto(1)
                
                # Save to Excel
                self.data_manager.append_data(data["lote"], data["pieza"], data["area"], data["total_area"])

        self.root.after(100, self._poll_queue)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()