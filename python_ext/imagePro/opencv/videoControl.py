import numpy as np
import cv2

class videoControl(object):

    cap = 0
    frame1 = 0
    greyFrame1 = 0

    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def read(self):
        ret, self.frame1 = self.cap.read()
        self.greyFrame1 = cv2.cvtColor(self.frame1, cv2.COLOR_BGR2GRAY)

    def showGreyImage(self):
        cv2.imshow('grey video feed', self.greyFrame1)

    def captureCam(self):
        cap = cv2.VideoCapture(0)
        return cap

    def showGreyFeed(self):
        cv2.imshow('grey video feed', self.greyFrame1)

    def release(self):
        self.cap.release()

    def input(self):
        return cv2.waitKey(10) & 0xFF
