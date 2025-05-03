import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/lady.jpg')
#cv.imshow('Lady', img)

# plt.imshow(img) # Displays the image using matplotlib
# #plt.axis('off') # Hides the axis
# plt.show() # Displays the image

# you can't convert grayscale to HSV directly; you have to convert it to BGR first and then to HSV
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV (Hue Saturation Value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#cv.imshow('HSV', hsv)

# BGR to LAB (Luminance A and B channels)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
#cv.imshow('LAB', lab)

# BGR to RGB (Red Green Blue)
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#cv.imshow('RGB', rgb)

# plt.imshow(rgb) # Displays the image using matplotlib
# plt.show() # Displays the image

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR', hsv_bgr)

cv.waitKey(0) # Wait for a key press to close the image window
cv.destroyAllWindows() #closes all image/video windows