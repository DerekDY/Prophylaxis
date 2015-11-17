from motor import *
from magnet import *
from Coordinate import Coordinate as C

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
		self.motorX = Motor(0)
		self.motorY = Motor(1)
		self.magnet = Magnet(0)
		self.x = None  #need to initialize table before knowing 
		self.y = None
    	

	'''
	Function: 		self.drawMotors()
	Author: 		Derek De Young
	Revision Date: 	9-28-15
	Last revision: 
	Description: 	This function will be removed in the actual version
					it is using graphics.py to give a visual representative
	Paramaters: 	self (XYTable object)
	Return: 		graphics are drawn
	To-Do: 			delete when move over 
	'''
	def drawMotors(self):
		self.motorX.body.draw(self.win)
		self.motorY.body.draw(self.win)
	
	
	'''
	Function: 		self.initialize_Coord()
	Author: 		Derek De Young
	Revision Date: 	9-28-15
	Last revision: 
	Description: 	This function must be called to initialize the table at 0,0
	Paramaters: 	self (XYTable object)
	Return: 		none (Table is initialized
	To-Do: 			multi treading instead of every other
	
	'''
	def initialize_Coord(self):
		#leaving a 5 pixel boarder 
		self.motorX.zero()
		self.motorY.zero()
		#initialize the coordinates	
		self.x = 0
		self.y = 0
		print ("Table is initialized")
		print ("Coordinates are: " + str(self.x) + ", " + str(self.y))
	
	
	
	'''
	Function: 		self.turnoff()
	Author: 		Derek De Young
	Revision Date: 	9-28-15
	Last revision: 
	Description: 	This function must be called to power off the board and
					set the motors back to 0,0 				
	Paramaters: 	self (XYTable object)
	Return: 		none (Table is initialized and ready to be powered down)
	To-Do: 			Finish method
	
	'''
	def turnoff(self):
		self.win = None
		
	
	
	'''
	Function: 		self.moveto()
	Author: 		Derek De Young
	Revision Date: 	9-28-15
	Last revision: 
	Description: 	This function is called to move the table to a point on 
					the coordinate system 
	Paramaters: 	new_x and new_y both int for new coordinate point 
	Return: 		none (Motors are moved to new location)
	To-Do: 			Finish method
	
	'''	
	def moveto(self, new_x, new_y):
		dx = new_x - self.x
		dy = new_y - self.y 
		if (dx < 0):
			self.motorX.cw(abs(dx))
		else:
			self.motorX.ccw(abs(dx))
		if (dy < 0):
			self.motorY.cw(abs(dy))
		else:
			self.motorY.ccw(abs(dy))
		self.x = new_x
		self.y = new_y
		print ("Coordinates are: " + str(self.x) + ", " + str(self.y))
	
	
	'''
	Function: 		self.grab()
	Author: 		Derek De Young
	Revision Date: 	9-28-15
	Last revision: 
	Description: 	This function will call magnet.grab to turn on the magnet  				
	Paramaters: 	self (XYTable object)
	Return: 		none (magnet is turned on)
	To-Do: 			delete graphics when ready 
	
	'''	
	def grab(self):
		self.motorX.body.setFill('red')
		self.motorY.body.setFill('red')
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
		self.motorX.body.setFill('')
		self.motorY.body.setFill('')
		#self.magnet.release()
		
		 
	