"""
Author  :   Adrián Silva Palafox
Date    :   2026-03-05
Brief   :   PDF receipt generator utilizing the FPDF library.
            Constructs an A4 formatted document integrating customer logos, 
            client metadata, and structured tables mapping leather area measurements.
"""
from fpdf import FPDF
import pandas as pd
import os
from datetime import datetime

class ReceiptPDF(FPDF):
    """
    Subclass of FPDF structured for A4 generation incorporating corporate headers.
    
    Attributes:
        client_name (str): The commercial name or corporate entity of the client.
        client_address (str): The physical address associated with the client.
        client_logo_path (str): The absolute file path to the client's localized logo asset.
    """
    
    def __init__(self, client_name: str, client_address: str, client_logo_path: str = ""):
        """
        Initializes the document rendering parameters to standard A4 specifications.

        Args:
            client_name (str): Entity name for the header.
            client_address (str): Entity address for the header.
            client_logo_path (str, optional): System path to a valid JPG/PNG file. Defaults to "".
        """
        super().__init__(format='A4', unit='mm')
        self.client_name = client_name
        self.client_address = client_address
        self.client_logo_path = client_logo_path
        self.set_auto_page_break(auto=True, margin=15)

    def header(self):
        """
        Overrides the native FPDF header method. Renders company logos and metadata 
        at the top margin of every generated page.
        """
        if self.client_logo_path and os.path.exists(self.client_logo_path):
            try:
                self.image(self.client_logo_path, 10, 8, 35)
            except Exception as e:
                print(f"Error loading logo into PDF: {e}")
        
        self.set_font("helvetica", "B", 16)
        self.cell(0, 8, "MÁQUINA DE MEDICIÓN - MODELO 602", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("helvetica", "", 12)
        self.cell(0, 6, f"Cliente: {self.client_name}", align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 6, f"Dirección: {self.client_address}", align="C", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 6, f"Fecha de impresión: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", align="C", new_x="LMARGIN", new_y="NEXT")
        
        self.ln(5)
        self.set_line_width(0.5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(8)


def generate_receipt(dataframe: pd.DataFrame, client_name: str, client_address: str, logo_path: str, output_path: str) -> bool:
    """
    Parses an input DataFrame and builds a complete A4 PDF receipt detailing 
    individual piece measurements and aggregate batch totals.
    
    Args:
        dataframe (pd.DataFrame): Dataset of measurements obtained during the active session.
        client_name (str): Commercial name of the client.
        client_address (str): Billing or physical address of the client.
        logo_path (str): File path to the client's logo image.
        output_path (str): Absolute path to the session's Excel file used to derive 
                           the PDF output destination.
                           
    Returns:
        bool: True if generation was successful. False if the provided dataframe was empty.
    """
    if dataframe.empty:
        return False

    pdf = ReceiptPDF(client_name=client_name, client_address=client_address, client_logo_path=logo_path)
    pdf.add_page()
    
    current_lote = None
    lote_total = 0.0

    col_lote_w = 40
    col_pieza_w = 40
    col_area_w = 110

    for index, row in dataframe.iterrows():
        lote = row['Lote']
        pieza = row['Pieza']
        area = row['Area']

        if lote != current_lote:
            if current_lote is not None:
                pdf.set_font("helvetica", "B", 12)
                pdf.cell(col_lote_w + col_pieza_w, 8, "TOTAL DEL LOTE:", border=0, align="R")
                pdf.cell(col_area_w, 8, f"{round(lote_total, 2)} Dm2", border=0, align="C", new_x="LMARGIN", new_y="NEXT")
                pdf.ln(5)
                
            current_lote = lote
            lote_total = 0.0
            
            pdf.set_font("helvetica", "B", 12)
            pdf.set_fill_color(220, 230, 240)
            pdf.cell(0, 10, f"REGISTRO DEL LOTE # {current_lote}", border=1, fill=True, align="L", new_x="LMARGIN", new_y="NEXT")
            
            pdf.set_font("helvetica", "B", 10)
            pdf.cell(col_lote_w, 8, "LOTE", border=1, align="C")
            pdf.cell(col_pieza_w, 8, "PIEZA #", border=1, align="C")
            pdf.cell(col_area_w, 8, "ÁREA (Dm2)", border=1, align="C", new_x="LMARGIN", new_y="NEXT")

        pdf.set_font("helvetica", "", 10)
        pdf.cell(col_lote_w, 8, str(lote), border=1, align="C")
        pdf.cell(col_pieza_w, 8, str(pieza), border=1, align="C")
        pdf.cell(col_area_w, 8, f"{area:.2f}", border=1, align="C", new_x="LMARGIN", new_y="NEXT")
        
        lote_total += float(area)

    if current_lote is not None:
        pdf.set_font("helvetica", "B", 12)
        pdf.cell(col_lote_w + col_pieza_w, 8, "TOTAL DEL LOTE:", border=0, align="R")
        pdf.cell(col_area_w, 8, f"{round(lote_total, 2)} Dm2", border=0, align="C", new_x="LMARGIN", new_y="NEXT")

    pdf_filename = output_path.replace('.xlsx', '.pdf')
    pdf.output(pdf_filename)
    return True