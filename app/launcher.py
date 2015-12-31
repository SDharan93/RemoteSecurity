#launcher for the motion detection program
from motion import sensor

class runApp(object):

    def __init__(self):
        self.sensor = sensor()

    def run(self):
        self.sensor.run()

if __name__ == "__main__":
    temp = runApp()
    temp.run()
