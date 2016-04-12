import subprocess
#New
import RPi.GPIO as GPIO
import time

from multiprocessing import Process

class LEDMatrix():


    def __init__(self):
        
        #New
        self.delay = 0.000001
        
        GPIO.setmode(GPIO.BCM)
        self.red1_pin = 11
        self.green1_pin = 27
        self.blue1_pin = 7
        self.red2_pin = 8
        self.green2_pin = 9
        self.blue2_pin = 10
        self.clock_pin = 17
        self.a_pin = 22
        self.b_pin = 23
        self.c_pin = 24
        self.latch_pin = 4
        self.oe_pin = 18
        
        self.smallFont = "/home/pi/THE-KNIGHT/rpi-rgb-led-matrix/fonts/4x6.bdf"
        self.normFont = "/home/pi/THE-KNIGHT/rpi-rgb-led-matrix/fonts/5x8.bdf"
        self.bigFont = "/home/pi/THE-KNIGHT/rpi-rgb-led-matrix/fonts/6x10.bdf"
        self.fontColor = "135, 206, 250"
        self.errorColor = "255,0,0"
        
        #Incorrect Pins
        '''
        self.red1_pin = 17
        self.green1_pin = 18
        self.blue1_pin = 22
        self.red2_pin = 23
        self.green2_pin = 24
        self.blue2_pin = 25
        self.clock_pin = 3
        self.a_pin = 7
        self.b_pin = 8
        self.c_pin = 9
        self.latch_pin = 4
        self.oe_pin = 2
        '''
        
        GPIO.setup(self.red1_pin, GPIO.OUT)
        GPIO.setup(self.green1_pin, GPIO.OUT)
        GPIO.setup(self.blue1_pin, GPIO.OUT)
        GPIO.setup(self.red2_pin, GPIO.OUT)
        GPIO.setup(self.green2_pin, GPIO.OUT)
        GPIO.setup(self.blue2_pin, GPIO.OUT)
        GPIO.setup(self.clock_pin, GPIO.OUT)
        GPIO.setup(self.a_pin, GPIO.OUT)
        GPIO.setup(self.b_pin, GPIO.OUT)
        GPIO.setup(self.c_pin, GPIO.OUT)
        GPIO.setup(self.latch_pin, GPIO.OUT)
        GPIO.setup(self.oe_pin, GPIO.OUT)

        self.screen = [[0 for x in range(32)] for x in range(16)]
            
        
        self.p = None



    def display(self, upperText, lowerText="", color="255,0,0", font="fonts/5x8.bdf"):
        if (self.p != None):
            self.p.terminate()
        if (lowerText == ""):
            self.p = subprocess.Popen(["./rgbmatrixrun", "-f", self.normFont, "-T", upperText, "-C", color])
        else:
            self.p = subprocess.Popen(["./rgbmatrixrun", "-f", font, "-T", upperText, "-t", lowerText, "-C", color])

    def clear(self):
        if (self.p != None):
            self.p.terminate()

    #New
    def clock(self):
        GPIO.output(self.clock_pin, 1)
        GPIO.output(self.clock_pin, 0)

    def latch(self):
        GPIO.output(self.latch_pin, 1)
        GPIO.output(self.latch_pin, 0)

    def bits_from_int(self,x):
        a_bit = x & 1
        b_bit = x & 2
        c_bit = x & 4
        return (a_bit, b_bit, c_bit)

    def set_row(self,row):
        #time.sleep(delay)
        a_bit, b_bit, c_bit = self.bits_from_int(row)
        GPIO.output(self.a_pin, a_bit)
        GPIO.output(self.b_pin, b_bit)
        GPIO.output(self.c_pin, c_bit)
        #time.sleep(delay)

    def set_color_top(self,color):
        #time.sleep(delay)
        red, green, blue = self.bits_from_int(color)
        GPIO.output(self.red1_pin, red)
        GPIO.output(self.green1_pin, green)
        GPIO.output(self.blue1_pin, blue)
        #time.sleep(delay)

    def set_color_bottom(self,color):
        #time.sleep(delay)
        red, green, blue = self.bits_from_int(color)
        GPIO.output(self.red2_pin, red)
        GPIO.output(self.green2_pin, green)
        GPIO.output(self.blue2_pin, blue)
        #time.sleep(delay)

    def refresh(self):
        while True:
            for row in range(8):
                GPIO.output(self.oe_pin, 1)
                self.set_color_top(0)
                self.set_row(row)
                #time.sleep(delay)
                for col in range(32):
                    self.set_color_top(self.screen[row][col])
                    self.set_color_bottom(self.screen[row+8][col])
                    self.clock()
                #GPIO.output(oe_pin, 0)
                self.latch()
                GPIO.output(self.oe_pin, 0)
                time.sleep(self.delay)

    def fill_rectangle(self,x1, y1, x2, y2, color):
        for x in range(x1, x2):
            for y in range(y1, y2):
                self.screen[y][x] = color


    def set_pixel(self,x, y, color):
        self.screen[y][x] = color
        

    def draw_pawn(self, color):
        self.fill_rectangle(25, 2, 28, 15, color)
        self.fill_rectangle(22, 14, 30, 15, color)
        self.set_pixel(24, 6, color) 
        self.set_pixel(24, 5, color) 
        self.set_pixel(24, 4, color) 
        self.set_pixel(24, 3, color) 
        self.set_pixel(28, 6, color) 
        self.set_pixel(28, 5, color) 
        self.set_pixel(28, 4, color) 
        self.set_pixel(28, 3, color) 
        self.set_pixel(23, 13, color) 
        self.set_pixel(24, 13, color)
        self.set_pixel(29, 13, color) 
        self.set_pixel(28, 13, color)
        self.set_pixel(24, 8, color) 
        self.set_pixel(28, 8, color)
        self.set_pixel(30, 14, color)
        self.set_pixel(24, 12, color)
        self.set_pixel(28, 12, color)
        i = 22
        for x in range(9):
            self.set_pixel(i, 15, color)
            i = i + 1
            
    def draw_bishop(self, color):
        self.fill_rectangle(25, 4, 28, 16, color)
        self.fill_rectangle(24, 2, 25, 7, color)
        self.fill_rectangle(28, 2, 29, 7, color)
        self.fill_rectangle(22, 14, 31, 16, color)
        self.fill_rectangle(23, 13, 30, 14, color)
        self.fill_rectangle(25, 1, 27, 3, color)
        self.set_pixel(24, 8, color) 
        self.set_pixel(28, 8, color) 
        self.set_pixel(24, 12, color) 
        self.set_pixel(28, 12, color) 
        self.set_pixel(27, 3, color) 
        self.set_pixel(27, 1, color) 
        self.set_pixel(26, 0, color)
        self.set_pixel(25, 3, color)
        
        
    def draw_knight(self, color):
        self.fill_rectangle(19, 8, 23, 16, color)
        self.fill_rectangle(25, 8, 29, 16, color)
        self.fill_rectangle(23, 13, 25, 16, color)
        self.fill_rectangle(19, 3, 29, 6, color)
        self.fill_rectangle(19, 6, 20, 8, color)
        self.fill_rectangle(28, 6, 29, 8, color)
        self.fill_rectangle(20, 2, 28, 3, color)
        self.fill_rectangle(21, 1, 27, 2, color)
        self.fill_rectangle(22, 0, 26, 1, color) 
    
    def draw_rook(self, color):
        self.fill_rectangle(24, 1, 28, 16, color)
        self.fill_rectangle(23, 1, 24, 4, color)
        self.fill_rectangle(22, 0, 23, 3, color)
        self.fill_rectangle(28, 1, 29, 4, color)
        self.fill_rectangle(29, 0, 30, 3, color)
        self.fill_rectangle(23, 10, 24, 16, color)
        self.fill_rectangle(28, 10, 29, 16, color)
        self.fill_rectangle(21, 14, 23, 16, color)
        self.fill_rectangle(29, 14, 31, 16, color)
        self.set_pixel(25, 0, color)
        self.set_pixel(26, 0, color)
        self.set_pixel(22, 13, color) 
        self.set_pixel(29, 13, color)
    
    def draw_queen(self, color):
        self.fill_rectangle(25, 3, 28, 15, color)
        self.fill_rectangle(23, 7, 30, 8, color)
        self.fill_rectangle(24, 6, 29, 7, color)
        self.fill_rectangle(24, 4, 29, 5, color)
        self.fill_rectangle(23, 3, 30, 4, color)
        self.fill_rectangle(23, 1, 24, 4, color)
        self.fill_rectangle(29, 1, 30, 4, color)
        self.fill_rectangle(22, 14, 31, 15, color)
        self.fill_rectangle(23, 13, 30, 14, color)
        self.set_pixel(25, 2, color) 
        self.set_pixel(27, 2, color) 
        self.set_pixel(24, 12, color) 
        self.set_pixel(28, 12, color) 
        
    def draw_king(self, color):
        self.fill_rectangle(25, 3, 28, 16, color)
        self.fill_rectangle(22, 14, 31, 16, color)
        self.fill_rectangle(23, 13, 30, 14, color)
        self.fill_rectangle(23, 10, 30, 11, color)
        self.fill_rectangle(23, 3, 30, 4, color)
        self.fill_rectangle(26, 0, 27, 3, color)
        self.fill_rectangle(25, 1, 28, 2, color)
        self.set_pixel(24, 12, color) 
        self.set_pixel(28, 12, color) 
        self.set_pixel(24, 9, color) 
        self.set_pixel(28, 9, color) 
        self.set_pixel(24, 6, color) 
        self.set_pixel(28, 6, color) 
        self.set_pixel(24, 4, color) 
        self.set_pixel(28, 4, color)
        
    def draw_capture(self, color):
        self.fill_rectangle(5, 2, 12, 4, color)
        self.fill_rectangle(6, 1, 11, 2, color)
        self.fill_rectangle(5, 4, 6, 6, color)
        self.fill_rectangle(8, 4, 9, 6, color)
        self.fill_rectangle(11, 4, 12, 6, color)
        self.fill_rectangle(6, 6, 8, 7, color)
        self.fill_rectangle(9, 6, 11, 7, color)
        self.fill_rectangle(7, 7, 10, 8, color)
        self.fill_rectangle(7, 9, 10, 10, color)
        self.fill_rectangle(3, 10, 6, 11, color)
        self.fill_rectangle(11, 10, 14, 11, color)
        self.fill_rectangle(5, 11, 12, 12, color)
        self.fill_rectangle(7, 12, 10, 13, color)
        self.fill_rectangle(5, 13, 8, 14, color)
        self.fill_rectangle(9, 13, 12, 14, color)
        self.fill_rectangle(3, 14, 6, 15, color)
        self.fill_rectangle(11, 14, 14, 15, color)
        self.fill_rectangle(4, 15, 13, 15, color)
        self.set_pixel(6, 8, color) 
        self.set_pixel(10, 8, color) 
        self.set_pixel(4, 9, color) 
        self.set_pixel(12, 9, color) 
        
        
    def draw_move(self, color):
        self.fill_rectangle(1, 6, 13, 9, color)
        self.fill_rectangle(8, 9, 12, 10, color)
        self.fill_rectangle(8, 11, 10, 12, color)
        self.fill_rectangle(8, 5, 12, 6, color)
        self.fill_rectangle(8, 4, 11, 5, color)
        self.fill_rectangle(8, 3, 10, 4, color)
        self.set_pixel(8, 2, color) 
        self.set_pixel(8, 10, color) 
        self.set_pixel(9, 10, color) 
        self.set_pixel(10, 10, color) 
        self.set_pixel(13, 7, color)
        self.set_pixel(8, 12, color)
        
    def draw_logo(self, color):
        self.set_pixel(20, 0, color)
        self.set_pixel(20, 2, color) 
        self.set_pixel(20, 3, color) 
        self.set_pixel(20, 4, color) 
        self.set_pixel(20, 5, color) 
        self.set_pixel(20, 6, color) 
        self.set_pixel(20, 12, color) 
        self.set_pixel(20, 14, color) 
        self.set_pixel(20, 15, color) 
        self.set_pixel(21, 0, color) 
        self.set_pixel(21, 1, color) 
        self.set_pixel(21, 7, color) 
        self.set_pixel(21, 11, color) 
        self.set_pixel(21, 12, color) 
        self.set_pixel(21, 14, color) 
        self.set_pixel(21, 15, color) 
        self.set_pixel(22, 0, color) 
        self.set_pixel(22, 1, color) 
        self.set_pixel(22, 3, color) 
        self.set_pixel(22, 6, color) 
        self.set_pixel(22, 7, color) 
        self.set_pixel(22, 10, color) 
        self.set_pixel(22, 11, color) 
        self.set_pixel(22, 14, color) 
        self.set_pixel(22, 15, color) 
        self.set_pixel(23, 0, color) 
        self.set_pixel(23, 1, color) 
        self.set_pixel(23, 5, color) 
        self.set_pixel(23, 6, color) 
        self.set_pixel(23, 9, color) 
        self.set_pixel(23, 10, color) 
        self.set_pixel(23, 14, color) 
        self.set_pixel(23, 15, color) 
        self.set_pixel(24, 0, color) 
        self.set_pixel(23, 1, color) 
        self.set_pixel(23, 4, color) 
        self.set_pixel(23, 5, color) 
        self.set_pixel(23, 8, color) 
        self.set_pixel(23, 9, color) 
        self.set_pixel(23, 12, color) 
        self.set_pixel(23, 14, color) 
        self.set_pixel(23, 15, color) 
        self.set_pixel(24, 0, color) 
        self.set_pixel(24, 1, color) 
        self.set_pixel(24, 7, color) 
        self.set_pixel(24, 8, color) 
        self.set_pixel(24, 11, color) 
        self.set_pixel(24, 12, color) 
        self.set_pixel(24, 14, color) 
        self.set_pixel(24, 15, color) 
        self.set_pixel(25, 0, color) 
        self.set_pixel(25, 1, color) 
        self.set_pixel(25, 5, color) 
        self.set_pixel(25, 6, color) 
        self.set_pixel(25, 7, color) 
        self.set_pixel(25, 10, color) 
        self.set_pixel(25, 11, color) 
        self.set_pixel(25, 14, color) 
        self.set_pixel(25, 15, color) 
        self.set_pixel(26, 1, color) 
        self.set_pixel(26, 2, color) 
        self.set_pixel(26, 3, color) 
        self.set_pixel(26, 4, color) 
        self.set_pixel(26, 5, color) 
        self.set_pixel(26, 6, color) 
        self.set_pixel(26, 9, color) 
        self.set_pixel(26, 10, color) 
        self.set_pixel(26, 14, color) 
        self.set_pixel(26, 15, color) 
        self.set_pixel(27, 2, color) 
        self.set_pixel(27, 3, color) 
        self.set_pixel(27, 4, color) 
        self.set_pixel(27, 8, color) 
        self.set_pixel(27, 9, color) 
        self.set_pixel(27, 14, color) 
        self.set_pixel(27, 15, color) 
        self.set_pixel(28, 15, color) 
        
    def displayCapture(self,strPiece):
        if strPiece == 'p':
            self.draw_pawn(1)
            self.draw_capture(1)
        elif strPiece == 'N':
            self.draw_knight(1)
            self.draw_capture(1)
        elif strPiece == 'B':
            self.draw_bishop(1)
            self.draw_capture(1)
        elif strPiece == 'R':
            self.draw_rook(1)
            self.draw_capture(1)
        elif strPiece == 'Q':
            self.draw_queen(1)
            self.draw_capture(1)
        elif strPiece == 'K':
            self.draw_king(1)
            self.draw_capture(1)
        
    def displayMove(self,strPiece):
        if strPiece == 'p':
            self.draw_pawn(1)
            self.draw_move(1)
        elif strPiece == 'N':
            self.draw_knight(1)
            self.draw_move(1)
        elif strPiece == 'B':
            self.draw_bishop(1)
            self.draw_move(1)
        elif strPiece == 'R':
            self.draw_rook(1)
            self.draw_move(1)
        elif strPiece == 'Q':
            self.draw_queen(1)
            self.draw_move(1)
        elif strPiece == 'K':
            self.draw_king(1)
            self.draw_move(1)


