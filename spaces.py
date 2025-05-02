import cv2 as cv

img = cv.imread('Resources/Photos/lady.jpg')
cv.imshow('Lady', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)



cv.waitKey(0) # Wait for a key press to close the image window
cv.destroyAllWindows() #closes all image/video windows