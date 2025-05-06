import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Cats', img)

#from a programming perspective, think of edges and gradients as similar in this context

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


#Laplacian Edges/gradient
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

#cv.imshow('Lap image', lap)


#Sobel gradient magnitude representation
#computes gradients in 2 directions: x and y
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

# cv.imshow('Sobel_X', sobelx)
# cv.imshow('Sobel_Y', sobely)

combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined Sobel', combined_sobel)


cv.waitKey(0)
cv.destroyAllWindows()