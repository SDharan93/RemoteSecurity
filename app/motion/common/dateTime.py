import time
import var

class dateTime(object):

    timeNow = 0
    checkPoint = 0
    passedTime = False

    def __init__(self):
        self.timeNow = time.time()
        self.passedTime = self.timeNow

    def getTime(self):
        timer = time.strftime("%H:%M:%S")
        self.timeNow = time.time()
        return timer

    def getFileDateTime(self):
        timer = time.strftime("%b_%d_%y_%H_%M_%S")
        return timer

    def pauseTime(self):
        self.passedTime = self.timeNow + var.TIME

    def isPassedTime(self):
        #if the timer is passed the pause time, notify user
        diff = self.timeNow >= self.passedTime
        if diff == True:
            self.pauseTime()
        return diff
