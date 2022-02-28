import cv2 as cv  # Allows for OpenCV functions to be used
import numpy as np # OpenCV Package 

blank = np.zeros((500,500, 3), dtype='uint8')  # Makes a blank image ('uint8' is the data type of an image & '(500,500, 3)' '(height, width, # of color channels)' (pixels))
cv.imshow('Blank', blank)                      # Displays the blank image we made 

#TODAY'S LESSON: Drawing shapes on a blank image

# 1. Paint the image a certain color 

blank[200:300, 300:400] = 0,255,0    # 'blank[:]' references all the pixels + ' 0,255,0' => Green + '0,0,255' => Red + '255, 255, 255' => White
                                     # 'blank[#:#,#:#]' references a square of pixels to color (Height Pixals, Width Pixals)

cv.imshow('Green', blank)            # Displays the blank green image we made 

# 2. Draw a Rectangle 

# -------------------------------cv.rectangle(IMAGE, PT1, PT2, COLOR, Border THICKNESS)--------------------------------
# Takes the image 'blank' to draw a rectangle over it, '(0,0)' Pt1 (Top Left Pt) (horizontal move, vertical move), 
# '(250,250)' Pt2 (Bot Right Pt), '(0,255,0)' => Green, 'thickness = 2' Refers to Border thickness 

# (Note: 'thickness = cv.FILLED' or 'thickness = -1' will give you a filled rectangle instead of just the border of a rectangle)
# (Note: You can switch '(250, 250)' Pt2 with '(blank.shape[1]//2, blank.shape[0]//2)' to refer to half the image's pixel value)

cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness = cv.FILLED) 
cv.imshow('Rectangle', blank)        # Displays the rectangle we made on the image 'Blank'
                                                     
# 3. Draw a circle

#------------------------------cv.circle(IMAGE, Center pt, Radius, COLOR, Border THICKNESS)----------------------------
# Takes the image 'blank' to draw a circle over it, '(250,250)' Pt1 (Center) (horizontal move, vertical move), 
# '40' radius, '(0,255,0)' => Green, 'thickness = 2' Refers to Border thickness 

# (Note: 'thickness = cv.FILLED' or 'thickness = -1' will give you a filled circle instead of just the border of a circle)
# (Note: You can switch '(250, 250)' the radius with '(blank.shape[1]//2, blank.shape[0]//2)' to refer to half the image's pixel value)

cv.circle(blank,(350, 250), 40, (0,0,255), thickness = 3) 
cv.imshow('Circle', blank)           # Displays the circle we made on the image 'Blank'

# 4. Draw a line

#-----------------------------cv.line(IMAGE, Starting Pt, Ending Pt, COLOR, Line THICKNESS)-------------------------
# Takes the image 'blank' to draw a line over it, '(0,0)' Stating Pt (horizontal move, vertical move), 
# '(250,250)' Ending Pt, '(255,255,255)' => White, 'thickness = 2' Refers to line thickness 

# (Note: You can switch '(250, 250)' the Ending Pt with '(blank.shape[1]//2, blank.shape[0]//2)' to refer to half the image's pixel value)

cv.line(blank, (0,0), (250, 250), (255, 255, 255), thickness = 3)
cv.imshow('Line', blank)             # Displays the line we made on the image 'Blank'

# 5. Write Text

#--------------------------cvputText(IMAGE, 'TEXT', Starting Point, Font, Font_Scale, COLOR, THICKNESS)-----------------------------------
# Takes the image 'blank' to draw text over it, ''Hello'' is the text, '(255,255)' Where you want the text (Hori, Vert),
# 'cv.FONT_HERSHEY_COMPLEX' is the font, '1.0' is the font size, '(0,255,0)' is green, '2' Font Thickness 

# (Note: You can switch '(250, 250)' the Text Starting point with '(blank.shape[1]//2, blank.shape[0]//2)' to refer to half the image's pixel value)

cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)             # Displays the TEXT we made on the image 'Blank'

cv.waitKey(0)                        # Used to keep the image from disappearing