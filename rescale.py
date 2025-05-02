import cv2 as cv

# img = cv.imread('Resources/Photos/cat_large.jpg')
# cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    # works for videos, images, and live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA) #resizes the image

def changeRes(width, height): # only works on live videos (something like a live webcam feed)
    # 0 is the default camera
    capture.set(3, width) # 3 = width
    capture.set(4, height) # 4 = height

#rescales the video

capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read() #bool and frame

    frame_resized = rescaleFrame(frame)
    #Displays the video frame by frame
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    #Press 'd' to stop the video
    if cv.waitKey(20) & 0xFF == ord('d'):
        break


capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
#It's generally best practice to downscale images to a smaller size for processing. This is because the larger the image, the more pixels there are to process. This can slow down processing time and increase memory usage