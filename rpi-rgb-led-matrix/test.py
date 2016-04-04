import time
from ledmatrix import *

m = LEDMatrix()
m.display("Hello","World")
time.sleep(3)
m.display("Bye")
time.sleep(3)
m.clear()
