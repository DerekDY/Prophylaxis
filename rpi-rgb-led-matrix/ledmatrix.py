import subprocess

class LEDMatrix():

    def __init__(self):
        self.p = None

    def display(self, upperText, lowerText="", color="255,0,0", font="fonts/5x8.bdf"):
        if (self.p != None):
            self.p.terminate()
        if (lowerText == ""):
            self.p = subprocess.Popen(["./rgbmatrixrun", "-f", font, "-T", upperText, "-C", color])
        else:
            self.p = subprocess.Popen(["./rgbmatrixrun", "-f", font, "-T", upperText, "-t", lowerText, "-C", color])

    def clear(self):
        if (self.p != None):
            self.p.terminate()
