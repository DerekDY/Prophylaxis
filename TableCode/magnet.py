from graphics import *

class Magnet:

	def __init__(self, pin):
		#direction 0 is horizontal
		#direction 1 is vertical
		self.pinout = pin
		self.grab = 0
		#print ("Magnet is created")
		
		# pin setup
		GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
		GPIO.setup(self.pinout, GPIO.OUT)
		
	def grab():
		GPIO.output(self.pinout, GPIO.HIGH)
		self.grab = 1
		#print ("Magnet is grabbing")
		
	def release():
		GPIO.output(self.pinout, GPIO.LOW)
		self.grab = 0
		#print ("Magnet is released")