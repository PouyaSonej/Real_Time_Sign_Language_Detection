import cv2 as cv
import os 
import time

image_path = 'captured_images'

labels = ['Hello', 'Welcome', 'To', 'My', 'Website']

number_imgs = 20

for label in labels:
    os.makedirs(os.path.join(image_path, label), exist_ok=True)
    cap = cv.VideoCapture(0)
    print(label)
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imgname = os.path.join(image_path, label, f"{label}_{imgnum}.jpg")
        cv.imwrite(imgname, frame)
        cv.imshow('frame', frame)
        time.sleep(2)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()