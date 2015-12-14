import numpy as np
import cv2

cap = cv2.VideoCapture(-1)
if cap:
    while(True):
        #capture frame by fraame
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
