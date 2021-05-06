import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = cv2.imread("030.PNG")
text = pytesseract.image_to_string(img)
print(text)

# Erick Braun Goecking - 1265 - GEC
# Paola de Souza Freitas - 1474 - GEC
