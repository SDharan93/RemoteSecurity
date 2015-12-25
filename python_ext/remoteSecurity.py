from imagePro import videoFeed
from imagePro import imageDetection

def snapShot(cam):
    cam.readCamera()
    cam.showFrame1()
    #cam.showFrame2()

def setImages(cam, control):
    image1 = cam.getGreyFrame1().copy()
    image2 = cam.getGreyFrame2().copy()
    control.setImage1(image1)
    control.setImage2(image2)
    control.thresholdCalc()

def showExtra(cam, control):
    control.showThresholdImage()
    control.showDifferenceImage()

def closeExtra(cam, control):
    cam.closeAll()

def detectMotion(control):
    motionDetected = False
    motionDetected = control.detectMotion()
    if motionDetected == True:
        print "MOTION DETECTED!!"

    else:
        print "NO MOTION"

def main():
    debug = False
    securityCam =videoFeed()
    imageControl = imageDetection()

    while(True):
        #capture frame by fraame
        snapShot(securityCam)

        #transfer data and calculate threshold images
        setImages(securityCam, imageControl)

        #search for motion within camera range
        detectMotion(imageControl)

        #debug mode for program
        if debug == True:
            showExtra(securityCam, imageControl)

        #inputs from user
        securityCam.checkInput()
        key = securityCam.getKey()

        #check if input matches expected inputs
        #quit the program
        if chr(key & 255) == 'q':
            break

        #check if debug mode
        elif chr(key & 255) == 'd':
            debug = not(debug)
            if debug == False:
                closeExtra(securityCam, imageControl)

    #releases camera from the program
    securityCam.close()

if __name__ == "__main__":
    main()
