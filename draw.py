import numpy as np
import cv2 as cv

blank = np.zeros((500, 500, 3), dtype='uint8') #creates a blank image
# cv.imshow('Blank', blank)


img = cv.imread('Resources/Photos/cat.jpg')
# cv.imshow('Cat', img)

# 1. Paint the image a color
# blank[:] = 0, 255, 0 # BGR
# cv.imshow('Green', blank)

# # 2. Draw a rectangle
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2) # BGR


# # 3. Draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=3) # BGR
# #cv.imshow('Circle', blank)

# # 4. Draw a line
# cv.line(blank, (0, 0), (250, 250), (255, 255, 255), thickness=3) # BGR #image name, position tuple, color, image thickness
# #cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello World', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2) # BGR
cv.imshow('Text', blank)

cv.waitKey(0) # Wait for a key press to close the image window
cv.destroyAllWindows() #closes all image/video windows


