import cv2 as cv
import numpy as np

img = cv.imread('C:\\Users\\david\\Desktop\\CSULA 2021 Fall\\Senior Design\\Python\\Photos\\Galio.PNG')
cv.imshow('Galio', img)

# TODAY'S LESSON: Gradient & Edge Detection (Note: For most cases you can think of gradients as these edge like regions that are present in an image (programmers perspective only))
# Previously we focused on 'CANNY' edge detection which is an advanced multi stepped edge detection algorithm. 
# In this lesson we will be focusing on Laplacian & Sobel method

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian: (Basically Finds Gradient) Gives the lapacian edges in the image  (Smugged image)
lap = cv.Laplacian(gray, cv.CV_64F)  # (Source Image, Data depth)
lap = np.uint8(np.absolute(lap)) # Converted lap to uint8 and took the absolute value
                                 # When you convert the image using laplacian it gives the pixels negative and positve pixel intensity values
                                 # You can't have negative values so you use absolute value to change them positve then you change into the correct data type
cv.imshow('Laplacian', lap)

# Sobel: Computes gradients in two directions (x,y) (Looks more staticy)
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)  # Gradient in the x direction: (Source image, Data depth, x direction, y direction)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)  # Gradient in the y direction: (Source image, Data depth, x direction, y direction)
combined_sobel = cv.bitwise_or(sobelx, sobely) # Combining the gradients in the x and y directions

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

# Canny: (AGAIN)
# The previously learned gradient technique (Pencil tracing of the edges) the is an advanced version and clearly better (Actually uses Sobel in it's multistep process)
canny = cv.Canny(gray, 150, 175) 
cv.imshow('Canny', canny)

# But then again determining which is best really DEPENDS ON THE SITUATION

cv.waitKey(0)

