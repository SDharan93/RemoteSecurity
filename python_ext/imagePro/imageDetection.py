from opencv import imageControl

class imageDetection(object):

    motionDetected = False

    def __init__(self):

    def detectMotion(self, thresholdImage):
        tempImage = thresholdImage.copy()

