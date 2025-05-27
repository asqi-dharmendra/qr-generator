import qrcode
import os


def generate_qr_code(data):
    """
    Generate a QR code from data and save it to the static folder.

    Args:
        data (str): The data to encode in the QR code

    Returns:
        str: The relative path to the QR code image within the static folder
    """
    # Create QR code directory if it doesn't exist
    qr_dir = os.path.join("app", "static", "qrcodes")
    if not os.path.exists(qr_dir):
        os.makedirs(qr_dir)

    # Generate unique filename
    if data is None or data.strip() == "":
        raise ValueError("Data for QR code cannot be empty or None.")
    filename_str = (
        data.strip().replace(" ", "_").replace(".", "_").replace("/", "_")
    )  # Replace spaces with underscores for filename safety
    filename = f"{filename_str}.png"
    relative_path = os.path.join("qrcodes", filename)
    filepath = os.path.join("app", "static", relative_path)

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create image and save
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filepath)

    return relative_path
