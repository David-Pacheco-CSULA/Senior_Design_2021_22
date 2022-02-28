#TODAY'S LESSON: Reading/Displaying videos and images

#--------Reading Images---------
# import cv2 as cv                       # Allows for OpenCV functions to be used
# img = cv.imread('C:\\Users\\david\\Desktop\\CSULA 2021 Fall\\Senior Design\\Python\\Photos\\Galio.PNG')   # Reads the image and stores it in variable 'img'
# cv.imshow('Sloth Poster Bitch', img)   # Displays the Image
# cv.waitKey(0)                          # Used to keep the image from disappearing

#-------Reading Videos----------
import cv2 as cv                         # Allows for OpenCV functions to be used

capture = cv.VideoCapture('C:\\Users\\david\\Pictures\\Camera Roll\\OpenCV Video Lesson 1 Reading Videos.mp4') # Captures the video and stores it in variable 'capture'

while True:                                 # While loop
    isTrue, frame = capture.read()          # A boolean statement that returns true if the frame was sucessfully read
                                            # capture.read() reads the video within the variable 'capture' frame by frame

    cv.imshow('Me', frame)                  # Shows the frames in a window

    if cv.waitKey(20) & 0xFF==ord('d'):     # If Statement: if you press 'd' on the keyboard
        break                               # Breaks out of a loop

capture.release()                           # Unlocks sections of code to be used by other sections needing locks
cv.destroyAllWindows()                      # Removes all windows that were opened 
                             