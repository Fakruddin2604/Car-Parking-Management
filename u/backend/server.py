# app.py (Flask back end)
import numpy as np
import cv2 
import  imutils
import pytesseract
import pandas as pd
import time
import mysql.connector
import datetime
import sys
import re
import time
import requests
from flask import Flask, send_file, make_response
from PyQt5 import QtCore, QtWidgets, uic

pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"

app = Flask(__name__)

@app.route("/image")
def image():
    # The path of the image file
    image_path = 'images/4.jpg'

    # Read and resize the image
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    img = imutils.resize(img, width=500)

    # Convert the image to grayscale and apply filters
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(gray, 170, 200)

    # Find the contours and select the one with four corners
    cnts= cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30] 
    NumberPlateCnt = None 

    count = 0
    for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            if len(approx) == 4:  
                    NumberPlateCnt = approx 
                    break

    # Mask the part other than the number plate
    mask = np.zeros(gray.shape,np.uint8)
    new_image = cv2.drawContours(mask,[NumberPlateCnt],0,255,-1)
    new_image = cv2.bitwise_and(img,img,mask=mask)

    # Configuration for tesseract
    config = ('-l eng --oem 1 --psm 3')

    # Run tesseract OCR on image
    text = str(pytesseract.image_to_string(new_image, config=config))

    # Return the image file and the text as a response
    response = make_response(text)
    response.headers['Content-Type'] = 'text/plain'
    return send_file(image_path, mimetype='image/jpeg'), response

if __name__ == "__main__":
    app.run(debug=True)
