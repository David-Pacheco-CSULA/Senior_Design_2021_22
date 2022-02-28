import cv2 as cv
import numpy as np

img = cv.imread('C:\\Users\\david\\Desktop\\CSULA 2021 Fall\\Senior Design\\Python\\Photos\\Public Place.PNG')

cv.imshow('Public Walkway', img)

blank = np.zeros(img.shape, dtype = 'uint8')  # Blank image 
cv.imshow('Blank', blank)

# TODAY'S LESSON: Contour Detection
# Contours are the boundaries of objects (Not the same as edges (mathematically))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #Coverts from BGR to Gray scale 
cv.imshow('Gray', gray)


#                       Method 1: Finding Contours (Canny)
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT) #Blurs image, we do this to get less edges and less contours
cv.imshow('Blur', blur)
canny = cv.Canny(blur, 65, 65) # Grabs the edges of the image this time pass 'blur' img to get less edges
cv.imshow('Canny Edges', canny)


#                       Method 2: Finding Contours (Thresholds)
# Threshold looks at an image and tries to binarize it, if the intensity of a pixel is under the threshold value then it will be set to zero (blank), if above it will be set to white (255) 
# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)   # '125' threshold value, '255' max value, 'cv.THRESH_BINARY' thresholding type: this one binarizes the image 
# cv.imshow('Thresh', thresh)



#'cv.findCountours' method looks at the structuring element (edges found in the image) and returns (COUNTOURS & HIERARCHIES)
# COUNTOURS: Is the python list of all the coordinates of all of the coutours found
# HIERARCHIES: Refers the hierarchal representation of contours like in a contour there might be another countour within that and so on and so on
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# ( 1. Structuring element (i.e, canny, thre), 2. The extent of the contours you want to find, 3. How we want to approximate the contour)
# 2. 'cv.RETR_LIST' returns all the contours, 'cv.RETR_EXTERNAL' returns only the external contours, 'cv.RETR_TREE' returns all the hierarchal contours
# 3. 'cv.CHAIN_APPROX_NONE' does nothing returns all of the contour coordinates, 'cv.CHAIN_APPROX_SIMPLE' compresses all the contours 
#    For Example: If you had a line and you put '..._NONE' this would return every contour point on the line, if you have '..._SIMPLE' it would only return the contour endpoints


# Since contours is a list we can find the length of the list (# of contours)
# '{len(contours)}' # number of contours
print(f'{len(contours)} contours(s) found!')


# Now we can draw those contours that OpenCV found on a blank image 
cv.drawContours(blank, contours, -1, (255,255,255), 1)   # (Image to draw over, list of contours, contours index which is how many contours you want '-1' means all contours,
                                                      # (0,0,255) => red, '1' thickness)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)