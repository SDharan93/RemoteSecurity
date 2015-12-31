from opencv import imageControl

#This class controls the image processing portion of program
class imageDetection(object):

    motionDetected = False
    control = 0
    thresholdImage = 0
    differenceImage = 0

    def __init__(self):
        self.control = imageControl()

    def setImage1(self,image):
        self.control.setImage1(image)

    def showImage1(self):
        self.control.showImage1()

    def setImage2(self,image):
        self.control.setImage2(image)

    def showImage2(self):
        self.control.showImage2()

    #calculates the threshold image between the two frames
    def thresholdCalc(self):
        self.control.threshold()
        self.thresholdImage = self.control.getThresholdImage().copy()

    #shows the threshold image in a new window
    def showThresholdImage(self):
        self.control.showThresholdImage()

    #shows the difference image in a new window
    def showDifferenceImage(self):
        self.control.showDifferenceImage()

    #returns True or False depending if motion is found
    def detectMotion(self):
        self.motionDetected = False
        self.control.findContours()
        return self.control.isMotion()
