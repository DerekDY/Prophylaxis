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
from ledmatrix import *

'''
Class: 			XYTable
Description: 	This class encapsulates the 2 motors and magnets of the 
                XY table into one class				
Paramaters: 	self (XYTable object)
Return: 		and XY Table Object
To-Do: 			delete graphics objects
'''

class XYTable:

	def __init__(self, testingOption = 0):   #when testing is 1 the physical motors will not be made 
		self.testing = testingOption
		print("Making xy tbale")
		print(testingOption)
		testingOption = 0
		self.testing = testingOption
		if (testingOption == 0): 
			motor1 = Motor(0) 
			motor2 = Motor(1)
			motor3 = Motor(2)
			motor4 = Motor(3)
			#bluetooth = Bluetooth(2)
			motor1is= None
			motor2is= None
			motor3is= None
			motor4is= None
			time.sleep(1.5)
			if motor1.connected:
				motor1is = motor1.who()
				#print("USB0 connected")
			if motor2.connected:
				motor2is = motor2.who()
				#print("USB1 connected")
			if motor3.connected:
				motor3is = motor3.who()
				#print("USB2 connected")
			if motor4.connected:
				motor4is = motor4.who()
				#print("USB3 connected")
			
			
			if (motor1is.strip() == "X"):
				print("USB0 is MotorX")
				self.motorX = motor1 
				if (motor2is.strip() == "Y"):
					print("USB1 is MotorY")
					self.motorY = motor2
					if motor3is.strip() == "Z":
						print("USB2 is BT")
						print("USB3 is Matrix")
						self.ledMatrix = LEDMatrix(motor4.serialPort)
						self.bt = Bluetooth(motor3.serialPort)
					else: 
						print("USB2 is Matrix")
						print("USB3 is BT")
						self.ledMatrix = LEDMatrix(motor3.serialPort)
						self.bt = Bluetooth(motor4.serialPort)
				elif (motor2is.strip() == "Z"):
					print("USB1 is BT")
					self.bt = Bluetooth(motor2.serialPort)
					if motor3is.strip() == "Y":
						print("USB2 is MotorY")
						self.motorY = motor3
						print("USB3 is Matrix")
						self.ledMatrix = LEDMatrix(motor4.serialPort)
					else: 
						print("USB2 is Matrix")
						print("USB3 is MotorY")
						self.ledMatrix = LEDMatrix(motor3.serialPort)
						self.motorY = motor4
				else:
					print("USB1 is Matrix")
					self.ledMatrix = LEDMatrix(motor2.serialPort)
					if motor3is.strip() == "Z":
						print("USB2 is BT")
						print("USB3 is MotorY")
						self.bt = Bluetooth(motor3.serialPort)
						self.motorY = motor4
					else: 
						print("USB2 is MotorY")
						print("USB3 is BT")
						self.motorY = motor3
						self.bt = Bluetooth(motor4.serialPort)
			elif (motor1is.strip() == "Y"):
				print("USB0 is MotorY")
				self.motorY = motor1 
				if (motor2is.strip() == "X"):
					print("USB1 is MotorX")
					self.motorX = motor2
					if motor3is.strip() == "Z":
						print("USB2 is BT")
						print("USB3 is Matrix")
						self.bt = Bluetooth(motor3.serialPort)
						self.ledMatrix = LEDMatrix(motor4.serialPort)
					else: 
						print("USB2 is Matrix")
						print("USB3 is BT")
						self.ledMatrix = LEDMatrix(motor3.serialPort)
						self.bt = Bluetooth(motor4.serialPort)
				elif (motor2is.strip() == "Z"):
					print("USB1 is BT")
					self.bt = Bluetooth(motor2.serialPort)
					if motor3is.strip() == "X":
						print("USB2 is MotorX")
						self.motorX = motor3
						print("USB3 is Matrix")
						self.ledMatrix = LEDMatrix(motor4.serialPort)
					else: 
						print("USB2 is Matrix")
						print("USB3 is MotorX")
						self.ledMatrix = LEDMatrix(motor3.serialPort)
						self.motorX = motor4
				else:
					print("USB1 is Matrix")
					self.ledMatrix = LEDMatrix(motor2.serialPort)
					if motor3is.strip() == "Z":
						print("USB2 is BT")
						print("USB3 is MotorX")
						self.bt = Bluetooth(motor3.serialPort)
						self.motorX = motor4
					else: 
						print("USB2 is MotorX")
						print("USB3 is BT")
						self.motorX = motor3
						self.bt = Bluetooth(motor4.serialPort)
			elif (motor1is.strip() == "Z"):
				print("USB0 is BT")
				self.bt = Bluetooth(motor1.serialPort) 
				if (motor2is.strip() == "X"):
					print("USB1 is MotorX")
					self.motorX = motor2
					if motor3is.strip() == "Y":
						print("USB2 is MotorY")
						self.ledMatrix = LEDMatrix(motor4.serialPort)
						print("USB3 is Matrix") 
						self.motorY = motor3
					else: 
						self.ledMatrix = LEDMatrix(motor3.serialPort)
						print("USB2 is Matrix") 
						print("USB3 is MotorY")
						self.motorY = motor4
				elif (motor2is.strip() == "Y"):
					print("USB1 is MotorY")
					self.motorY = motor2
					if motor3is.strip() == "X":
						print("USB2 is MotorX")
						self.motorX = motor3
						self.ledMatrix = LEDMatrix(motor4.serialPort)
						print("USB3 is Matrix") 
					else: 
						self.ledMatrix = LEDMatrix(motor3.serialPort)
						print("USB2 is Matrix") 
						print("USB3 is MotorX")
						self.motorX = motor4
				else:
					print("USB1 is Unused")
					if motor3is.strip() == "Y":
						print("USB2 is MotorY")
						print("USB3 is MotorX")
						self.motorY = motor3
						self.motorX = motor4
					else: 
						print("USB2 is MotorX")
						print("USB3 is MotorY")
						self.motorX = motor3
						self.motorY = motor4		
			else:
				self.ledMatrix = LEDMatrix(motor1.serialPort)
				print("USB0 is Matrix") 
				if (motor2is.strip() == "X"):
					print("USB1 is MotorX")
					self.motorX = motor2
					if motor3is.strip() == "Y":
						print("USB2 is MotorY")
						print("USB3 is BT")
						self.motorY = motor3
						self.bt = Bluetooth(motor4.serialPort)
					else: 
						print("USB2 is BT")
						print("USB3 is MotorY")
						self.bt = Bluetooth(motor3.serialPort)
						self.motorY = motor4
				elif (motor2is.strip() == "Y"):
					print("USB1 is MotorY")
					self.motorY = motor2
					if motor3is.strip() == "X":
						print("USB2 is MotorX")
						self.motorX = motor3
						print("USB3 is BT")
						self.bt = Bluetooth(motor4.serialPort)
					else: 
						print("USB2 is BT")
						print("USB3 is MotorX")
						self.bt = Bluetooth(motor3.serialPort)
						self.motorX = motor4
				else:
					print("USB1 is BT")
					self.bt = Bluetooth(motor2.serialPort)
					if motor3is.strip() == "Y":
						print("USB2 is MotorY")
						print("USB3 is MotorX")
						self.motorY = motor3
						self.motorX = motor4
					else: 
						print("USB2 is MotorX")
						print("USB3 is MotorY")
						self.motorX = motor3
						self.motorY = motor4		
			print("USBs are set up")
			'''
			print(self.motorX)
			print(self.motorY)
			print(self.bt)
			'''
			
		self.magnet = Magnet(0)
		self.x = None  #need to initialize table before knowing 
		self.y = None
    	
	

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
		#self.motorXG.zero()
		#self.motorYG.zero()
		if (self.testing == 0):
			print("Zeroing!")
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
		print ("Table is initialized")
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
		'''
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
		'''
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
		'''
		self.motorXG.body.setFill('red')
		self.motorYG.body.setFill('red')
		'''
		#self.magnet.grab()
		print("Grabbing")


	'''
	Function: 		self.release()
	Description: 	This function will call magnet.release to turn off the magnet
	Paramaters: 	self (XYTable object)
	Return: 		none (Table is initialized and ready to be powered down)
	To-Do: 			delete graphics when ready

	'''	
	def release(self):
		'''
		self.motorXG.body.setFill('')
		self.motorYG.body.setFill('')
		'''
		print("Release")
		#self.magnet.release()
		
		 

