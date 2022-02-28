import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('C:\\Users\\david\\Desktop\\CSULA 2021 Fall\\Senior Design\\Python\\Photos\\Public Place.PNG')
cv.imshow('Public Place', img)

# TODAY'S LESSON: COLOR SPACES
# How to siwtch between color spaces in OpenCV
# A system of representing an array of pixel colors (i.e, RGB & Grayscale)

#   # Outside of OpenCV we use RGB format which is the inverse of the BGR format
#   # Sooooo you get an inversion of colors 
#   # You will se an inversion of colors because matplotlib reads images in RGB format 
#   plt.imshow(img) 
#   plt.show()

# YOU CAN COVERT BETWEEN ANY OF THESE COLOR SPACES EXCEPT...
# NOTE: CANT CONVERT GRAYSCALE TO HSV DIRECTLY

# BGR (Default) to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV (Hue saturation color)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB or L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb) # Now you gave OpenCV a RGB image and it thought it was a BGR image so the colors are inversed 

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('BGR', hsv_bgr)

plt.imshow(rgb)
plt.show() # A RGB image is passed so matplotlib and since the default for matplotlib is RGB it correctly showed the image

cv.waitKey(0)