from motorGraphics import *
test = 1
try:
    from motor import *  #real motor
    from magnet import *
except ImportError:
    test = 0
    pass

from Coordinate import Coordinate as C
from subprocess import call
from multiprocessing import Process
from BlueTooth import *

'''
Class: 			XYTable
Author: 		Derek De Young
Revision Date: 		9-28-15
Last revision:		2-6-2016
Description: 	This class encapsulates the 2 motors and magnets of the 
                XY table into one class				
Paramaters: 	self (XYTable object)
Return: 		and XY Table Object
To-Do: 			delete graphics objects
'''

class XYTable:

<<<<<<< HEAD
	def __init__(self, testingOption = 0):   #when testing is 1 the physical motors will not be made 
		self.testing = testingOption
		self.motorXG = MotorG(0)
		self.motorYG = MotorG(1)
		if (testingOption == 0): 
			motor1 = Motor(0) 
			motor2 = Motor(1)
			bluetooth = Bluetooth(2)
			#print ("I'm making a motor")
			print("Who is USB0")
			print(motor1.who())
			print("Who is USB1")
			print(motor2.who())
			print("Who is USB2")
			print(bluetooth.who())
			if (motor1.who().strip() == "X"):
				self.motorX = motor1
				print ("I MADE USB0 MOTOR X")
				if (motor2.who().strip() == "Y"):
					self.motorY = motor2
					print ("I MADE USB1 MOTOR Y")
					self.bt = bluetooth
				else:
					self.bt = Bluetooth(motor2.serialPort)
					self.motorY = Motor(bluetooth.serialPort)
			else:
				if (motor2.who().strip() == "Y"):
					self.bt = Bluetooth(motor1.serialPort)
					self.motorY = motor2
					self.motorX = Motor(bluetooth.serialPort)
				elif (bluetooth.who().strip() == "BT"):
					self.bt = bluetooth
					self.motorY = motor1
					self.motorX = motor2	
				elif (bluetooth.who().strip() == "Y"):
					self.bt = Bluetooth(motor2.serialPort)
					self.motorY = motor1
					self.motorX = Motor(bluetooth.serialPort)	
				else:
					print("something went wrong here folks")
			
			print("USBs are set up")
				
		self.magnet = Magnet(0)
		self.x = None  #need to initialize table before knowing 
		self.y = None
    	
=======
    def __init__(self, testingOption = 0):   #when testing is 1 the physical motors will not be made 
        self.testing = testingOption
        self.motorXG = MotorG(0)
        self.motorYG = MotorG(1)
        if (testingOption == 0): 
            motor1 = Motor(0) 
            motor2 = Motor(1)
            #print ("I'm making a motor")
            #print("Who is USB0")
            print(motor1.who())
            #print("Who is USB1")
            print(motor2.who())
            if (motor1.who().strip() == "X"):
                self.motorX = motor1
                #print ("I MADE USB0 MOTOR X")
                self.motorY = motor2
                #print ("I MADE USB1 MOTOR Y")
            else:
                self.motorX = motor2
                #print ("I MADE USB1 MOTOR X")
                self.motorY = motor1
                #print ("I MADE USB0 MOTOR Y")
            #print("WE MADE THE MOTORS")
        if test == 1:
            self.magnet = Magnet(0)
        self.x = None  #need to initialize table before knowing 
        self.y = None
        
>>>>>>> bb847f689d18231a02e61d36829320d026207be4

    '''
    Function: 		self.drawMotors()
    Description: 	This function will be removed in the actual version
                    it is using graphics.py to give a visual representative
    Paramaters: 	self (XYTable object)
        delete when move over 
    '''
    def drawMotors(self):
        self.motorXG.body.draw(self.win)
        self.motorYG.body.draw(self.win)
    
    
    '''
    Function: 		self.initialize_Coord()
    Description: 	This function must be called to initialize the table at 0,0
    
    '''
    def initialize_Coord(self):
        self.motorXG.zero()
        self.motorYG.zero()
        if (self.testing == 0):
            #print("Zero that ish?")
            xProcess = Process(target=self.motorX.zero, args=())
            yProcess = Process(target=self.motorY.zero, args=())
            xProcess.start()
            yProcess.start()
            xProcess.join()
            yProcess.join()
            #self.motorX.zero()
            #self.motorY.zero()
        #initialize the coordinates	
        self.x = 0
        self.y = 0
        #print ("Table is initialized")
        #print ("Coordinates are: " + str(self.x) + ", " + str(self.y))
    
    
    
    '''
    Function: 		self.turnoff()
    Author: 		Derek De Young
    Description: 	This function must be called to power off the board and
                    set the motors back to 0,0 			
    
    '''
    def turnoff(self):
        self.win = None
        
    
    
    '''
    Function: 		self.moveto()
    Description: 	This function is called to move the table to a point on 
                    the coordinate system 
    Paramaters: 	new_x and new_y both int for new coordinate point 
    
    '''	
    def moveto(self, new_x, new_y):
        dx = new_x - self.x
        dy = new_y - self.y 
        dxg = int(new_x/2.25 - self.x/2.25)
        dyg = int(new_y/2.25 - self.y/2.25)
        if (dx < 0):
            self.motorXG.cw(abs(dxg))
        else:
            self.motorXG.ccw(abs(dxg))
        if (dy < 0):
            self.motorYG.cw(abs(dyg))
        else:
            self.motorYG.ccw(abs(dyg))
        if (self.testing == 0):
            xProcess = Process(target=self.motorX.move, args=(dx,))
            yProcess = Process(target=self.motorY.move, args=(dy,))
            xProcess.start()
            yProcess.start()
            xProcess.join()
            yProcess.join()
            #self.motorX.move(dx)
            #self.motorY.move(dy)
        self.x = new_x
        self.y = new_y
        print ("Coordinates are: " + str(self.x) + ", " + str(self.y))
    
    
    '''
    Function: 		self.grab()
    Description: 	This function will call magnet.grab to turn on the magnet  				
    Paramaters: 	self (XYTable object)
    
    '''	
    def grab(self):
        self.motorXG.body.setFill('red')
        self.motorYG.body.setFill('red')
        #self.magnet.grab()
    
    
    '''
    Function: 		self.release()
    Author: 		Derek De Young
    Revision Date: 	9-28-15
    Last revision: 
    Description: 	This function will call magnet.release to turn off the magnet
    Paramaters: 	self (XYTable object)
    Return: 		none (Table is initialized and ready to be powered down)
    To-Do: 			delete graphics when ready
    
    '''	
    def release(self):
        self.motorXG.body.setFill('')
        self.motorYG.body.setFill('')
        #self.magnet.release()
        
         
    
