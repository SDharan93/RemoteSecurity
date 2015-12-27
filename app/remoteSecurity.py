from imagePro import videoFeed
from imagePro import imageDetection
from common import dateTime
import common.var as var

class remote(object):

    debug = False
    cam = 0
    control = 0
    timer = 0
    alert = False
    run = True

    def __init__(self):
        self.debug = False
        self.cam = videoFeed()
        self.control = imageDetection()
        self.timer = dateTime()

    def snapShot(self):
        self.cam.readCamera()
        self.cam.showFrame1()

    def setImages(self):
        image1 = self.cam.getGreyFrame1().copy()
        image2 = self.cam.getGreyFrame2().copy()
        self.control.setImage1(image1)
        self.control.setImage2(image2)

    def showExtra(self):
        self.control.showThresholdImage()
        self.control.showDifferenceImage()

    def closeExtra(self):
        self.cam.closeAll()

    def detectMotion(self):
        motionDetected = False
        self.control.thresholdCalc()
        motionDetected = self.control.detectMotion()
        time = self.getTime()

        #check if the time has passed the user specification
        self.alert = self.timer.isPassedTime()

        #replace with text and dropbox api later
        if motionDetected == True:
            if self.alert == True:
                print 'MOTION DETECTED at %s' % (time)

    def getTime(self):
        time = self.timer.getTime()
        return time

    def getFileDateTime(self):
        time = self.timer.getFileTime()
        return time

    def userInput(self, key):
        inputChar = chr(key & 255)
        return inputChar

    def debugControl(self, debug):
        debug = not(debug)
        if debug == False:
            self.closeExtra()
        return debug

    def start(self):
        self.run = True

    def stop(self):
        self.run = False

    def run(self):
        debug = False

        while(True):
            #capture frame by fraame
            self.snapShot()

            #transfer data and calculate threshold images
            self.setImages()

            #search for motion within camera range
            self.detectMotion()

            #debug mode for program
            if debug == True:
                self.showExtra()

            #inputs from user
            self.cam.checkInput()
            key = self.cam.getKey()
            options = self.userInput(key)

            #check if input matches expected inputs from computer
            #quit the program
            if options == var.QUIT:
                break

            #check if debug mode
            elif options == var.DEBUG:
                debug = self.debugControl(debug)

            #check if user messaged stop
            if self.run == False:
                break

        #releases camera from the program and stop program
        self.cam.close()

if __name__ == "__main__":
    security = remote()
    security.run()
