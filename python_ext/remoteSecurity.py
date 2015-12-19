from imagePro import videoFeed

if __name__ == "__main__":
    securityCam =videoFeed()
    while(True):
        #capture frame by fraame
        securityCam.readCamera()
        if securityCam.inputKey() == ord('q'):
            break
    securityCam.close()
