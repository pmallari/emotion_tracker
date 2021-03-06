import numpy as np
import cv2
import os
import time
import glob
import face_recognition
from tqdm import tqdm

"""
Define emotion dictionary to map file name pattern to emotion
"""

emotion = {"01": "neutral",
           "02": "calm",
           "03": "happy",
           "04": "sad",
           "05": "angry",
           "06": "fearful",
           "07": "disgust",
           "08": "surprised"}

"""
Define image set where image will be saved
"""

img_set = ['train', 'test', 'valid']


"""
Check if folders for image data exists. Create folder if it doesn't exist.
"""

for emote in emotion:
    for folder in img_set:
        path = f"./data/images/{folder}/{emote}"
        if not os.path.exists(path):
            os.mkdir(path)

"""
Browse through each video file, detect faces, and crop face.
"""
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
                
                for (top, right, bottom, left) in faces:

                    width       = right - left
                    height      = top - bottom
                    scale_perc  = 0.1

                    delta_w     = width * scale_perc
                    delta_h     = height * scale_perc

                    top_new     = top - delta_h
                    right_new   = right + delta_w
                    bottom_new  = bottom + delta_h
                    left_new    = left + delta_w

                    crop_img    = frame[top_new:bottom_new, left_new:right_new, :]

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