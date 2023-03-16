# imports libraries
import pytesseract
import cv2
import sys
from langdetect import detect 
from translate import Translator


try:
    # gets the name of the file being looked at
    filename = "uploads/" + sys.argv[1]

    # loads the image
    img = cv2.imread(filename)

    # converts the image text to a string
    text = pytesseract.image_to_string(img)

    # detects the language
    lang = detect(text)

    # creates the translation
    translator = Translator(from_lang=lang, to_lang='en')
    trans = translator.translate(text)

    # prints outputs
    print("Text: " + text)
    print("<br>Translated: " + trans)

except:
    print("There was an error running this program!")