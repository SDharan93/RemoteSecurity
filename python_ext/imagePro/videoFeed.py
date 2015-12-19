from opencv import videoControl

class videoFeed(object):

    capture = 0
    frame1 = 0
    frame2 = 0
    greyImage1 = 0
    greyImage2 = 0
    ret = False

    def __init__(self):
        self.capture = videoControl().captureCam()

    def readCamera(self):
        ret, self.frame1 = self.capture.read()
        self.greyImage1 = cv2.cvtColor(self.frame1, cv2.COLOR_BGR2GRAY)
        cv2.imshow('grey video feed', self.greyImage1)

    def close(self):
        self.capture.release()

    def inputKey(self):
        return cv2.waitKey(10) & 0xFF
