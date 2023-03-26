# imports libraries
import pytesseract
import cv2
import sys

try:
    # gets the name of the file being looked at
    filename = "uploads/" + sys.argv[1]

    # loads the image
    img = cv2.imread(filename)

    # converts the image text to a string
    text = pytesseract.image_to_string(img)

    # prints outputs
    print(text)

except:
    print("There was an error running this program!")