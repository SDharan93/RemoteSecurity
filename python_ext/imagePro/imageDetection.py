from opencv import imageControl

class imageDetection(object):

    motionDetected = False
    control = 0
    thresholdImage = 0
    differenceImage = 0

    def __init__(self):
        self.control = imageControl()

    def thresholdImage(self):
        self.control.threshold()
        self.thresholdImage = self.control.getThresholdImage().copy()

    def detectMotion(self, thresholdImage):
        self.motionDetected = False
        self.control.findContours(self)
        return self.control.isMotion()
