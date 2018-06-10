from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import recognizer2 as rec
import database as db
import max

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)

count=0
arrayOfFace=[0,0,0]
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = np.asarray(frame.array)

    face, rect = rec.detect_face(image)
    if face is not None:
        label = rec.predict(image)
        arrayOfFace[count]=label
        count+=1
       # print label
        if (count>=3):
            break

    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

db.getDBInfo(max.maxRepeating(arrayOfFace,len(arrayOfFace)))
db.close()
