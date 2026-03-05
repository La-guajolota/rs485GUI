from PIL import Image
import os

# Define relative paths
input_jpg = "../docs/companiesLogos/scaliniLogo.jpg"
output_ico = "../docs/companiesLogos/icono.ico"

try:
    # Open the existing JPG
    img = Image.open(input_jpg)
    
    # Force a square aspect ratio required for Windows icons
    img_resized = img.resize((256, 256), Image.LANCZOS)
    
    # Save with the ICO format encoder
    img_resized.save(output_ico, format="ICO", sizes=[(256, 256)])
    print(f"Success: Icon generated at {os.path.abspath(output_ico)}")
except Exception as e:
    print(f"Error during conversion: {e}")