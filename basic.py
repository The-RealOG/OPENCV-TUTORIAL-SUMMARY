import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
# cv.imshow('Cat', img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

# Blurring an image
blur = cv.GaussianBlur(img, (11, 11), cv.BORDER_DEFAULT) # img, kernel size (has to be an odd tuple), border type
# cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 150) # img, lower threshold, upper threshold
# cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=3) # img, kernel size, iterations
# cv.imshow('Dilated', dilated)

# Eroding the image
eroded = cv.erode(dilated, (7, 7), iterations=3) # img, kernel size, iterations
# cv.imshow('Eroded', eroded)

# Resizing the image
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC) # img, size, interpolation
#INTER_AREA = resampling using pixel area relation
#INTER_CUBIC = bicubic interpolation over 4x4 pixel neighborhood
#INTER_LINEAR = bilinear interpolation (default)
# cv.imshow('Resized', resized)

# Cropping the image
cropped = img[50:200, 200:400] # img[y1:y2, x1:x2]
cv.imshow('Cropped', cropped)

cv.waitKey(0) # Wait for a key press to close the image window
cv.destroyAllWindows() #closes all image/video windows
