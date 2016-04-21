#language:Python
# External module imports

import time
import serial
steps = 2000
rotationPerInch = 1272/2000  #every 4th number can be multiplied by 2.25 and be whole

class Motor:

	def __init__(self, usb):
		#clk is the number of the clock pin
		#dir is the number of the direction pin
		#usb is the number of the USB identifier found in the '/dev/ttyUSB#' string
		#XY is the orientation of the motor
		#print("Now I'm actually making a motor")
		self.connected = True
		try:
			self.serialPort = serial.Serial('/dev/ttyUSB' + str(usb), 9600)
		except:
			print("USB"+str(usb)+" Is not connected")
			self.connected = False
		#print("The serial connection was made")
		#time.sleep(1.5)
		self.usb = usb

	def waitfordone(self):
		while (True):
			serialmsg = self.serialPort.readline().decode('UTF-8')
			#print(serialmsg)
			if ("Done" in serialmsg):
				return 0 # no error
			elif ("Zero Error" in serialmsg):
				return 1 #error

	def move(self, distance):
		fb = "f" if (distance > 0) else "b"
		#print("I MOVED THE CRAP OUT OF THAT PIECE")
		self.serialPort.write(bytes(fb+str(abs(distance*steps*rotationPerInch))+"\n", 'UTF-8'))
		if (self.waitfordone() == 1):
			print("Error - Reseting Table")
			zero()
			
	def zero(self):
		#print("Zeroing")
		self.serialPort.write(bytes("zero\n", 'UTF-8'))
		self.waitfordone()

	def who(self):
		#print("Telling them who I am")
		self.serialPort.write(bytes("who\n", 'UTF-8'))
		return self.serialPort.readline().decode('UTF-8')



	
