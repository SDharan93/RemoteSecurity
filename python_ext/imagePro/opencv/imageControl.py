import numpy as np
import cv2

class imageControl(object):

    #image properities
    contours = 0
    hierarchy = 0
    contourSize = 0
    motionDetected = False
    BLUR_SIZE = 10
    SENSITIVITY_VALUE = 40

    #frames needed for motion detection
    image1 = 0
    image2 = 0
    differenceImage = 0
    thresholdImage = 0

    def setImage1(self, image1):
        self.image1 = image1.copy()

    def getImage1(self):
        return self.image1

    def showImage1(self):
        cv2.imshow('image 1 video feed 1', self.image1)

    def setImage2(self, image2):
        self.image2 = image2.copy()

    def getImage2(self):
        return self.image2

    def showImage2(self):
        cv2.imshow('video feed 2', self.image2)

    def difference(self):
        self.differenceImage = cv2.absdiff(self.image1, self.image2).copy()

    def getDifferenceImage(self):
        return self.differenceImage

    def showDifferenceImage(self):
        cv2.imshow('Difference Image Feed', self.differenceImage)

    def threshold(self):
        self.difference()
        self.calcThresholdImage(self.differenceImage)
        self.blurImage()
        self.calcThresholdImage(self.thresholdImage)

    def getThresholdImage(self):
        return self.thresholdImage

    def showThresholdImage(self):
        cv2.imshow('threshold feed', self.thresholdImage)

    def findContours(self):
        temp = self.thresholdImage.copy()
        self.contours, self.heirarchy = cv2.findContours(temp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        #index out of bound checks
        if len(self.contours) > 0:
            self.contourSize = len(self.contours[0])
        else:
            self.contourSize = 0

    def calcThresholdImage(self, image):
        ret, self.thresholdImage = cv2.threshold(image, self.SENSITIVITY_VALUE, 255, cv2.THRESH_BINARY)

    def blurImage(self):
        self.thresholdImage = cv2.blur(self.thresholdImage, (self.BLUR_SIZE, self.BLUR_SIZE))

    def isMotion(self):
        if self.contourSize > 0:
            self.motionDetected = True
        else:
            self.motionDetected = False
        return self.motionDetected

    def getMotionDetected(self):
        return self.motionDetected
