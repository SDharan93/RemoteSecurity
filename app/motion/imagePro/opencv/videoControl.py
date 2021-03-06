import numpy as np
import cv2

#low level class for controlling camera
class videoControl(object):

    cap = 0
    frame1 = 0
    frame2 = 0
    greyFrame1 = 0
    greyFrame2 = 0

    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    #reads next two frames and stores values + grey frames
    def read(self):
        ret, self.frame1 = self.cap.read()
        self.greyFrame1 = cv2.cvtColor(self.frame1, cv2.COLOR_BGR2GRAY)
        ret, self.frame2 = self.cap.read()
        self.greyFrame2 = cv2.cvtColor(self.frame2, cv2.COLOR_BGR2GRAY)

    def getFrame1(self):
        return self.frame1

    def getFrame2(self):
        return self.frame2

    def getGreyFrame1(self):
        return self.greyFrame1

    def getGreyFrame2(self):
        return self.greyFrame2

    def showGreyFeed1(self):
        cv2.imshow('grey video feed 1', self.greyFrame1)

    def showGreyFeed2(self):
        cv2.imshow('grey video feed 2', self.greyFrame2)

    def captureCam(self):
        cap = cv2.VideoCapture(0)
        return cap

    def showVideoFeed1(self):
        cv2.imshow('Video Feed 1', self.frame1)

    def showVideoFeed2(self):
        cv2.imshow('Video Feed 2', self.frame2)

    #destorys all windows
    def destoryAll(self):
        cv2.destroyAllWindows()

    #releases camera from program
    def release(self):
        self.cap.release()

    #gets keyboard input from user
    def input(self):
        return cv2.waitKey(10)
