from opencv import imageControl

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

    def thresholdCalc(self):
        self.control.threshold()
        self.thresholdImage = self.control.getThresholdImage().copy()

    def showThresholdImage(self):
        self.control.showThresholdImage()

    def showDifferenceImage(self):
        self.control.showDifferenceImage()

    def detectMotion(self):
        self.motionDetected = False
        self.control.findContours()
        return self.control.isMotion()
