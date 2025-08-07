#pip install pytesseract
#pip install pillow
import pytesseract
from  PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img_path='card.png'
img_open=Image.open(img_path)
text=pytesseract.image_to_string(img_open,)

print(text)
