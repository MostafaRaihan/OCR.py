import pytesseract
from PIL import Image

# Set Tesseract path (only required for Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Input image
img_path = "card.png"
img_open = Image.open(img_path)

# Extract text
text = pytesseract.image_to_string(img_open)

print("Extracted Text:\n")
print(text)
