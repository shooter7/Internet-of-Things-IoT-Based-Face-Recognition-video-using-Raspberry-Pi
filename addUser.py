import MySQLdb
import os
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import recognizer2 as rec

# Open database connection
db = MySQLdb.connect("localhost", "ahmed", "ahmed", "project")
# prepare a cursor object using cursor() method
cursor = db.cursor()

username = raw_input("insert your name(must be uniqe)")
sql = "insert into names(username) value('%s') ;" % username
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()
cursor.execute('select ID from names where username="%s";' % username)
# Fetch a single row using fetchone() method.
label = cursor.fetchone()
fasesDir = "/home/pi/Desktop/faces/p" + str(label[0])
os.mkdir(fasesDir)

db.close()

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 5
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)
count = 1

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = np.asarray(frame.array)
    face, rect = rec.detect_face(image)
    if face is not None:
        cv2.imwrite(fasesDir+"/" + str(count) + ".jpg",image)
        count += 1

    if count == 5:
        break
        # show the frame
    rawCapture.truncate(0)
    cv2.imshow("Frame", image)
rec.train()

