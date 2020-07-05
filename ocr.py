import numpy as np
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  ##Path of tesseract installed

image=cv2.imread("in.jpg")  #loading the image

gray = cv2.cvtColor(x,cv2.COLOR_BGR2GRAY)  #converting the image to grayscale


text = pytesseract.image_to_string(gray)   #reading the text from the image

with open("file.txt","w") as f:    #writing the read text in the file
	f.write(text)
	f.close()

cv2.imshow("gray",gray)           		#showing the gray image
cv2.imshow("image",image)		  		#showing the original image
		
cv2.waitKey(0)                          #enter any key to exit
	