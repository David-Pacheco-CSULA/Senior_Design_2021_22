import cv2 as cv

img = cv.imread('C:\\Users\\david\\Desktop\\CSULA 2021 Fall\\Senior Design\\Python\\Photos\\Public Place.PNG')
cv.imshow('Galio', img)

# TODAY'S LESSON: Blurring & Smoothing

# Blur: A Kernal is the number of a window in a square so basically the number of rows and number of coloums
# So a Kernal Size of (3,3) would be a square consisting of 9 windows (3 by 3)
# Blur is then applied to the middle of that 3 by 3 window. 



# Averaging: In that example (the (3,3) window) every windows intensity is set to the average intensity of those 9 windows. 
# That 3 by 3 window then moves around the entire image and the samething happens 

average = cv.blur(img, (9,9)) # The high the kernal size the higher the blur
cv.imshow('Average Blur' , average)


# Gaussian Blur: Samething as averaging except that instead of averaging the intensities each of the windows is given a weight
# and a proper blur locaiton is found in the square and it provides a more natural blur although it is usually less overall blur

gauss = cv.GaussianBlur(img, (9,9), 0) #'0' standard deviation in the x direction
cv.imshow('Gaussian Blur', gauss)

# Median Blur: Samething as averaging except that instead of finding the average of the surrounding pixels it finds the median.
# This is usually better at removing noise from an image than Gaus and averaging at low kernal sizes.

median = cv.medianBlur(img, 9) # Kernal size is now just an integer so if you put 3 openCV thinks its just (3,3)
cv.imshow('Median Blur', median)

# Bilateral Blurring: BEST BLURRING TECHNIQUE because of how it blurs. This applys bluring but keeps the edges in the image.
bilateral = cv.bilateralFilter(img,10,35,25 ) # (image, pixel diameter: bigger pixel diameter more blur, sigma color: so i higher sigma number the more colors will be 
                                        # considered in the image when blurred, space sigma: Larger sigma space means that pixels 
                                        # further away from the blur point will be considered in the blur of that square of windows)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)