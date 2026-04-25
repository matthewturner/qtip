# Creates a Version 7 QR Code with quality error 
# correction and saves it as an image file. 
# The data to encode is read from 'input.txt'.

import qrcode
import os
from qrcode.constants import ERROR_CORRECT_Q

def create_qr(data, version=7, filename="version7_qr.png"):
    """
    Create a Version 7 QR Code with quality error correction.
    
    Parameters:
        data (str): The text or URL to encode.
        filename (str): Output image file name.
    """
    try:
        if not isinstance(data, str) or not data.strip():
            raise ValueError("Data must be a non-empty string.")

        # Create QRCode object with specified version
        qr = qrcode.QRCode(
            version=version,
            error_correction=ERROR_CORRECT_Q,  # Quality error correction
            box_size=10,  # Pixel size of each module
            border=1      # Border size in modules
        )

        qr.add_data(data)
        qr.make(fit=False)  # fit=False ensures fixed version

        # Generate image
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)

        print(f"QR Code saved as '{filename}'")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if not os.path.exists("input.txt"):
        print("Warning: 'input.txt' was not found.")
        exit()

    with open("input.txt", "r") as f:
        data = f.read()

    version = 7
    create_qr(data, version, filename=f"version{version}_qr.jpg")