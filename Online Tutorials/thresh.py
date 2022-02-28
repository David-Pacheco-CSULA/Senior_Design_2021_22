import cv2 as cv 

img = cv.imread('C:\\Users\\david\\Desktop\\CSULA 2021 Fall\\Senior Design\\Python\\Photos\\Galio.PNG')
cv.imshow('Galio', img)

# TODAY'S LESSON: Thresholding
# Thresholding: is a binary realisation of an image. In general we want to take an image and convert it to a binary image
# where pixels are either zero (black) or 255 (white). An example of this would be if we set a thresholding value of 200, then 
# we would compare every pixel's intensity to that threshold value and if the pixel falls under that threshold value it is set to zero (black)
# otherwise it would be set ot 255 (white)

# Note: A pixel's intensity is its brightness. 
# The histogram shows you how many pixels are at a given intensity level as compared to the others in the image. 
# Black is on the left (0), white on the right (255), and intensities increase as you move to the right.

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding: Disadvantage is that you have to specify the threshold value 

# CV.THRESHOLD function returns 'thresh' which is the thresholded image (binarized image) & 'threshold' which is just the threshold value currently set at '150'
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)  # (Grayscale image, threshold value, once reaching the thresh what do we set it too, threshold type)
cv.imshow('Simple Thresholded', thresh)

# Thresholded Inversed Image
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)  # (Grayscale image, threshold value, once reaching the thresh what do we set it too, threshold type)
cv.imshow('Simple Thresholded Inverse', thresh_inv)


# Adaptive Thresholding: This is able to find the optimal threshold value by itself 
# (Image, Max value, adative method tells the machine which method to use when computing the threshold value, threshold height, kernal size to find the mean, c value which is an integer that is subtracted from the mean to fine tune the threshold)
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 5) #Note: Can also use 'cv.ADAPTIVE_THRESH_GAUSSIAN_C' instead of 'cv.ADAPTIVE...MEAN_C' this adds weight to each of the pixels and provides a better adaptive threshold value
                                                                                                      # butttt there isnt really a one size fits all adaptive method
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)