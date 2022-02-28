import cv2 as cv
import numpy as np

img = cv.imread('C:\\Users\\david\\Desktop\\CSULA 2021 Fall\\Senior Design\\Python\\Photos\\Galio.PNG')
cv.imshow('Galio', img)

# TODAY'S LESSON: Masking
# Maksing allows one to focus on a certain part of an image (cuts out a part of an image)
# i.e If you wanted to focus on a person's face than you can use masking to do that 


# Blank must be the same size as the image or it will fail (-215 : Assertion Failed)
blank = np.zeros(img.shape[:2], dtype = 'uint8')
cv.imshow('Blank Image', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45,img.shape[0]//2) , 100, 255,-1) # '45' are pixel movements
# cv.imshow('Mask', circle)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1) # Make a rectangle on the blank image

werid_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird Shape', werid_shape)

masked = cv.bitwise_and(img,img, mask = werid_shape) #'mask' = 'werid_shape' is a condition that cuts out a 'werid_shape' portion out of the original 'img'
cv.imshow('Masked Image', masked)



cv.waitKey(0)