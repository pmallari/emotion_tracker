import numpy as np
import cv2
import os
import time
import glob
import face_recognition
from tqdm import tqdm

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')

emotion = {"01": "neutral",
           "02": "calm",
           "03": "happy",
           "04": "sad",
           "05": "angry",
           "06": "fearful",
           "07": "disgust",
           "08": "surprised"}

vocal   = {"01": "speech",
           "02": "song"}

img_set = ['train', 'test', 'valid']

for emote in emotion:
    for folder in img_set:
        path = f"./data/images/{folder}/{emote}"
        if not os.path.exists(path):
            os.mkdir(path)

for root, dirs, files in os.walk('data/Video/'):
    print(f"Root file: {root}")
    for name in tqdm(files):
        if name.endswith(".mp4"):

            profile, _  = name.split(".")
            profile     = profile.split("-")

            video_link  = os.path.join(root, name)
            cap         = cv2.VideoCapture(video_link)

            frame_count = 1
            img_count   = 1

            while(cap.isOpened()):
                ret, frame  = cap.read()

                faces       = face_recognition.face_locations(frame)

                if img_count % 5 == 3:
                    image_set   = "valid"
                elif img_count % 5 == 4:
                    image_set   = "test"
                else:
                    image_set   = "train"
                
                for (x, y, w , h) in faces:
                    crop_img    = frame[y:y+h, x:x+w, :]

                img_emotion     = emotion[profile[2]]

                cv2.imshow(emotion[profile[2]], crop_img)
                cv2.imwrite(f"./data/images/{image_set}/{img_emotion}/{'-'.join(profile)}_{img_count}.jpg", crop_img)

                img_count += 1

            else:
                frame_count += 1

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            if frame is None:
                break

        cap.release()
        cv2.destroyAllWindows()       