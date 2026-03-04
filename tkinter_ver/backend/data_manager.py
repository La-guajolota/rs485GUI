import pandas as pd
import os
from datetime import datetime

class DataManager:
    def __init__(self):
        self.current_session_file = None

    def create_session(self, client_name, output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{client_name}_{timestamp}.xlsx"
        self.current_session_file = os.path.join(output_dir, filename)
        
        df = pd.DataFrame(columns=["Lote", "Pieza", "Area", "Timestamp"])
        df.to_excel(self.current_session_file, index=False)
        return self.current_session_file

    def append_data(self, lote, pieza, area):
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