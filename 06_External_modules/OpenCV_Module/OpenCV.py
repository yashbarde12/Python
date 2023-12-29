# OpenCV Module
# Only uncomment (""" """)each section before executing for understanding.
#--------------------------------------------------------
# Read an image - imread()
"""
import cv2
img = cv2.imread("Images/taj.jpg", 1)   # 1 denotes colored image
cv2.imshow("Image",img)    # To display the image
cv2.waitKey(5000)          # Required - image doesn't close immediately
cv2.destroyAllWindows()
"""
#--------------------------------------------------------
# Accessing and Modifying pixel values
"""
import numpy as np
import cv2
img = cv2.imread("Images/taj.jpg",0)
pixel = img[30,200]
print(pixel)
"""
#--------------------------------------------------------
# Accessing Image Properties
"""
import cv2
img = cv2.imread("Images/taj.jpg",1)
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
size1 = img.size
print(img.shape)
print("Image height:", height)
print("Image width:", width)
print("No of channels:", channels)
print("Image size:", size1)
"""
#--------------------------------------------------------
# Resize an Image
#Method 1
"""
import cv2
img = cv2.imread("Images/taj.jpg",1)
cv2.imshow("Taj", img)
resized = cv2.resize(img, (600,900))
cv2.imshow("TajMahal",resized)
cv2.waitKey(10000)          
cv2.destroyAllWindows()
"""
#--------------------------------------------------------
#Method 2
"""
import cv2
img = cv2.imread("Images/taj.jpg",1)
resized = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("TajMahal",resized)
cv2.waitKey(10000)          
cv2.destroyAllWindows()
"""
#--------------------------------------------------------
# Image Rotation
"""
import cv2
img = cv2.imread("Images/taj.jpg",1)
(h,w) = img.shape[:2]
center = (w/2,h/2)

r1 = cv2.getRotationMatrix2D(center, 90, 1)
r90 = cv2.warpAffine(img, r1, (h,w))

cv2.imshow("TajMahal Original",img)


cv2.imshow("TajMahal Rotated 90 degrees",r90)
cv2.waitKey(10000)          
cv2.destroyAllWindows()

"""
#--------------------------------------------------------
#--------------------------------------------------------
