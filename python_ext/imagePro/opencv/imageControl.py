import numpy as np
import cv2

class imageControl(object):

    contours = 0
    hierarchy = 0
    contourSize = 0
    motionDetected = False
    image1 = 0
    image2 = 0
    differenceImage = 0
    thresholdImage = 0

    def setImage1(self, image1):
        self.image1 = image1

    def getImage1(self):
        return self.image1

    def setImage2(self, image2):
        self.image2 = image2

    def getImage2(self):
        return self.image2

    def difference(self):
        self.differenceImage = cv2.absdiff(self.image1, self.image2)

    def getDifferenceImage(self):
        return self.differenceImage

    def threshold(self):
        difference()
        ret, self.thresholdImage = cv2.threshold(self.differenceImage, 127, 255, THRESH_BINARY)

    def getThresholdImage(self):
        return self.thresholdImage

    def findContours(self, thresholdImage):
        self.contours, self.heirarchy = cv2.findContours(self.thresholdImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.contourSize = len(self.contours[0])

    def isMotion(self):
        if len(self.contourSize) > 0:
            self.motionDetected = True
        else:
            motionDetected = False
        return self.motionDetected

    def getMotionDetected(self):
        return self.motionDetected
