import cv2 as cv

img = cv.imread('C:\\Users\\david\\Desktop\\CSULA 2021 Fall\\Senior Design\\Python\\Photos\\Galio.PNG') # This is a BGR image (Blue, Green, Red)

cv.imshow('GALIO', img)

# TODAY'S LESSON: Basic Functions in OpenCV

# ESSENTIAL FUNCTION #1: Converting to grayscale from BGR (Seeing the intensity of distribution of pixels instead of the color)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)   # The function convert from one color space to another, 
                                             #'cv.COLOR_BGR2GRAY' is a color code that converts a BGR image to a grayscale image
cv.imshow('Gray', gray)

# ESSENTTIAL FUNCTION #2: Blur an image (Which removes noise from an image (e.g, Bad lighting, Camera sensor issues))
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)  #'ksize' must be an odd number which determines how much an image is blurred (don't worry to much about this right now)
                                                       #'cv.BORDER_DEFAULT' is border type 
cv.imshow('Blur', blur)

# ESSENTIAL FUNCTION #3: Edge Cascade (Finds the edges of the image) values that determine which edges are found 
# Smallest of the thresholds is used for 'edge linking' while the largest is used to find initial segments of strong edges
# You can pass a blurred image to get less edges
canny = cv.Canny(img, 125, 175) # '125' & '175' are threshold 
cv.imshow('Canny Edge', canny)

#ESSENTIAL FUNCTION #4A: How to Dilate an image using a specificed structuring element 
dilated = cv.dilate(canny, (7,7), iterations = 3) # We are passing the 'canny' which is the structuring element here and it makes the edges found thicker 
                                                  # '(7,7)' is the kSize (kernal size) which determines the amount of dilation
                                                  # 'iterations = 3' is the number of times the dialtion is applied   
cv.imshow('Dilated', dilated)

#ESSENTIAL FUNCTION #4B: Eroding which will attempt to pass in a dilated image and return an undilated version of it 
erode = cv.erode(dilated, (7,7), iterations = 3) # Will be close to the undilated image 
                                                 # '(7,7)' is the kSize (kernal size) which determines the amount of erosion
                                                 # 'iterations = 3' is the number of times the erosion is applied   
cv.imshow('Eroded', erode)

#ESSENTIAL FUNCTION #5A: Resizing an image (CBO resize function)
resize = cv.resize(img, (500,500), interpolation = cv.INTER_CUBIC)  # Takes in an image and returns that image into the size you want in this case '(500,500)'
                                                                   # Ignoring the aspect ratio
                                    # 'interpolation = cv.INTER_AREA' is useful if you are shrinking the image 
                                    # 'interpolation = cv.INTER_LINEAR' (FASTER) & 'interpolation = cv.INTER_CUBIC' (SLOW) is useful if you are enlarging an image
cv.imshow('Resize', resize)

#ESSENTIAL FUNCTION #5B: Cropping an image
cropped = img[50:200, 200:400]   #Crops an image (Vertical Crop, Horizontal Crop)
cv.imshow('Cropped', cropped)

cv.waitKey(0)