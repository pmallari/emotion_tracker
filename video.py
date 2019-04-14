import numpy as np
import face_recognition
import cv2 as cv 

# Set webcam as the video capture
video_capture = cv.VideoCapture(0)

while True:
        # Retrieve image from webcam
        ret, frame = video_capture.read()

        # Resize image to 1/4 to increase speed of locating faces
        img_scale = 3
        image = cv.resize(frame, (0,0), fx=1/img_scale, fy=1/img_scale)

        # Find face bounding boxes
        face_locations      = face_recognition.face_locations(image)
        face_landmarks_list = face_recognition.face_landmarks(image)

        # Create bounding boxes for each face detected
        for (top, right, bottom, left) in face_locations:

                # Rescale bounding boxes to original size
                top     *= img_scale
                right   *= img_scale
                bottom  *= img_scale
                left    *= img_scale

                width       = right - left
                height      = top - bottom
                scale_perc  = 0.1

                delta_w     = width * scale_perc
                delta_h     = height * scale_perc

                top_new     = int(top + delta_h)
                right_new   = int(right + delta_w)
                bottom_new  = int(bottom - delta_h)
                left_new    = int(left - delta_w)
                
                # Draw bounding boxes
                cv.rectangle(frame,(left_new, top_new),(right_new, bottom_new),(255,0,0),2)

        for face_landmarks in face_landmarks_list:
                for eyes in ['left_eye', 'right_eye']:
                        eye = face_landmarks[eyes]
                        for point_idx in range(len(eye)-1):
                                pt_1_x  = eye[point_idx][0] * img_scale
                                pt_1_y  = eye[point_idx][1] * img_scale
                                pt_2_x  = eye[point_idx+1][0] * img_scale
                                pt_2_y  = eye[point_idx+1][1] * img_scale
                                cv.line(frame, (pt_1_x, pt_1_y), (pt_2_x, pt_2_y), (0,255,0))
                        cv.line(frame, (eye[0][0]*img_scale, eye[0][1]*img_scale), (eye[-1][0]*img_scale, eye[-1][1]*img_scale), (0,255,0))

        # Display image
        cv.imshow('img',frame)
        
        # Define breaking parameter
        if cv.waitKey(1) & 0xFF == ord('q'):
                break


video_capture.release()
cv.destroyAllWindows()