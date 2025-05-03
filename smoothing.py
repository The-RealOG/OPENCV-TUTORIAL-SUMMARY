import cv2 as cv

img = cv.imread('Resources/Photos/lady.jpg')
cv.imshow('Lady', img)

#Averaging 
average = cv.blur(img, (7, 7)) #blurs the image
cv.imshow('Averaging', average)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (7, 7), 0) #blurs the image
cv.imshow('Gaussian Blur', gaussian) #each pixel is replaced by the average of its neighbors
cv.waitKey(0)
cv.destroyAllWindows()