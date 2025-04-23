import cv2 as cv

#Reads the image from the specified path
img = cv.imread('Resources/Photos/cat_large.jpg')
#Displays the image
#cv.imshow('Cat', img)

#Reading videos from your webcam
# 0 is the default camera
capture = cv.VideoCapture(0)

capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue, frame = capture.read() #bool and frame
    #Displays the video frame by frame
    cv.imshow('Video', frame)

    #Press 'd' to stop the video
    if cv.waitKey(20) & 0xFF == ord('d'):
        break


capture.release()
cv.destroyAllWindows()