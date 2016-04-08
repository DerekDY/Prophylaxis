import time
from ledmatrix import *


normFont = "/home/pi/Prophylaxis/rpi-rgb-led-matrix/fonts/5x8.bdf"
fontColor = "135, 206, 250"



#Button Setup
pin1 = 19   
selectButton = ButtonListener(pin1)

m = LEDMatrix()

#Loading Screen Test
m.display("BEGIN"," TEST1", fontColor, normFont)
time.sleep(3)
incr1 = 0
incr2 = 15
while(True):
    m.fill_rectangle(incr1,0,incr1,incr2, 1)   
    incr1 = incr1 + 1
    incr2 = incr2 - 1
    if incr1 == 32:
        incr1 = 0
    if incr2 == -1:
        incr2 = 15
    if selectButton.wasPressed():
        break
        
time.sleep(3)
m.display(" END"," TEST1", fontColor, normFont)
time.sleep(3)
m.clear()

#Image Tests
m.display("BEGIN"," TEST2", fontColor, normFont)
time.sleep(3)
m.display("THE","KNIGHT", fontColor, normFont)
time.sleep(3)

color = 1
m.set_pixel(20, 0, color):
m.set_pixel(20, 2, color):
m.set_pixel(20, 3, color):
m.set_pixel(20, 4, color):
m.set_pixel(20, 5, color):
m.set_pixel(20, 6, color):
m.set_pixel(20, 12, color):
m.set_pixel(20, 14, color):
m.set_pixel(20, 15, color):
m.set_pixel(21, 0, color):
m.set_pixel(21, 1, color):
m.set_pixel(21, 7, color):
m.set_pixel(21, 11, color):
m.set_pixel(21, 12, color):
m.set_pixel(21, 14, color):
m.set_pixel(21, 15, color):
m.set_pixel(22, 0, color):
m.set_pixel(22, 1, color):
m.set_pixel(22, 3, color):
m.set_pixel(22, 6, color):
m.set_pixel(22, 7, color):
m.set_pixel(22, 10, color):
m.set_pixel(22, 11, color):
m.set_pixel(22, 14, color):
m.set_pixel(22, 15, color):
m.set_pixel(23, 0, color):
m.set_pixel(23, 1, color):
m.set_pixel(23, 5, color):
m.set_pixel(23, 6, color):
m.set_pixel(23, 9, color):
m.set_pixel(23, 10, color):
m.set_pixel(23, 14, color):
m.set_pixel(23, 15, color):
m.set_pixel(24, 0, color):
m.set_pixel(23, 1, color):
m.set_pixel(23, 4, color):
m.set_pixel(23, 5, color):
m.set_pixel(23, 8, color):
m.set_pixel(23, 9, color):
m.set_pixel(23, 12, color):
m.set_pixel(23, 14, color):
m.set_pixel(23, 15, color):
m.set_pixel(24, 0, color):
m.set_pixel(24, 1, color):
m.set_pixel(24, 7, color):
m.set_pixel(24, 8, color):
m.set_pixel(24, 11, color):
m.set_pixel(24, 12, color):
m.set_pixel(24, 14, color):
m.set_pixel(24, 15, color):
m.set_pixel(25, 0, color):
m.set_pixel(25, 1, color):
m.set_pixel(25, 5, color):
m.set_pixel(25, 6, color):
m.set_pixel(25, 7, color):
m.set_pixel(25, 10, color):
m.set_pixel(25, 11, color):
m.set_pixel(25, 14, color):
m.set_pixel(25, 15, color):
m.set_pixel(26, 1, color):
m.set_pixel(26, 2, color):
m.set_pixel(26, 3, color):
m.set_pixel(26, 4, color):
m.set_pixel(26, 5, color):
m.set_pixel(26, 6, color):
m.set_pixel(26, 9, color):
m.set_pixel(26, 10, color):
m.set_pixel(26, 14, color):
m.set_pixel(26, 15, color):
m.set_pixel(27, 2, color):
m.set_pixel(27, 3, color):
m.set_pixel(27, 4, color):
m.set_pixel(27, 8, color):
m.set_pixel(27, 9, color):
m.set_pixel(27, 14, color):
m.set_pixel(27, 15, color):
m.set_pixel(28, 15, color): 
time.sleep(5)
m.clear()


#PAWN
m.display("TEST2"," PAWN", fontColor, normFont)
time.sleep(3)
m.fill_rectangle(25, 2, 27, 15, color)
m.fill_rectangle(24, 3, 24, 6, color)
m.fill_rectangle(28, 3, 28, 6, color)
m.fill_rectangle(22, 14, 30, 15, color)
m.fill_rectangle(23, 13, 29, 13, color)
m.set_pixel(24, 8, color):
m.set_pixel(28, 8, color):
m.set_pixel(24, 12, color):
m.set_pixel(28, 12, color):
time.sleep(5)
m.clear()


#KNIGHT
m.display("TEST2"," KNIGHT", fontColor, normFont)
time.sleep(3)
m.fill_rectangle(19, 8, 22, 15, color)
m.fill_rectangle(25, 8, 28, 15, color)
m.fill_rectangle(23, 13, 24, 15, color)
m.fill_rectangle(19, 3, 28, 5, color)
m.fill_rectangle(19, 6, 19, 7, color)
m.fill_rectangle(28, 6, 28, 7, color)
m.fill_rectangle(20, 2, 27, 2, color)
m.fill_rectangle(21, 1, 26, 1, color)
m.fill_rectangle(20, 0, 25, 0, color)
time.sleep(5)
m.clear()


#BISHOP
m.display("TEST2"," BISHOP", fontColor, normFont)
time.sleep(3)
m.fill_rectangle(25, 4, 27, 15, color)
m.fill_rectangle(24, 2, 24, 6, color)
m.fill_rectangle(28, 2, 28, 6, color)
m.fill_rectangle(22, 14, 30, 15, color)
m.fill_rectangle(23, 13, 29, 13, color)
m.fill_rectangle(25, 1, 26, 2, color)
m.set_pixel(24, 8, color):
m.set_pixel(28, 8, color):
m.set_pixel(24, 12, color):
m.set_pixel(28, 12, color):
m.set_pixel(27, 3, color):
m.set_pixel(27, 1, color):
m.set_pixel(26, 0, color):
time.sleep(5)
m.clear()


#ROOK
m.display("TEST2"," ROOK", fontColor, normFont)
time.sleep(3)
m.fill_rectangle(24, 1, 27, 15, color)
m.fill_rectangle(23, 1, 23, 3, color)
m.fill_rectangle(22, 0, 22, 2, color)
m.fill_rectangle(28, 1, 28, 3, color)
m.fill_rectangle(29, 0, 29, 2, color)
m.fill_rectangle(23, 10, 23, 15, color)
m.fill_rectangle(28, 10, 28, 15, color)
m.fill_rectangle(21, 14, 22, 15, color)
m.fill_rectangle(29, 14, 30, 15, color)
m.set_pixel(22, 13, color):
m.set_pixel(29, 13, color):
time.sleep(5)
m.clear()


#QUEEN
m.display("TEST2"," QUEEN", fontColor, normFont)
time.sleep(3)
m.fill_rectangle(25, 3, 27, 15, color)
m.fill_rectangle(23, 7, 29, 7, color)
m.fill_rectangle(24, 6, 28, 6, color)
m.fill_rectangle(24, 4, 28, 4, color)
m.fill_rectangle(23, 3, 29, 3, color)
m.fill_rectangle(23, 1, 23, 3, color)
m.fill_rectangle(29, 1, 29, 3, color)
m.fill_rectangle(22, 14, 30, 15, color)
m.fill_rectangle(23, 13, 29, 13, color)
m.set_pixel(25, 2, color):
m.set_pixel(27, 2, color):
m.set_pixel(24, 12, color):
m.set_pixel(28, 12, color):
time.sleep(5)
m.clear()


#KING
m.display("TEST2"," KING", fontColor, normFont)
time.sleep(3)
m.fill_rectangle(25, 3, 27, 15, color)
m.fill_rectangle(22, 14, 30, 15, color)
m.fill_rectangle(23, 13, 29, 13, color)
m.fill_rectangle(23, 10, 29, 10, color)
m.fill_rectangle(23, 3, 29, 3, color)
m.fill_rectangle(26, 0, 26, 2, color)
m.fill_rectangle(25, 1, 27, 1, color)
m.set_pixel(24, 12, color):
m.set_pixel(28, 12, color):
m.set_pixel(24, 9, color):
m.set_pixel(28, 9, color):
m.set_pixel(24, 6, color):
m.set_pixel(28, 6, color):
m.set_pixel(24, 4, color):
m.set_pixel(28, 4, color):
time.sleep(5)
m.clear()


m.display(" END"," TEST2", fontColor, normFont)
time.sleep(3)
m.clear()



m.display(" BEGIN"," TEST3", fontColor, normFont)
time.sleep(3)
m.clear()

#BISHOP
m.fill_rectangle(25, 4, 27, 15, color)
m.fill_rectangle(24, 2, 24, 6, color)
m.fill_rectangle(28, 2, 28, 6, color)
m.fill_rectangle(22, 14, 30, 15, color)
m.fill_rectangle(23, 13, 29, 13, color)
m.fill_rectangle(25, 1, 26, 2, color)
m.set_pixel(24, 8, color):
m.set_pixel(28, 8, color):
m.set_pixel(24, 12, color):
m.set_pixel(28, 12, color):
m.set_pixel(27, 3, color):
m.set_pixel(27, 1, color):
m.set_pixel(26, 0, color):

#CAPTURE
m.fill_rectangle(5, 2, 11, 3, color)
m.fill_rectangle(6, 1, 10, 1, color)
m.fill_rectangle(5, 4, 5, 5, color)
m.fill_rectangle(8, 4, 8, 5, color)
m.fill_rectangle(11, 4, 11, 5, color)
m.fill_rectangle(6, 6, 7, 6, color)
m.fill_rectangle(9, 6, 10, 6, color)
m.fill_rectangle(7, 7, 9, 7, color)
m.fill_rectangle(7, 9, 9, 9, color)
m.fill_rectangle(3, 10, 5, 10, color)
m.fill_rectangle(11, 10, 13, 10, color)
m.fill_rectangle(5, 11, 11, 11, color)
m.fill_rectangle(7, 12, 9, 12, color)
m.fill_rectangle(5, 13, 7, 13, color)
m.fill_rectangle(9, 13, 11, 13, color)
m.fill_rectangle(3, 14, 5, 14, color)
m.fill_rectangle(11, 14, 13, 14, color)
m.fill_rectangle(4, 15, 12, 14, color)
m.set_pixel(6, 8, color):
m.set_pixel(10, 8, color):
m.set_pixel(4, 9, color):
m.set_pixel(12, 9, color):

time.sleep(5)
m.display(" END"," TEST3", fontColor, normFont)
time.sleep(3)
m.clear()



m.display(" BEGIN"," TEST4", fontColor, normFont)
time.sleep(3)
m.clear()

#BISHOP
m.fill_rectangle(25, 4, 27, 15, color)
m.fill_rectangle(24, 2, 24, 6, color)
m.fill_rectangle(28, 2, 28, 6, color)
m.fill_rectangle(22, 14, 30, 15, color)
m.fill_rectangle(23, 13, 29, 13, color)
m.fill_rectangle(25, 1, 26, 2, color)
m.set_pixel(24, 8, color):
m.set_pixel(28, 8, color):
m.set_pixel(24, 12, color):
m.set_pixel(28, 12, color):
m.set_pixel(27, 3, color):
m.set_pixel(27, 1, color):
m.set_pixel(26, 0, color):

#MOVE
m.fill_rectangle(1, 6, 12, 8, color)
m.fill_rectangle(8, 9, 11, 9, color)
m.fill_rectangle(8, 10, 10, 8, color)
m.fill_rectangle(8, 11, 9, 11, color)
m.fill_rectangle(8, 5, 11, 5, color)
m.fill_rectangle(8, 4, 10, 4, color)
m.fill_rectangle(8, 3, 9, 3, color)
m.set_pixel(8, 2, color):
m.set_pixel(13, 7, color):
m.set_pixel(8, 12, color):

time.sleep(5)
m.display(" END"," TEST4", fontColor, normFont)
time.sleep(3)
m.clear()





