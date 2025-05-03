import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/lady.jpg')
#cv.imshow('Lady', img)


blank = np.zeros(img.shape[:2], dtype='uint8') #creates a blank image
b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank]) #merging the images
green = cv.merge([blank, g, blank]) #merging the images
red = cv.merge([blank, blank, r]) #merging the images

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)
# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

# print(img.shape)

merged = cv.merge([b, g, r]) #merging the images
#cv.imshow('Merged Image', merged)


cv.waitKey(0)
# print(b.shape) #regions where the images appear whiter would be due to the fact that the pixel values are higher in those regions
# regions where the images appear darker would be due to the fact that the pixel values are lower in those regions
# print(g.shape)
# print(r.shape)


cv.destroyAllWindows()