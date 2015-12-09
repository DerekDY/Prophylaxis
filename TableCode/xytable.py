from motor import *
from motor1 import *  #real motor
from magnet import *
from Coordinate import Coordinate as C
import multiprocessing as mp

'''
Class: 			XYTable
Author: 		Derek De Young
Revision Date: 	9-28-15
Last revision:	
Description: 	This class encapsulates the 2 motors and magnets of the 
				XY table into one class				
Paramaters: 	self (XYTable object)
Return: 		and XY Table Object
To-Do: 			delete graphics objects
'''

class XYTable:

	def __init__(self):
		self.motorXG = MotorG(0)
		self.motorYG = MotorG(1)
		self.motorX = Motor(21,16,20)
		self.motorY = Motor(26,19,13)
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
		#leaving a 5 pixel boarder 
		#processes = [mp.Process(target=self.motorXG.zero, args=()),mp.Process(target=self.motorY.zero, args=())]
		#start multiprocessing
		#for p in processes:
		#	p.start()
		#end mulitprocessing
		#for p in processes:
		#	p.join()
		self.motorXG.zero()
		self.motorYG.zero()
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
		if (dx < 0):
			self.motorXG.cw(abs(dx))
			self.motorX.cw(abs(dx))
		else:
			self.motorXG.ccw(abs(dx))
			self.motorX.ccw(abs(dx))
		if (dy < 0):
			self.motorYG.cw(abs(dy))
			self.motorY.cw(abs(dy))
		else:
			self.motorYG.ccw(abs(dy))
			self.motorY.ccw(abs(dy))
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
		
		 
	