import pytesseract
from PIL import Image
from io import BytesIO
import base64

def process_image(image):
    # Decode base64 image
    image_data = base64.b64decode(image)
    image = Image.open(BytesIO(image_data))
    
    # Perform OCR
    text = pytesseract.image_to_string(image)
    return text