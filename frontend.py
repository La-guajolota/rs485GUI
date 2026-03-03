"""
RS485 Measurement GUI Frontend

A Streamlit-based graphical user interface for displaying RS485 measurement data.
Optimized for industrial HMI standards and high legibility.

Module: frontend.py
Version: 3.1.0
"""
import streamlit as st
from PIL import Image
import random
import time
from pathlib import Path

# ─────────────────────────────────────────────
# Asset Configuration & Path Resolution
# ─────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
CLIENT_NAME = "CLIENT COMPANY"
CLIENT_LOGO_PATH = BASE_DIR / "companiesLogos" / "clienteLogo.jpg"

SCALINI_NAME = "SCALINI"
SCALINI_LOGO_PATH = BASE_DIR / "companiesLogos" / "scaliniLogo.jpg"

# Standard Industrial Color Palette
BG_COLOR = "#f8fafc"
PANEL_COLOR = "#ffffff"
CARD_COLOR = "#f1f5f9"
ACCENT_COLOR = "#2563eb"
SUCCESS_COLOR = "#16a34a"
TEXT_COLOR = "#1e293b"
TEXT_SECONDARY = "#64748b"
BORDER_COLOR = "#e2e8f0"

def load_logo(path: Path) -> Image.Image | None:
    """Load an image file and return a PIL Image, or None if unavailable."""
    try:
        if path.exists():
            return Image.open(path).convert("RGBA")
        return None
    except Exception:
        return None

def get_custom_css() -> str:
    """Return custom CSS for styling the application."""
    return f"""
    <style>
        /* Reset and Base Variables */
        .stApp {{
            background-color: {BG_COLOR};
        }}
        
        * {{
            font-family: system-ui, -apple-system, sans-serif;
            color: {TEXT_COLOR};
        }}
        
        /* Sidebar Styling */
        section[data-testid="stSidebar"] {{
            background-color: {PANEL_COLOR};
            border-right: 1px solid {BORDER_COLOR};
        }}
        
        /* Containers and Cards */
        .card-panel {{
            background-color: {PANEL_COLOR};
            border: 1px solid {BORDER_COLOR};
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 16px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }}
        
        .metric-container {{
            background-color: {CARD_COLOR};
            border-radius: 6px;
            padding: 16px;
            margin-bottom: 12px;
            border: 1px solid {BORDER_COLOR};
        }}
        
        /* Typography */
        .title-text {{
            font-size: 14px;
            font-weight: 600;
            color: {TEXT_SECONDARY};
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 8px;
        }}
        
        .data-value {{
            font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
            font-size: 24px;
            font-weight: 700;
            color: {TEXT_COLOR};
        }}
        
        /* Primary Display */
        .primary-measurement {{
            font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
            font-size: 84px;
            font-weight: 700;
            color: {ACCENT_COLOR};
            text-align: center;
            line-height: 1.1;
            padding: 30px 0;
        }}
        
        .primary-unit {{
            font-size: 24px;
            color: {TEXT_SECONDARY};
            text-align: center;
            font-weight: 500;
        }}
        
        /* Status Indicators */
        .status-badge {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: #dcfce7;
            padding: 6px 12px;
            border-radius: 16px;
            border: 1px solid #bbf7d0;
            font-size: 12px;
            font-weight: 600;
            color: {SUCCESS_COLOR};
        }}
        
        .status-dot {{
            width: 8px;
            height: 8px;
            background-color: {SUCCESS_COLOR};
            border-radius: 50%;
        }}

        /* Utility */
        #MainMenu, footer, header {{visibility: hidden;}}
    </style>
    """

def init_session_state():
    """Initialize state variables."""
    defaults = {
        "measurement": 0.0000,
        "lote": 1,
        "pz": 0,
        "unit": "dm²",
        "num_lotes": 1,
        "piezas_por_lote": 0,
        "num_pieles": 0,
        "area_total_cortada": 0.0,
        "area_piel_actual": 0.0,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def build_sidebar():
    """Construct the lateral control panel."""
    with st.sidebar:
        st.markdown(f"""
            <div style="text-align: center; padding: 10px 0 20px 0;">
                <h2 style="color: {ACCENT_COLOR}; margin: 0; font-weight: 700;">RS485 HMI</h2>
                <div class="status-badge" style="margin-top: 10px;">
                    <div class="status-dot"></div>
                    <span>SYSTEM ONLINE</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        tab_prod, tab_area, tab_sys = st.tabs(["Producción", "Áreas", "Sistema"])
        
        with tab_prod:
            st.markdown('<div class="title-text">Métricas de Producción</div>', unsafe_allow_html=True)
            st.markdown(f"""
                <div class="metric-container">
                    <div class="title-text" style="font-size: 11px;">Lotes Activos</div>
                    <div class="data-value">{st.session_state.num_lotes}</div>
                </div>
                <div class="metric-container">
                    <div class="title-text" style="font-size: 11px;">Piezas / Lote</div>
                    <div class="data-value">{st.session_state.piezas_por_lote}</div>
                </div>
                <div class="metric-container">
                    <div class="title-text" style="font-size: 11px;">Total Pieles</div>
                    <div class="data-value">{st.session_state.num_pieles}</div>
                </div>
            """, unsafe_allow_html=True)
            
        with tab_area:
            st.markdown('<div class="title-text">Datos de Superficie</div>', unsafe_allow_html=True)
            st.markdown(f"""
                <div class="metric-container">
                    <div class="title-text" style="font-size: 11px;">Área Total</div>
                    <div class="data-value">{st.session_state.area_total_cortada:,.1f} {st.session_state.unit}</div>
                </div>
            """, unsafe_allow_html=True)
            
            utilization = 0
            if st.session_state.area_piel_actual > 0:
                utilization = (st.session_state.measurement / st.session_state.area_piel_actual) * 100
                
            st.markdown(f"""
                <div class="metric-container">
                    <div class="title-text" style="font-size: 11px;">Eficiencia de Corte</div>
                    <div class="data-value" style="color: {SUCCESS_COLOR};">{utilization:.1f}%</div>
                </div>
            """, unsafe_allow_html=True)

        with tab_sys:
            st.markdown('<div class="title-text">Parámetros RS485</div>', unsafe_allow_html=True)
            st.selectbox("Puerto COM", ["/dev/ttyUSB0", "/dev/ttyUSB1", "/dev/ttyACM0"], key="puerto")
            st.selectbox("Baudrate", [9600, 19200, 38400, 57600, 115200], index=4, key="baudrate")
            
            if st.button("Aplicar Parámetros", use_container_width=True):
                st.success("Configuración aplicada.")
                
            st.markdown("<hr>", unsafe_allow_html=True)
            if st.button("Simular Entrada", use_container_width=True):
                st.session_state.measurement = random.uniform(10, 200)
                st.session_state.num_lotes = random.randint(1, 10)
                st.session_state.piezas_por_lote = random.randint(50, 150)
                st.session_state.num_pieles = random.randint(100, 500)
                st.session_state.area_total_cortada = random.uniform(5000, 15000)
                st.session_state.area_piel_actual = random.uniform(200, 300)
                st.session_state.lote = st.session_state.num_lotes
                st.session_state.pz = st.session_state.piezas_por_lote
                st.rerun()

def build_top_bar():
    """Construct the identification header."""
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown(f'<div style="font-weight: 600; font-size: 18px; color: {TEXT_SECONDARY}; padding-top: 10px;">{CLIENT_NAME}</div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div style="font-weight: 600; font-size: 18px; color: {ACCENT_COLOR}; text-align: right; padding-top: 10px;">{SCALINI_NAME}</div>', unsafe_allow_html=True)

def build_main_display():
    """Construct the primary measurement visualization."""
    st.markdown('<div class="card-panel">', unsafe_allow_html=True)
    
    # Primary Value Display
    st.markdown('<div class="title-text" style="text-align: center;">Lectura Actual del Sensor</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="primary-measurement">{st.session_state.measurement:,.4f}</div>', unsafe_allow_html=True)
    
    # Unit Selector
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        unit = st.radio("Unit", options=["dm²", "ft²"], horizontal=True, label_visibility="collapsed")
        st.session_state.unit = unit

    st.markdown('</div>', unsafe_allow_html=True)
    
    # Secondary Data Row
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown(f"""
            <div class="card-panel" style="text-align: center;">
                <div class="title-text">Lote Actual</div>
                <div class="data-value">{st.session_state.lote}</div>
            </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.markdown(f"""
            <div class="card-panel" style="text-align: center;">
                <div class="title-text">Piezas Procesadas</div>
                <div class="data-value">{st.session_state.pz}</div>
            </div>
        """, unsafe_allow_html=True)
    with col_c:
        st.markdown(f"""
            <div class="card-panel" style="text-align: center;">
                <div class="title-text">Pieles Totales</div>
                <div class="data-value">{st.session_state.num_pieles}</div>
            </div>
        """, unsafe_allow_html=True)

def main():
    """Execution entry point."""
    st.set_page_config(page_title="HMI Measurement", layout="wide", initial_sidebar_state="expanded")
    init_session_state()
    st.markdown(get_custom_css(), unsafe_allow_html=True)
    
    build_sidebar()
    
    st.markdown('<div class="card-panel" style="padding: 10px 20px;">', unsafe_allow_html=True)
    build_top_bar()
    st.markdown('</div>', unsafe_allow_html=True)
    
    build_main_display()

if __name__ == "__main__":
    main()