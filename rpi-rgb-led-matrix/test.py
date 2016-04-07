import time
from ledmatrix import *


upperText1 = "  The "
lowerText1 = " Knight"
color1 = "255,75,0"
font1 = "/home/pi/Prophylaxis/rpi-rgb-led-matrix/fonts/4x6.bdf"


m = LEDMatrix()
m.display("Hello","World")
time.sleep(3)
m.display(upperText1, lowerText1, color1, font1)
time.sleep(3)
m.display("Bye")
time.sleep(3)
m.clear()
