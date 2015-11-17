from graphics import *

class Magnet:

	def __init__(self, pin):
		#direction 0 is horizontal
		#direction 1 is vertical 
		self.pinout = pin 
		self.grab = 0
		print ("This magnet is made")
		
	def grab():
		self.grab = 1
		print ("Magnet is grabbing")
		
	def release():
		self.grab = 0
		print ("Magnet is released")