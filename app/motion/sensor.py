from imagePro import videoFeed
from imagePro import imageDetection
from common import dateTime
import common.var as var
from messenger import notify
from threading import Thread

class remote(object):

    def __init__(self):
        self.debug = False
        self.cam = videoFeed()
        self.control = imageDetection()
        self.timer = dateTime()
        self.alert = False
        self.running = True

    def snapShot(self):
        self.cam.readCamera()
        self.cam.showFrame1()

    def setImages(self):
        image1 = self.cam.getGreyFrame1().copy()
        image2 = self.cam.getGreyFrame2().copy()
        self.control.setImage1(image1)
        self.control.setImage2(image2)

    def capture(self):
        #capture frame by fraame
        self.snapShot()
        #transfer data and calculate threshold images
        self.setImages()
        #search for motion within camera range
        self.detectMotion()
        #debug mode for program
        if self.debug == True:
            self.showExtra()
        #inputs from user
        self.cam.checkInput()

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
                #change to twilio send message
                print 'MOTION DETECTED at %s' % (time)
                self.message()

    def getTime(self):
        time = self.timer.getTime()
        return time

    def getFileDateTime(self):
        time = self.timer.getFileTime()
        return time

    def userInput(self):
        key = self.cam.getKey()
        inputChar = chr(key & 255)
        return inputChar

    def debugControl(self, debug):
        debug = not(debug)
        if debug == False:
            self.closeExtra()
        return debug

    def message(self):
        thread = Thread(target = notify.alert())
        thread.daemon = True
        thread.start()

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def run(self):


        while(True):
            self.capture()
            options = self.userInput()
            #check if input matches expected inputs from computer
            #quit the program
            if options == var.QUIT:
                break
            #check if debug mode
            elif options == var.DEBUG:
                self.debug = self.debugControl(self.debug)
            #check if user messaged stop
            if self.running == False:
                break
        #releases camera from the program and stop program
        self.cam.close()

if __name__ == "__main__":
    security = remote()
    security.run()
