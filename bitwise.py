import cv2 as cv
import numpy as np

blank = np.zeros((400, 400, 3), dtype='uint8') # creates a blank image

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, thickness=-1) # creates a rectangle
# blank.copy() creates a copy of the blank image

circle = cv.circle(blank.copy(), (200, 200), 200, 255, thickness=-1) # creates a circle

# cv.imshow('Rectangle', rectangle) # displays the rectangle
# cv.imshow('Circle', circle) # displays the circle

# Bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle) # performs a bitwise AND operation (overlaps the two shapes and returns the common area/intersection)

#cv.imshow('Bitwise AND', bitwise_and) # displays the result

# Bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle) # performs a bitwise OR operation (returns all areas of both shapes/basically a union of the two shapes)
#cv.imshow('Bitwise OR', bitwise_or) # displays the result

# Bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle) # performs a bitwise XOR operation (returns all areas of both shapes except the common area)
#cv.imshow('Bitwise XOR', bitwise_xor) # displays the result

# Bitwise NOT
bitwise_not_rectangle = cv.bitwise_not(rectangle) # performs a bitwise NOT operation (inverts the color on the rectangle)
bitwise_not_circle = cv.bitwise_not(circle) # performs a bitwise NOT operation (inverts the color on circle)
cv.imshow('Bitwise NOT Rectangle', bitwise_not_rectangle) # displays the result
cv.imshow('Bitwise NOT Circle', bitwise_not_circle) # displays the result

cv.waitKey(0)
cv.destroyAllWindows()