import time
import var

#class is responsible for sending time in various formats and track time
#used in sensor.py to track when the user was last notified
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

    #pauses time for var.TIME amount, default is 5 mins
    def pauseTime(self):
        self.passedTime = self.timeNow + var.TIME

    def isPassedTime(self):
        #if the timer is passed the pause time, notify user
        diff = self.timeNow >= self.passedTime
        #if enough time is passed, pause time
        if diff == True:
            self.pauseTime()
        return diff
