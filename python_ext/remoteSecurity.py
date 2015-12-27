from imagePro import videoFeed
from imagePro import imageDetection
import common.dateTime as formatTime
import common.var as var

class remote(object):

    debug = False
    cam = 0
    control = 0

    def __init__(self):
        self.debug = False
        self.cam = videoFeed()
        self.control = imageDetection()

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

        #replace with text and dropbox api later
        if motionDetected == True:
            print 'MOTION DETECTED at %s!!' % (time)

        else:
            print "NO MOTION"

    def getTime(self):
        time = formatTime.getTime()
        return time

    def getFileDateTime(self):
        time = formatTime.getFileTime()
        return time

    def userInput(self, key):
        inputChar = chr(key & 255)
        return inputChar

    def debugControl(self, debug):
        debug = not(debug)
        if debug == False:
            self.closeExtra()
        return debug

    def main(self):
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

            #check if input matches expected inputs
            #quit the program
            if options == var.QUIT:
                break

            #check if debug mode
            elif options == var.DEBUG:
                debug = self.debugControl(debug)

        #releases camera from the program
        self.cam.close()

if __name__ == "__main__":
    security = remote()
    security.main()
