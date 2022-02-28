import cv2 as cv
import numpy as np

img = cv.imread('C:\\Users\\david\\Desktop\\CSULA 2021 Fall\\Senior Design\\Python\\Photos\\Galio.PNG')
cv.imshow('Boston', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

# TODAY'S LESSON: COLOR CHANNELS
# How to split and merge color channels
# Any color image consists of 3 color channels (red, green, blue) which we can then split and merge them

b,g,r = cv.split(img)

# The following allows one to print out solely the blue, red, or green parts of an image
# by setting the other two to the blank image
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)


# All the color channels will be in grayscale that show the distribution of pixel intensities
# Regions where its lighter shows there is a far more concentration of those pixels be it (red, green, blue)
# Regions where its darker shows there is a far less more concentration of those pixels be it (red, green, blue)
cv.imshow('Blue GrayScale', b)
cv.imshow('Green GrayScale', g)
cv.imshow('Red GrayScale', r)

# prints out (height, length, # of Color Channels)
print(img.shape) #Original Image 
print(b.shape) # Blue color channel
print(g.shape) # Green color channel
print(r.shape) # Red color channel

merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)