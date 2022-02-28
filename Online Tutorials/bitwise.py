import cv2 as cv
import numpy as np

# TODAY'S LESSON: BITWISE OPERATORS
# Pixel is turned off if given a value of zero and turned on when given a value of 1

def rescaleFrame (frame, scale =1):  # Function takes in a frame and rescales it by the scale value (CURRENTLY SET TO: 25%)
    width = int(500)  # 'frame.shape[1]' returns the width of the image & int(frame.shape[1]) makes the width an integer
    height = int(500) # 'frame.shape[0]' returns the height of the image & int(frame.shape[0]) makes the height an integer
    dimensions = (width,height)          # varible storing width and height 

    return cv.resize(frame, dimensions,interpolation=cv.INTER_AREA) # We will talk about this later in depth but for now just know

publicPlace = cv.imread('C:\\Users\\david\\Desktop\\CSULA 2021 Fall\\Senior Design\\Python\\Photos\\Public Place.PNG')
galio = cv.imread('C:\\Users\\david\\Desktop\\CSULA 2021 Fall\\Senior Design\\Python\\Photos\\Galio.PNG')

publicPlace = rescaleFrame(publicPlace)
galio = rescaleFrame(galio)

bitwise_and = cv.bitwise_and(publicPlace, galio)

cv.imshow('TRYING', bitwise_and)



blank = np.zeros((400,400), dtype = 'uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1) # Make a rectangle on the blank image
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1) # Make a circle on a blank image

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# Bitwise AND: (Intersecting regions) The common dot of both images gets carried over.
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

# Bitwise OR: (Non-intersecting & Intersecting regions) Any pixel that was ON either of the images was placed on a new image
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# Bitwise XOR: (Non-intersecting regions) When one image's pixels is ON and one image's pixel is OFF than the new image will be on otherwise off
bitwise_xor = cv.bitwise_xor(rectangle, circle) 
cv.imshow('Bitwise XOR', bitwise_xor)

# Bitwise NOT: It inverts the ON and OFF pixels of a image.
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Rectangle NOT', bitwise_not)


cv.waitKey(0) 