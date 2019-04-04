import numpy as np
import face_recognition
import cv2 as cv 

# Set webcam as the video capture
video_capture = cv.VideoCapture(0)

while True:
        # Retrieve image from webcam
        ret, frame = video_capture.read()

        # Resize image to 1/4 to increase speed of locating faces
        image = cv.resize(frame, (0,0), fx=0.25, fy=0.25)

        # Find face bounding boxes
        face_locations = face_recognition.face_locations(image)

        # Create bounding boxes for each face detected
        for (top, right, bottom, left) in face_locations:

                # Rescale bounding boxes to original size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw bounding boxes
                cv.rectangle(frame,(left, top),(right, bottom),(255,0,0),2)

        # Display image
        cv.imshow('img',frame)
        
        # Define breaking parameter
        if cv.waitKey(1) & 0xFF == ord('q'):
                break


video_capture.release()
cv.destroyAllWindows()