import pytesseract
import cv2
import sys

try:
    filename = "uploads/" + sys.argv[1]

    img = cv2.imread(filename)
    text = pytesseract.image_to_string(img)

    print(text)
except:
    print("There was an error running this program!")