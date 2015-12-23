from opencv import videoControl

class videoFeed(object):

    capture = 0
    frame1 = 0
    frame2 = 0
    greyImage1 = 0
    greyImage2 = 0
    ret = False

    def __init__(self):
        self.capture = videoControl()

    def snapShot(self):
        self.frame1 = self.capture.getFrame1()
        self.frame2 = self.capture.getFrame2()
        self.greyImage1 = self.capture.getGreyFrame1()
        self.greyImage2 = self.capture.getGreyFrame2()

    def getFrame1(self):
        return self.frame1

    def getFrame2(self):
        return self.frame2

    def getGreyFrame1(self):
        return self.greyImage1

    def getGreyFrame2(self):
        return self.greyImage2

    def readCamera(self):
        self.capture.read()
        self.snapShot()

    def showFrame1(self):
        self.capture.showVideoFeed1()

    def showFrame2(self):
        self.capture.showVideoFeed2()

    def close(self):
        self.capture.release()

    def inputKey(self):
        return self.capture.input()
