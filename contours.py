import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/lady.jpg')
cv.imshow('Lady', img)

blank = np.zeros(img.shape, dtype='uint8') #creates a blank image
cv.imshow('Blank', blank)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blurring the image
# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT) # img, kernel size (has to be an odd tuple), border type
# cv.imshow('Blur', blur)

# canny = cv.Canny(blur, 125, 175) # img, lower threshold, upper threshold
# cv.imshow('Canny Edges', canny)

# contours, heirarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) # img, mode, method
# contours: list of contours found in the image
# heirarchy: information about the image topology

# print(f"{len(contours)} contours found!")

#thresholding looks at an image and converts it to a binary image

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) # img, threshold value, max value, threshold type

cv.imshow('Thresholded', thresh) # think back to threshold feature for image processing with the Jiang lab and the Fiji software plugin

contours, heirarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) # img, mode, method
print(f"{len(contours)} contours found!")

cv.drawContours(blank, contours, -1, (0, 0, 255), 1) # img, contours, contour index (-1 for all), color, thickness
cv.imshow('Contours Drawn', blank) # img, contours, contour index (-1 for all), color, thickness



cv.waitKey(0) # Wait for a key press to close the image window
cv.destroyAllWindows() #closes all image/video windows