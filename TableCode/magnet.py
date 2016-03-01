import RPi.GPIO as GPIO

class Magnet:
	def __init__(self, pin):
		self.pinout = pin
		#self.grab = 0
		#print ("Magnet is created")
		# pin setup
		GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
		GPIO.setup(self.pinout, GPIO.OUT)
		
	def grab(self):
		GPIO.output(self.pinout, GPIO.HIGH)
		#self.grab = 1
		#print ("Magnet is grabbing")
		
	def release(self):
		GPIO.output(self.pinout, GPIO.LOW)
		#self.grab = 0
		#print ("Magnet is released")
