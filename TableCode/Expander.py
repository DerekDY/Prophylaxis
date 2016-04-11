from MCP23017_I2C import *

## This class is to be used just like GPIO
## Pins are 0-15

##   TOP
## 0 --- 15
## 1 --- 14
## 2 --- 13
## 3 --- 12
## 4 --- 11
## 5 --- 10
## 6 --- 9
## 7 --- 8
## X --- X
## X --- X
## X --- X
## X --- X
## OTHER PINS

# invoke
# expander = Expander(address)
#		#The address should be in HEX

# setup
# expander.setup(pinNumber, pinMode)
#	#pinMode should be 'IN' or 'OUT'

# read an input
# x = expander.input(pinNumber)
# x will now read 1 or 0 (HIGH or LOW)

# set an output
# x = expander.output(pinNumber, outputHigh_Low)
# outputHigh_Low should be 'HIGH' or 'LOW', anything not 'HIGH' will be considered 'LOW'

def getPinData(pinNumber):
	if pinNumber < 8:
		letter = 'A'
	else:
		letter = 'B'
	pinNumber = pinNumber % 8
	return (pinNumber, letter)

class Expander:
	
	def __init__(self, address):
		self.chip = GPIO_CHIP(address, 1)

	def setup(self, pinNumber, in_out):
		letNum = getPinData(pinNumber)
		#print(letNum[0])
		#print(letNum[1])
		#print(in_out)
		self.chip.setup(letNum[0], in_out, letNum[1]) 

	def input(self, pinNumber):
		letNum = getPinData(pinNumber)
		return self.chip.input(letNum[0], letNum[1])

	def output(self, pinNumber, hi_low):
		letNum = getPinData(pinNumber)
		if (hi_low == 'HIGH'):
			hi_low = 1
		else:
			hi_low = 0
		self.chip.output(letNum[0], hi_low, letNum[1])  