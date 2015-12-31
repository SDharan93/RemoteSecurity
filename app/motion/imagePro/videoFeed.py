from opencv import videoControl
#higher level video class to interact with sensor.py
class videoFeed(object):

    capture = 0
    frame1 = 0
    frame2 = 0
    greyImage1 = 0
    greyImage2 = 0
    ret = False
    inputKey = ' '

    def __init__(self):
        self.capture = videoControl()

    #takes two frames from camera and stores grey values as well
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

    #capture the next 2 frames
    def readCamera(self):
        self.capture.read()
        self.snapShot()

    #displays frame one in new window
    def showFrame1(self):
        self.capture.showVideoFeed1()

    #displays frame two in new window
    def showFrame2(self):
        self.capture.showVideoFeed2()

    #release the camera
    def close(self):
        self.capture.release()

    #destory all windows
    def closeAll(self):
        self.capture.destoryAll()

    #check keyboard input from user
    def checkInput(self):
        self.inputKey = self.capture.input()

    def getKey(self):
        return self.inputKey
