import numpy as np 
import cv2 as cv 

# Import haarcascade face detector
face_cascade = cv.CascadeClassifier('cv_xml/haarcascade_frontalface_default.xml')
eye_cascade  = cv.CascadeClassifier('cv_xml/haarcascade_eye.xml')

# Set as webcam
video_capture = cv.VideoCapture(0)

while True:
        ret, frame = video_capture.read()

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        eyes  = eye_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
                cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        for (x,y,w,h) in eyes:
                cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        cv.imshow('img',frame)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
                break

video_capture.release()
cv.destroyAllWindows()