import numpy as np
import cv2

class imageProc:

    capture = 0
    frame1 = 0
    frame2 = 0
    greyImage1 = 0
    greyImage2 = 0

    def __init__():
        self.cap = cv2.VideoCapture(0)

    def readCamera(self, camera):
        frame1 = cap.read()
        greyImage1 = cv2.imshow(frame1, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame 1', greyImage1)
