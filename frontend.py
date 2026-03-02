import tkinter as tk
from tkinter import font as tkfont
from PIL import Image, ImageTk  # pip install Pillow

# ─────────────────────────────────────────────
# Configuration – change these to match assets
# ─────────────────────────────────────────────
CLIENT_NAME      = "CLIENT COMPANY"
CLIENT_LOGO_PATH = "client_logo.png"   # path to client logo file

SCALINI_NAME      = "SCALINI"
SCALINI_LOGO_PATH = "scalini_logo.png" # path to Scalini logo file

BG_COLOR       = "#1e1e2e"
PANEL_COLOR    = "#2a2a3d"
ACCENT_COLOR   = "#4fc3f7"
TEXT_COLOR     = "#e0e0e0"
DIM_TEXT_COLOR = "#888"
DISPLAY_BG     = "#0d0d1a"
DISPLAY_FG     = "#00e5ff"
COUNTER_BG     = "#252538"
COUNTER_ACCENT = "#7c4dff"


def load_logo(path: str, size: tuple[int, int]) -> ImageTk.PhotoImage | None:
    """Load an image file and return a PhotoImage, or None if unavailable."""
    try:
        img = Image.open(path).convert("RGBA").resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception:
        return None


class MeasurementApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("RS485 Measurement GUI")
        self.configure(bg=BG_COLOR)
        self.resizable(True, True)
        self.minsize(800, 500)

        # ── State ──────────────────────────────
        self.unit_var   = tk.StringVar(value="dm²")
        self.measure_val = tk.DoubleVar(value=0.0)
        self.lote_val    = tk.IntVar(value=0)
        self.pz_val      = tk.IntVar(value=0)

        # ── Fonts ──────────────────────────────
        self._f_header  = tkfont.Font(family="Segoe UI", size=15, weight="bold")
        self._f_company = tkfont.Font(family="Segoe UI", size=11)
        self._f_display = tkfont.Font(family="Consolas",  size=52, weight="bold")
        self._f_unit    = tkfont.Font(family="Segoe UI",  size=18)
        self._f_label   = tkfont.Font(family="Segoe UI",  size=10, weight="bold")
        self._f_counter = tkfont.Font(family="Consolas",  size=32, weight="bold")

        self._build_header()
        self._build_body()
        self._build_footer()

    # ── Header ─────────────────────────────────────────────────────────────
    def _build_header(self):
        hdr = tk.Frame(self, bg=PANEL_COLOR, pady=8)
        hdr.pack(fill="x", side="top")

        # ── Client (left) ──────────────────────
        client_frame = tk.Frame(hdr, bg=PANEL_COLOR)
        client_frame.pack(side="left", padx=16)

        self._client_logo_img = load_logo(CLIENT_LOGO_PATH, (64, 64))
        if self._client_logo_img:
            tk.Label(client_frame, image=self._client_logo_img,
                     bg=PANEL_COLOR).pack(side="left", padx=(0, 8))

        tk.Label(client_frame, text=CLIENT_NAME,
                 font=self._f_header, fg=TEXT_COLOR, bg=PANEL_COLOR).pack(side="left")

        # ── Divider in center ──────────────────
        tk.Frame(hdr, bg=ACCENT_COLOR, width=2).pack(
            side="left", fill="y", expand=True, padx=4)

        # ── Scalini (right) ────────────────────
        scalini_frame = tk.Frame(hdr, bg=PANEL_COLOR)
        scalini_frame.pack(side="right", padx=16)

        self._scalini_logo_img = load_logo(SCALINI_LOGO_PATH, (64, 64))
        if self._scalini_logo_img:
            tk.Label(scalini_frame, image=self._scalini_logo_img,
                     bg=PANEL_COLOR).pack(side="right", padx=(8, 0))

        tk.Label(scalini_frame, text=SCALINI_NAME,
                 font=self._f_header, fg=ACCENT_COLOR, bg=PANEL_COLOR).pack(side="right")

    # ── Body ───────────────────────────────────────────────────────────────
    def _build_body(self):
        body = tk.Frame(self, bg=BG_COLOR)
        body.pack(fill="both", expand=True, padx=20, pady=20)

        # ── Left panel – counters ──────────────
        left = tk.Frame(body, bg=PANEL_COLOR, width=180, padx=16, pady=20)
        left.pack(side="left", fill="y")
        left.pack_propagate(False)

        self._build_counter(left, "LOTE", self.lote_val)
        tk.Frame(left, bg=ACCENT_COLOR, height=1).pack(fill="x", pady=14)
        self._build_counter(left, "Pz",   self.pz_val)

        # ── Center panel – measurement display ─
        center = tk.Frame(body, bg=BG_COLOR)
        center.pack(side="left", fill="both", expand=True, padx=20)

        # Numeric display box
        display_box = tk.Frame(center, bg=DISPLAY_BG,
                               highlightbackground=ACCENT_COLOR,
                               highlightthickness=2)
        display_box.pack(expand=True)

        self._display_label = tk.Label(
            display_box,
            textvariable=self.measure_val,
            font=self._f_display,
            fg=DISPLAY_FG, bg=DISPLAY_BG,
            padx=40, pady=30,
            width=10,
        )
        self._display_label.pack()

        # Format traced value to 4 decimals
        self.measure_val.trace_add("write", self._format_display)
        self._format_display()

        # Unit label below number
        self._unit_label = tk.Label(
            display_box,
            text=self.unit_var.get(),
            font=self._f_unit,
            fg=DIM_TEXT_COLOR, bg=DISPLAY_BG,
            pady=(0), padx=40,
        )
        self._unit_label.pack(pady=(0, 20))
        self.unit_var.trace_add("write",
            lambda *_: self._unit_label.config(text=self.unit_var.get()))

        # Unit selector
        unit_sel = tk.Frame(center, bg=BG_COLOR, pady=12)
        unit_sel.pack()

        tk.Label(unit_sel, text="Units:", font=self._f_label,
                 fg=DIM_TEXT_COLOR, bg=BG_COLOR).pack(side="left", padx=(0, 8))

        for unit in ("dm²", "ft²"):
            tk.Radiobutton(
                unit_sel,
                text=unit,
                variable=self.unit_var,
                value=unit,
                font=self._f_label,
                fg=TEXT_COLOR,
                bg=BG_COLOR,
                selectcolor=COUNTER_ACCENT,
                activebackground=BG_COLOR,
                activeforeground=ACCENT_COLOR,
                indicatoron=0,
                relief="flat",
                borderwidth=0,
                highlightthickness=0,
                padx=14, pady=6,
                cursor="hand2",
            ).pack(side="left", padx=4)

    def _build_counter(self, parent: tk.Frame, name: str, var: tk.IntVar):
        tk.Label(parent, text=name, font=self._f_label,
                 fg=DIM_TEXT_COLOR, bg=PANEL_COLOR).pack(anchor="w")

        tk.Label(parent, textvariable=var,
                 font=self._f_counter, fg=COUNTER_ACCENT,
                 bg=PANEL_COLOR).pack(anchor="w")

    def _format_display(self, *_):
        """Keep the display label showing exactly 4 decimal places."""
        try:
            val = self.measure_val.get()
            self._display_label.config(text=f"{val:,.4f}")
        except tk.TclError:
            pass

    # ── Footer ─────────────────────────────────────────────────────────────
    def _build_footer(self):
        footer = tk.Frame(self, bg=PANEL_COLOR, pady=4)
        footer.pack(fill="x", side="bottom")

        tk.Label(footer, text="RS485 Measurement System",
                 font=self._f_company, fg=DIM_TEXT_COLOR,
                 bg=PANEL_COLOR).pack(side="left", padx=16)

        tk.Label(footer, text="© SCALINI",
                 font=self._f_company, fg=DIM_TEXT_COLOR,
                 bg=PANEL_COLOR).pack(side="right", padx=16)

    # ── Public API (called by backend) ─────────────────────────────────────
    def update_measurement(self, value: float):
        self.measure_val.set(round(value, 4))

    def update_lote(self, value: int):
        self.lote_val.set(value)

    def update_pz(self, value: int):
        self.pz_val.set(value)


if __name__ == "__main__":
    app = MeasurementApp()

    # ── Demo: fake live values ──────────────────
    import random

    def _demo_tick():
        app.update_measurement(random.uniform(0.5, 999.9999))
        app.update_lote(app.lote_val.get() + 1)
        app.update_pz(random.randint(1, 50))
        app.after(1500, _demo_tick)

    _demo_tick()
    app.mainloop()
