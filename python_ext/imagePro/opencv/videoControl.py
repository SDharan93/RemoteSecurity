import numpy as np
import cv2

class videoControl(object):

    def captureCam(self):
        cap = cv2.VideoCapture(0)
        return cap
