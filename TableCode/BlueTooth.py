import serial
from xytable import *

class Bluetooth:
	
	def __init__(self, sPort):
		print("Making Connection...")
		self.serialPort = sPort


	def waitformove(self):
		while (True):
			serialmsg = self.ser.readline().decode('UTF-8')
			#print("serial message: \n")
			#print(serialmsg)
			if ("z" in serialmsg):
				msgtemp = serialmsg.split('z')
				msg = msgtemp[0]
				print(msg)
				print("z in message")
				break
				
	def sendmove(self, move):
		self.serialPort.write(bytes("t" + move + "\n", 'UTF-8'))


