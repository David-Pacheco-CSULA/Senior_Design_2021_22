import cv2 as cv
import numpy as np #Provides array and lists related operations

img = cv.imread('C:\\Users\\david\\Desktop\\CSULA 2021 Fall\\Senior Design\\Python\\Photos\\Public Place.PNG')

cv.imshow('Galio', img)


# TODAY'S LESSON: Tranformations
# Transformations shifts an image up, down, left, right, or any combination


def translate(img, x, y):        #Translate function: x & y describe the number of pixels you want to shift along the x or y axis
    transMat = np.float32([[1,0, x],[0,1,y]]) #Translation matrix: Takes a list with two lists inside of it
    dimensions = (img.shape[1], img.shape[0]) #Getting the dimensions of the image (width, height)
    return cv.warpAffine(img, transMat, dimensions) #Returns the shifted image (IMAGE, TRANSLATION MATRIX, DIMENSIONS)

# -x --> Left
# -y --> Up
#  x --> Right 
#  y --> Down

translated = translate(img, -100, 100) #Calling translation function
cv.imshow('Translated', translated)


# Rotation: Rotate an image by some angle


def rotate(img, angle, rotPoint=None): # rotPoint => ROTATION POINT
    (height,width) = img.shape[:2] # Gets Height and width of image

    if rotPoint is None: #'if rotPoint is None:' just means the rotation point is in the center of the image
        rotPoint = (width//2, height//2)  #So we set the rotPoint to the center of the image

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) #Rotation Matrix: (Rotations Point, angle, scale value)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions) #Returns the rotated image (IMAGE, Rotation Matrix, Dimensions of Image)

rotated = rotate(img, 45)  # Calling rotation function 
cv.imshow('Rotated', rotated)

# Note you can also rotate an already rotated image byyy:
rotated_rotated = rotate(rotated, -45) # Note: Doing this will not return the orginal value if the rotated image filled in the blank spaces with black
                                       # As when you rotate part of the image is cut off and those cut off parts don't return when you rotate it the other direction.
cv.imshow('Rotated Rotated', rotated_rotated)


# Resizing Image (Again): Resizes image


resized = cv.resize(img, (500,500), interpolation = cv.INTER_CUBIC)  # ALREADY WENT OVER THIS TOPIC
cv.imshow('Resize', resized)


# Flipping: Flips image


flip = cv.flip(img, 0)  #'0' flips over the x axis & '1' flips over the y axis & '-1' flips both over the x & y axis
cv.imshow('Flip', flip)


# Cropping: Crops image

cropped = img[200:400, 300:400] # ALREADY WENT OVER THIS TOPIC
cv.imshow('Croppped', cropped)

cv.waitKey(0)