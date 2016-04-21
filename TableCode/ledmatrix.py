import serial
from xytable import *

class LEDMatrix:
	
    def __init__(self, sPort):
        print("Making Connection...")
        self.serialPort = sPort
    
				
    def sendString(self, string):
        #print("Serial Port")
        #print(self.serialPort)		
        self.serialPort.write(bytes(string + "\n", 'UTF-8'))
	
    def sendMultLines(self, stringTop, stringBot):
        #print("Serial Port")
        #print(self.serialPort)		
        self.serialPort.write(bytes(stringTop + '&' + stringBot + "\n", 'UTF-8'))
				
    def who(self):
        #print("Telling them who I am")
        self.serialPort.write(bytes("who\n", 'UTF-8'))
        return self.serialPort.readline().decode('UTF-8')


