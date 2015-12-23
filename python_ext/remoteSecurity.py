from imagePro import videoFeed
from imagePro import imageDetection

if __name__ == "__main__":
    securityCam =videoFeed()
    imageControl = imageDetection()
    while(True):
        #capture frame by fraame
        securityCam.readCamera()
        securityCam.showFrame1()

        if securityCam.inputKey() == ord('q'):
            break
    securityCam.close()
