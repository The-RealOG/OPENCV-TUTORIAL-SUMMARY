import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/lady.jpg')
cv.imshow('Lady', img)


cv.waitKey(0)
cv.destroyAllWIndows()
