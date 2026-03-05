from bill_generartor import ReceiptPDF as billGen
from bill_generartor import generate_receipt
import pandas as pd

frame = pd.DataFrame({
    "Lote": [1, 1, 1, 2, 2],
    "Pieza": [1, 2, 3, 1, 2],
    "Area": [10.5, 20.0, 15.75, 5.0, 12.25]
})

ticket = billGen("Juan", "Calle Falsa 123")
result = generate_receipt(dataframe=frame, client_name="Cliente de Prueba", output_path="C:\\Users\\lapto\\OneDrive\\Desktop\\rs485GUI\\tkinter_ver\\backend\\test_receipt.pdf")
print("Receipt generated:", result) 