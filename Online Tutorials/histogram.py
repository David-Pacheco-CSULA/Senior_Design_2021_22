from PIL.Image import NONE
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('C:\\Users\\david\\Desktop\\CSULA 2021 Fall\\Senior Design\\Python\\Photos\\Galio.PNG')
cv.imshow('Galio', img)

#TODAY'S LESSON: Histograms
#Hisograms: allow you to visualize/measured the distribution of pixel intensities in an image (Colored/Gray Scale)

blank = np.zeros(img.shape[:2], dtype='uint8')


# Colored First

mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img, img, mask=mask) #Pass the 'gray' image and now cut out a 'circle' sized hole in the image
cv.imshow('Mask', masked)


# Colored Histogram 
plt.figure()  # Creating a figure (later commands are the specification of the figure)
plt.title('Colored Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colors = ('b', 'g', 'r')  # Defining a tuble of tuple elements which in this case are colors 
for i,col in enumerate(colors):   # For loop: repeats once for every color channel 
                                  # 'in enumerate': Numbers a sequence/list in this case a list of colors 
                                  # 'col': contains the colors and 'i' counts up from zero
    hist = cv.calcHist([img], [i], mask, [256], [0,256]) # Note we did calcute the masked version of the image
                                                         # Note we do have a colored image so the number of channels is not zero now it is '[i]'
    plt.plot(hist, color=col) # Note: 'color=col' gives a color to the histogram line
    plt.xlim([0,256])

plt.show()


# Grayscale Second

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
# cv.imshow('Circle', circle)

# mask = cv.bitwise_and(gray, gray, mask=circle) #Pass the 'gray' image and now cut out a 'circle' sized hole in the image
# cv.imshow('Mask', mask)


# # GrayScale Histogram
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])  # This will create a histogram (Note: '[]' means its a list)
#                                                             # ([image], [# of color Channels], mask, [# number of bins will talk about later] , [range of pixel values] ) (Note: In this case, 'None' means no mask needed)
#                                                             # bins: refers to the intervals of pixel intensities
#                                                             # Note you are allowed to use a mask on the image before making a histogram. 

# plt.figure()  # Creating a figure (later commands are the specification of the figure)
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist) # Will show the number of pixels at every bin or interval of intensity 
#                     # Where the peak is will depend on the colors most promenint in the image the whiter it is the more it will lean to 255
# plt.xlim([0,250])
# plt.show()


cv.waitKey(0)
