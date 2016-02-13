from graphics import *
from random import randint
from time import sleep

class MotorG:

	def __init__(self, dir):
		#direction 0 is horizontal
		#direction 1 is vertical 
		self.direction = dir # replace direction with pin info
		#print ("This motor is made with direction: " + str(self.direction))
		if (self.direction == 1):
			initial = randint(5, 210-25)
			self.body = Rectangle(Point(5,initial), Point(505,initial+25))
		else:
			initial = randint(5, 310-25)
			self.body = Rectangle(Point(initial,5), Point(initial+25,405))
		
		
	def ccw(self, dist):
		for i in range(0, dist*25):  #pixels simulating an inch 
			if (self.direction == 0):
				self.body.move(1, 0)
			else:
				self.body.move(0, 1)
			sleep(.01)
			
			
	def cw(self, dist):
		for i in range(0, dist*25):
			if (self.direction == 0):
				self.body.move(-1, 0)
			else:
				self.body.move(0, -1)
			sleep(.01)
			
	def getCoord(self):
		if (self.direction == 0):
			coord = self.body.p1.x
		else:
			coord = self.body.p1.y
		return coord


	#todo a funtion that will zero a motor
	def zero(self):
		for i in range(0, self.getCoord()):  
			if (self.direction == 0):
				self.body.move(-1, 0)
			else:
				self.body.move(0, -1)
