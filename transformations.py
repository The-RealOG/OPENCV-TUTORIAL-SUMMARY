import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/lady.jpg')

cv.imshow('Lady', img)

def translate(img, x, y): # img, x translation, y translation
    transMat = np.float32([[1, 0, x], [0, 1, y]]) # translation matrix
    dimensions = (img.shape[1], img.shape[0]) # width, height
    return cv.warpAffine(img, transMat, dimensions) # img, translation matrix, dimensions

# -x --> Left
# -y --> Up
# +x --> Right
# +y --> Down

translated = translate(img, 100, 100) # img, x translation, y translation
# cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None): # img, angle, rotation point
    (height , width) = img.shape[:2] # height, width
    if rotPoint is None:
        rotPoint = (width // 2, height // 2) # center of the image

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # rotation matrix: rotation point, angle, scale
    dimensions = (width, height) # width, height
    return cv.warpAffine(img, rotMat, dimensions) # img, rotation matrix, dimensions # cv.warpAffine() applies an affine transformation to the image
   
rotated = rotate(img, 45) # img, angle: + angle --> clockwise, - angle --> counterclockwise
cv.imshow('Rotated', rotated)



cv.waitKey(0)
cv.destroyAllWindows()