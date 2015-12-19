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

    def readCamera(self):
        self.capture.read()
        self.capture.showGreyFeed()

    def close(self):
        self.capture.release()

    def inputKey(self):
        return self.capture.input()
