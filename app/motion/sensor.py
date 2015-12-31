from imagePro import videoFeed
from imagePro import imageDetection
from common import dateTime
import common.var as var
import sys
import select
from messenger import notify

class sensor(object):

    def __init__(self):
        self.debug = False
        self.cam = videoFeed()
        self.control = imageDetection()
        self.timer = dateTime()
        self.alert = False
        self.running = True

    #reads two frames from the camera
    def snapShot(self):
        self.cam.readCamera()
        #self.cam.showFrame1()

    #transfers two frames to the control class
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

    #shows extra windows for debug
    def showExtra(self):
        self.control.showThresholdImage()
        self.control.showDifferenceImage()

    #closes the extra windows opened for debug
    def closeExtra(self):
        self.cam.closeAll()

    #checks if motion has been detected will alert if found
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
                #alerts user via text
                self.message()

    #get time for video
    def getTime(self):
        time = self.timer.getTime()
        return time

    #gets time in for file format
    def getFileDateTime(self):
        time = self.timer.getFileTime()
        return time

    #gets input from user
    def userInput(self):
        #gets keyboard input
        key = self.cam.getKey()
        inputChar = chr(key & 255)
        return inputChar

    #gets input from the server
    def serverInput(self):
        message = "empty"
        #if stdin is empty, it is ignored
        if select.select([sys.stdin,],[],[],0.0)[0]:
            message = raw_input()
        return message

    #shows extra debug windows if 'd' is hit by user
    def debugControl(self, debug):
        debug = not(debug)
        if debug == False:
            self.closeExtra()
        return debug

    #alerts user via text that motion was detected
    def message(self):
        #alert threaded so recording is not scewed
        thread = Thread(target = notify.alert())
        thread.daemon = True
        thread.start()

    def run(self):
        while(True):
            self.capture()
            #message from the user
            options = self.userInput()
            #message from the server
            message = self.serverInput()

            #check if input matches expected inputs from computer
            #quit the program
            if options == var.QUIT:
                break
            #check if debug mode
            elif options == var.DEBUG:
                self.debug = self.debugControl(self.debug)

            #check if server messaged stop
            elif message == var.STOP:
                break

        #releases camera from the program and stop program
        self.cam.close()

if __name__ == "__main__":
    temp = sensor()
    temp.run()
