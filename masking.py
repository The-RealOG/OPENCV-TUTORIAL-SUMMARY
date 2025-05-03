import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/lady.jpg')
cv.imshow('Lady', img)

blank = np.zeros(img.shape[:2], dtype='uint8') # creates a blank image
cv.imshow('Blank', blank) # displays the blank image

# Masking: creating a region of interest (ROI) in the image
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1) # creates a circular mask
#cv.imshow('Mask', mask) # displays the mask

masked = cv.bitwise_and(img, img, mask=mask) # applies the mask to the image
cv.imshow('Masked Image', masked) # displays the masked image


cv.waitKey(0)
cv.destroyAllWindows()

