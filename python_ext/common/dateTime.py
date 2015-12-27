import time

def getTime():
    #print (time.strftime("%H:%M:%S"))
    timeNow = time.strftime("%H:%M:%S")
    return timeNow

def getFileDateTime():
    timeNow = time.strftime("%b_%d_%y_%H_%M_%S")
    return timeNow
