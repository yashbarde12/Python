# Face Detection
'''
Haar Cascade -
It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images
It is then used to detect objects in other images
'''
'''
import cv2

# Create a CascadeClassifier Object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
 
# Reading the image as it is
img = cv2.imread("Images/hritik.jpg")
 
# Reading the image as gray scale image
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
# Search the co-ordintes of the image
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors=5)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)
 
cv2.imshow("Gray", img)
 
cv2.waitKey(10000)
 
cv2.destroyAllWindows()
'''
# Video Capture

import cv2  
import numpy as np  
  
cap = cv2.VideoCapture(0)  
  
while(True):  
    # Capture image frame-by-frame  
    ret, frame = cap.read()  
  
    # Our operations on the frame come here  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
  
    # Display the resulting frame  
    cv2.imshow('frame',gray)  
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break  
  
# When everything done, release the capture  
cap.release()  
cv2.destroyAllWindows()

