import serial
from xytable import *

class Bluetooth:
	
	def __init__(self, sPort):
		print("Making Connection...")
		#self.sPort = sPort
		#self.serialPort = serial.Serial('/dev/ttyUSB' + str(sPort), 9600)
		self.serialPort = sPort
	
	def deciferMove(self,msg):
		pos = str(msg)
		#print("decifering move...")
		#print(pos)
		
		#num to alpha conversion
		#add one to num coord to fix y positions
		numPos = str(int(pos[1]) + 1)
		if pos[0] == '0':
			pos = 'a' + numPos
		elif pos[0] == '1':
			pos = 'b' + numPos
		elif pos[0] == '2':
			pos = 'c' + numPos
		elif pos[0] == '3':
			pos = 'd' + numPos
		elif pos[0] == '4':
			pos = 'e' + numPos
		elif pos[0] == '5':
			pos = 'f' + numPos
		elif pos[0] == '6':
			pos = 'g' + numPos                    
		elif pos[0] == '7':
			pos = 'h' + numPos
		#print(pos)
		return pos
	
	def waitformove(self):
		while(True):
			print("Waiting for Move...")
			print(self.serialPort)
			serialmsg = self.serialPort.readline().decode('UTF-8')
			print("serial message: \n")
			print(serialmsg)

			if ("#" in serialmsg):
				msgtemp = serialmsg.split('#')
				msg = msgtemp[0]
				print("# in message")
				print(msg)
				break
		startPos = self.deciferMove(msg[0:2])
		endPos = self.deciferMove(msg[2:4])
		msg = startPos + endPos
		print(msg)
		return msg
				
	def sendmove(self, move):
		print("Serial Port")
		print(self.serialPort)	
		#self.serialPort.write(bytes("testString", 'UTF-8'))	
		self.serialPort.write(bytes("t" + move, 'UTF-8'))
		
	def who(self):
		#print("Telling them who I am")
		self.serialPort.write(bytes("who\n", 'UTF-8'))
		return self.serialPort.readline().decode('UTF-8')


