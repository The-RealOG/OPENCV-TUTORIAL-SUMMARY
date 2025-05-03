import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/lady.jpg')
cv.imshow('Lady', img)
blank = np.zeros(img.shape[:2], dtype='uint8') 

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1) # creates a mask (a circle in the center of the image)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # converts the image to grayscale  
cv.imshow('Gray', gray)  

mask = cv.bitwise_and(gray, gray, mask=circle) # applies the mask to the image (only the area inside the circle will be visible)

cv.imshow('Mask', mask)

# To show the histogram distribution of pixels in the image, we can use the cv2.calcHist() function. This function takes the following parameters:
gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256]) # calculates the histogram of the grayscale image

plt.figure()
plt.title('Grayscale Histogram')

plt.xlabel('Bins') # bins refers to the number of pixel values (0-255)
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256]) # sets the x-axis limits
plt.show() #displays the histogram image



cv.waitKey(0)
cv.destroyAllWindows()
