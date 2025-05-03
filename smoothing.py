import cv2 as cv

img = cv.imread('Resources/Photos/lady.jpg')
cv.imshow('Lady', img)

#Averaging 
average = cv.blur(img, (7, 7)) #blurs the image
cv.imshow('Averaging', average)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (7, 7), 0) # inputs: img, kernel size, sigmaX which is the standard deviation in X direction
#blurs the image
cv.imshow('Gaussian Blur', gaussian) #each pixel is replaced by the average of its neighbors


# Median Blur
median = cv.medianBlur(img, 7) # blurs the image; inputs: img, kernel size
cv.imshow('Median Blur', median) #each pixel is replaced by the median of its neighbors

# Bilateral Blur: Most commonly used/effective
bilateral = cv.bilateralFilter(img, 15, 35, 25) # blurs the image; inputs: img, d, sigmaColor, sigmaSpace
cv.imshow('Bilateral Blur', bilateral) #each pixel is replaced by the average of its neighbors, but only if they are similar in color
# The bilateral filter is a non-linear, edge-preserving, and noise-reducing smoothing filter
# It replaces the intensity of each pixel with a weighted average of intensity values from nearby pixels
# The weights are based on both the spatial distance and the intensity difference
# The result is a smoother image with preserved edges


cv.waitKey(0)
cv.destroyAllWindows()