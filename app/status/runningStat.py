#class is responsible for tracking if a program is running in run.py
#essentially just tracks boolean Running and toggles
class runningStat(object):

    def __init__(self):
        self.Running = False

    def getRunning(self):
        return self.Running

    def setRunning(self, stat):
        self.Running = stat

    def switch(self):
        self.Running = not(self.Running)
