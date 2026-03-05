"""
Author  :   Adrián Silva Palafox
Date    :   2026-03-05
Brief   :   Data management class handling continuous storage and retrieval 
            of measurement parameters via Excel file operations.
"""
import pandas as pd
import os
from datetime import datetime

class DataManager:
    """
    Manages structured data inputs and controls the persistence layer.
    
    Attributes:
        current_session_file (str): The absolute path pointing to the active session's .xlsx file.
    """
    
    def __init__(self):
        """Initializes the DataManager instance with a null session state."""
        self.current_session_file = None

    def create_session(self, client_name: str, client_address: str, output_dir: str) -> str:
        """
        Creates a new directory if necessary and initializes a base Excel file 
        containing data headers for the current measurement tracking session.
        
        Args:
            client_name (str): Identity string used for timestamped file generation.
            client_address (str): Target physical address parameter (stored dynamically).
            output_dir (str): Absolute path designating the output target directory.
            
        Returns:
            str: The absolute path of the generated .xlsx session file.
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{client_name}_{timestamp}.xlsx"
        self.current_session_file = os.path.join(output_dir, filename)
        
        df = pd.DataFrame(columns=["Lote", "Pieza", "Area", "Timestamp"])
        df.to_excel(self.current_session_file, index=False)
        return self.current_session_file

    def append_data(self, lote: int, pieza: int, area: float) -> bool:
        """
        Appends a discrete measurement row into the active session file using OpenPyxl logic.
        
        Args:
            lote (int): The associated batch index.
            pieza (int): The current leather piece index within the batch.
            area (float): The calculated dimensional area in square decimeters (Dm2).
            
        Returns:
            bool: True if writing succeeded. False if no active session file is designated.
        """
        if not self.current_session_file:
            return False
            
        new_data = pd.DataFrame([{
            "Lote": lote,
            "Pieza": pieza,
            "Area": area,
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }])
        
        with pd.ExcelWriter(self.current_session_file, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
            startrow = writer.sheets['Sheet1'].max_row
            new_data.to_excel(writer, index=False, header=False, startrow=startrow)
        return True

    def get_current_dataframe(self) -> pd.DataFrame:
        """
        Reads the target .xlsx file for the active session and returns a structured DataFrame.
        
        Returns:
            pd.DataFrame: Compiled dataset corresponding to the current measurement session.
                          Returns an empty DataFrame if no session file exists or read errors occur.
        """
        if self.current_session_file and os.path.exists(self.current_session_file):
            try:
                return pd.read_excel(self.current_session_file)
            except Exception as e:
                print(f"Error reading session Excel file: {e}")
        return pd.DataFrame()