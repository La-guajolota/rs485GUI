"""
Author  :   Adrián Silva Palafox
Date    :   2026-03-05
Brief   :   Main application for the leather area measurement terminal. 
            Provides a graphical user interface (GUI) for real-time data display 
            and session management of Excel logs.
"""
import sys
import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import serial.tools.list_ports

from backend.serial_parser import SerialProcessor
from backend.data_manager import DataManager
from backend.bill_generartor import generate_receipt


def get_resource_path(relative_path: str) -> str:
    """
    Returns the absolute path to a required resource.
    
    Resolves the directory path for both standard Python execution and 
    PyInstaller temporary execution environments (_MEIPASS).

    Args:
        relative_path (str): The relative path to the target resource.

    Returns:
        str: The absolute path to the specified resource.
    """
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
    """
    Main application class for the Leather Measurement Terminal.
    
    Manages the initialization of the UI components, handles user input events, 
    and facilitates inter-thread communication with the background serial processor.
    
    Attributes:
        root (tk.Tk): The root Tkinter window instance.
        data_manager (DataManager): Instance handling local file operations.
        serial_processor (SerialProcessor): Instance managing RS-232 communications.
        is_running (bool): State flag indicating active serial polling.
    """
    
    def __init__(self, root: tk.Tk):
        """
        Initializes the App instance and configures the main window.
        
        Args:
            root (tk.Tk): The root graphical window object.
        """
        self.root = root
        self.root.title("Terminal de Medición de Cuero")
        self.root.geometry("850x750")
        
        self.data_manager = DataManager()
        self.serial_processor = None
        self.is_running = False
        
        self.logo_left_img = None
        self.logo_right_img = None

        self._setup_ui()
        self._poll_queue()

    def _show_about(self) -> None:
        """Displays developer and system information."""
        about_text = (
            "Máquina de Medición - Modelo 602\n"
            "Versión: 1.0\n\n"
            "Copyright © 2026 Scalini\n"
            "Todos los derechos reservados.\n\n"
            "Ingeniero de Desarrollo: Adrián Silva Palafox\n"
            "Soporte Técnico: - - -\n"
            "Web: https://scalini.mx/"
        )
        messagebox.showinfo("Acerca de", about_text)

        # Insert this routing logic into the _setup_ui method in main.py
        menubar = tk.Menu(self.root)
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Acerca de", command=self._show_about)
        menubar.add_cascade(label="Ayuda", menu=help_menu)
        self.root.config(menu=menubar)

    def _load_logo(self, path: str, size: tuple):
        """
        Loads and resizes an image file for UI integration.

        Args:
            path (str): The absolute path to the image file.
            size (tuple): A tuple containing (width, height) integers.

        Returns:
            ImageTk.PhotoImage: The processed image ready for Tkinter, 
            or None if the file is missing or corrupted.
        """
        if os.path.exists(path):
            try:
                img = Image.open(path)
                img = img.resize(size, Image.LANCZOS)
                return ImageTk.PhotoImage(img)
            except Exception as e:
                print(f"Error loading logo: {e}")
                return None
        return None

    def _get_available_ports(self) -> list:
        """
        Scans the system hardware for active serial interfaces.

        Returns:
            list: A list of strings representing available COM port device names.
        """
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    def _refresh_ports(self) -> None:
        """
        Refreshes the COM port selection dropdown menu in the UI with current system data.
        """
        current_ports = self._get_available_ports()
        self.port_combo['values'] = current_ports
        if current_ports:
            self.port_combo.current(0)
        else:
            self.port_combo.set("No ports found")

    def _select_directory(self) -> None:
        """
        Triggers a system directory selection dialog to define the output folder.
        """
        selected_dir = filedialog.askdirectory(initialdir=self.dir_var.get(), title="Seleccionar Directorio")
        if selected_dir:
            self.dir_var.set(selected_dir)

    def _select_logo_file(self) -> None:
        """
        Triggers a system file selection dialog restricted to standard image formats.
        """
        filetypes = (
            ("Image files", "*.jpg *.jpeg *.png"),
            ("All files", "*.*")
        )
        selected_file = filedialog.askopenfilename(
            title="Seleccionar Logo del Cliente",
            initialdir=os.getcwd(),
            filetypes=filetypes
        )
        if selected_file:
            self.logo_var.set(selected_file)

    def _setup_ui(self) -> None:
        """
        Constructs and aligns all internal graphical user interface widgets.
        """
        # Header Frame
        header_frame = ttk.Frame(self.root)
        header_frame.pack(fill="x", padx=10, pady=10)

        self._show_about()
        
        self.logo_left_img = self._load_logo(LOGO_LEFT, size=SCALINI_LOGO_SIZE)
        if self.logo_left_img:
            left_logo_label = ttk.Label(header_frame, image=self.logo_left_img)
        else:
            left_logo_label = ttk.Label(header_frame, text="[Logo Empresa]", relief="sunken", width=15, anchor="center")
        left_logo_label.pack(side="left", padx=10)
        
        title_label = ttk.Label(header_frame, text="MÁQUINA DE MEDICIÓN DE ÁREA DE PIEL\nMODELO 602", font=("Helvetica", 18, "bold"), anchor="center")
        title_label.pack(side="left", expand=True)
        
        self.logo_right_img = self._load_logo(LOGO_RIGHT, size=CLIENT_LOGO_SIZE)
        if self.logo_right_img:
            right_logo_label = ttk.Label(header_frame, image=self.logo_right_img)
        else:
            right_logo_label = ttk.Label(header_frame, text="[Logo Cliente]", relief="sunken", width=15, anchor="center")
        right_logo_label.pack(side="right", padx=10)

        # Bill Generation Controls Frame
        bill_control_frame = ttk.LabelFrame(self.root, text="Control de generación de recibos")
        bill_control_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(bill_control_frame, text="Directorio de salida:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        default_dir = os.path.abspath(os.path.join(os.getcwd(), "sesion"))
        self.dir_var = tk.StringVar(value=default_dir)
        self.dir_entry = ttk.Entry(bill_control_frame, textvariable=self.dir_var, state="readonly", width=50)
        self.dir_entry.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        self.dir_btn = ttk.Button(bill_control_frame, text="Examinar...", command=self._select_directory)
        self.dir_btn.grid(row=0, column=2, padx=5, pady=5)

        ttk.Label(bill_control_frame, text="Logo del cliente:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.logo_var = tk.StringVar()
        self.logo_entry = ttk.Entry(bill_control_frame, textvariable=self.logo_var, state="readonly", width=50)
        self.logo_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        self.logo_btn = ttk.Button(bill_control_frame, text="Buscar Imagen...", command=self._select_logo_file)
        self.logo_btn.grid(row=1, column=2, padx=5, pady=5)

        ttk.Label(bill_control_frame, text="Nombre del cliente:").grid(row=0, column=3, sticky="e", padx=5, pady=5)
        self.client_entry = ttk.Entry(bill_control_frame, width=50)
        self.client_entry.grid(row=0, column=4, sticky="w", padx=5, pady=5)

        ttk.Label(bill_control_frame, text="Dirección del cliente:").grid(row=1, column=3, sticky="e", padx=5, pady=5)
        self.address_entry = ttk.Entry(bill_control_frame, width=50)
        self.address_entry.grid(row=1, column=4, sticky="w", padx=5, pady=5)

        # Management Controls Frame
        management_controls_frame = ttk.LabelFrame(self.root, text="Controles de gestión")
        management_controls_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(management_controls_frame, text="Puerto COM:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.port_combo = ttk.Combobox(management_controls_frame, state="readonly", width=15)
        self.port_combo.grid(row=0, column=1, sticky="w", padx=5, pady=5)
        self._refresh_ports()

        self.refresh_btn = ttk.Button(management_controls_frame, text="↻ Actualizar", command=self._refresh_ports)
        self.refresh_btn.grid(row=0, column=2, padx=5, pady=5)

        self.start_btn = ttk.Button(management_controls_frame, text="Iniciar Sesión", command=self.start_session)
        self.start_btn.grid(row=0, column=3, padx=15, pady=5)

        self.stop_btn = ttk.Button(management_controls_frame, text="Detener Sesión", command=self.stop_session, state="disabled")
        self.stop_btn.grid(row=0, column=4, padx=5, pady=5)

        # Data Frame
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

        # Status Bar
        self.status_var = tk.StringVar(value="Estado: Esperando conexión...")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief="sunken", anchor="w")
        status_bar.pack(fill="x", side="bottom", padx=10, pady=5)

    def start_session(self) -> None:
        """
        Validates input parameters, initializes data storage structures, and starts 
        the background serial polling thread. Disables form inputs during runtime.
        """
        client = self.client_entry.get().strip()
        client_address = self.address_entry.get().strip()
        port = self.port_combo.get().strip()
        output_dir = self.dir_var.get().strip()

        if not client or not client_address or not port or port == "No ports found":
            messagebox.showerror("Error", "El nombre del cliente, la dirección del cliente y un puerto COM válido son obligatorios.")
            return

        self.data_manager.create_session(client, client_address, output_dir)
        self.serial_processor = SerialProcessor(port=port)
        
        if self.serial_processor.start_reading():
            self.is_running = True
            self.start_btn.config(state="disabled")
            self.stop_btn.config(state="normal")
            self.client_entry.config(state="disabled")
            self.address_entry.config(state="disabled")
            self.logo_btn.config(state="disabled")
            self.port_combo.config(state="disabled")
            self.dir_btn.config(state="disabled")
            self.refresh_btn.config(state="disabled")
            self.status_var.set(f"Estado: Conectado a {port} - Sesión activa para {client}")
        else:
            messagebox.showerror("Error", f"No se pudo abrir el puerto {port}.")

    def stop_session(self) -> None:
        """
        Terminates active serial communications, extracts the finalized session data, 
        and invokes the PDF receipt generator. Restores interface control states.
        """
        if self.serial_processor:
            self.serial_processor.stop_reading()
        self.is_running = False
        
        client_name = self.client_entry.get().strip()
        client_address = self.address_entry.get().strip()
        logo_path = self.logo_var.get().strip()
        output_excel_path = self.data_manager.current_session_file
        
        session_df = self.data_manager.get_current_dataframe()

        if not session_df.empty:
            pdf_success = generate_receipt(session_df, client_name, client_address, logo_path, output_excel_path)
            if pdf_success:
                messagebox.showinfo("Éxito", "El recibo PDF fue generado correctamente.")
            else:
                messagebox.showwarning("Advertencia", "Ocurrió un error procesando los datos para el recibo PDF.")
        else:
            messagebox.showwarning("Información", "No se detectaron piezas medidas durante esta sesión. No se generó recibo.")

        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.client_entry.config(state="normal")
        self.address_entry.config(state="normal")
        self.logo_btn.config(state="normal")
        self.port_combo.config(state="readonly")
        self.dir_btn.config(state="normal")
        self.refresh_btn.config(state="normal")
        self.status_var.set("Estado: Sesión detenida")

    def _poll_queue(self) -> None:
        """
        Asynchronous loop method called via the Tkinter event loop.
        Extracts pending items from the serial processor's queue and updates 
        the Treeview and underlying dataset. Runs continuously every 100 milliseconds.
        """
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