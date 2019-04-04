import numpy as np
import face_recognition
import cv2 as cv 

# Import haarcascade face detector
face_cascade = cv.CascadeClassifier('cv_xml/haarcascade_frontalface_default.xml')
eye_cascade  = cv.CascadeClassifier('cv_xml/haarcascade_eye.xml')

# Set as webcam
video_capture = cv.VideoCapture(0)

while True:
        ret, frame = video_capture.read()

        image = cv.resize(frame, (0,0), fx=0.25, fy=0.25)

        face_locations = face_recognition.face_locations(image)

        for (top, right, bottom, left) in face_locations:
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4
                cv.rectangle(frame,(left, top),(right, bottom),(255,0,0),2)

        cv.imshow('img',frame)
        
        if cv.waitKey(1) & 0xFF == ord('q'):
                break

video_capture.release()
cv.destroyAllWindows()