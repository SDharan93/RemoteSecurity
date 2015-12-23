from imagePro import videoFeed
from imagePro import imageDetection

image1 = 0
image2 = 0
differenceImage = 0
thresholdImage = 0

def snapShot(cam):
    cam.readCamera()
    cam.showFrame1()
    image1 = cam.getGreyFrame1().copy()
    image2 = cam.getGreyFrame2().copy()

def setImages(control):
    control.setImage1(image1)

def main():
    securityCam =videoFeed()
    imageControl = imageDetection()
    while(True):
        #capture frame by fraame
        snapShot(securityCam)
        setImages(imageControl)
        if securityCam.inputKey() == ord('q'):
            break
    securityCam.close()

if __name__ == "__main__":
    main()
