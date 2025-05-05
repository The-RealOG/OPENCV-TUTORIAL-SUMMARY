import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')

cv.imshow('park', img)




#thresholding is the binarization of an image i.e. converting an image to a binary image (black or white)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY', gray)

#Types
#Simple thresholding 
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY) #compares each pixel value to the threshold value and if its above the threshold value, it sets it to 255 otherwise it sets it to 0.

#cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)

#cv.imshow('Simple inverse threshold', thresh_inv)

#Adaptive thresholding
#allows the system decide the optimum threshold value
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)

cv.imshow('Adaptive Thresholding', adaptive_thresh)



cv.waitKey(0)
cv.destroyAllWindows()