import barcode
from barcode.writer import ImageWriter
import base64
from io import BytesIO

def generate_barcode_image(barcode_data):
    ean = barcode.get('ean13', barcode_data, writer=ImageWriter())
    buffer = BytesIO()
    ean.write(buffer)
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return image_base64