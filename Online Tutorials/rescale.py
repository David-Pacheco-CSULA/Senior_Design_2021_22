import cv2 as cv  # Allows for OpenCV functions to be used

#TODAY'S LESSON: Rescaling/Resizing images


#-----------------------------START: NEW RESCALING CODE---------------------------------------

# FOR IMAGES, VIDEOS, LIVE VIDEOS
def rescaleFrame (frame, scale = 0.25):  # Function takes in a frame and rescales it by the scale value (CURRENTLY SET TO: 25%)
    width = int(frame.shape[1] * scale)  # 'frame.shape[1]' returns the width of the image & int(frame.shape[1]) makes the width an integer
    height = int(frame.shape[0] * scale) # 'frame.shape[0]' returns the height of the image & int(frame.shape[0]) makes the height an integer
    dimensions = (width,height)          # varible storing width and height 

    return cv.resize(frame, dimensions,interpolation=cv.INTER_AREA) # We will talk about this later in depth but for now just know
                                                                    # it resizes the frame to a specific dimension
#------------------------------END: NEW RESCALING CODE-------------------------------------------


#-----------------------------START: 2nd RESCALING CODE----------------------------------------

# FOR LIVE VIDEOS ONLY 
def changeRes(width, height):   # Function that also rescales Live video; Width & Height referes to pixel size
    capture.set(3,width)        # 3 References the width; capture => the name of the video capture object  
    capture.set(4,height)       # 4 References the height; capture => the name of the video capture object
                                # Video Capture Object: capture = cv.VideoCapture('VIDEO PATH')

#------------------------------END: 2nd RESCALING CODE----------------------------------------


# --------------------------- START: FROM THE read.py CODE ------------------------------------

img = cv.imread('C:\\Users\\david\\Desktop\\CSULA 2021 Fall\\Senior Design\\Python\\Photos\\Galio.PNG') # Reads the image and stores it in variable 'img'
cv.imshow('Sloth Poster', img)   # Displays the Image

resized_image = rescaleFrame(img)  # NEW: Called the rescaleFrame() function and passes img
cv.imshow('Image', resized_image)  # NEW: Displays the RESIZED Image

#-----------------------------END: FROM THE read.py code-------------------------------------


# --------------------------- START: FROM THE read.py CODE ------------------------------------

#Reading Videos
capture = cv.VideoCapture('C:\\Users\\david\\Pictures\\Camera Roll\\OpenCV Video Lesson 1 Reading Videos.mp4') # Captures the video and stores it in variable 'capture'

while True:                                 # While loop
    isTrue, frame = capture.read()          # A boolean statement that returns true if the frame was sucessfully read
                                            # capture.read() reads the video within the variable 'capture' frame by frame

    frame_resized = rescaleFrame(frame)     # NEW: Calling the function
    
    cv.imshow('Video Normal', frame)                  # Shows the frames in a window
    cv.imshow('Video Resized', frame_resized)         # NEW: Shows the resized frames in the window

    if cv.waitKey(20) & 0xFF==ord('d'):     # If Statement: if you press 'd' on the keyboard
        break                               # Breaks out of a loop

capture.release()                           # Unlocks sections of code to be used by other sections needing locks
cv.destroyAllWindows()                      # Removes all windows that were opened 

#-----------------------------END: FROM THE read.py code-------------------------------------