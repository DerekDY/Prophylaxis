import RPi.GPIO as GPIO

class ReedBoard:

	# assumes decoder for columns
	# parameters: number of columns, array of column pins, array of row pins
	# columnPins: from LEAST to MOST significant bits (for decoder)
	def __init__(self, columns, columnPins, rowPins):
		self.numRows = len(rowPins)
		self.numColumns = columns
		self.cPins = columnPins
		self.rPins = rowPins
		
		# initialize board to all zeros
		self.currentBoard = [[0 for x in range(self.numColumns)] for y in range(self.numRows)]
		
		# pin setup
		GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
		for cPin in self.cPins:
			GPIO.setup(cPin, GPIO.OUT)
		for rPin in self.rPins:
			GPIO.setup(rPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # internal pull-down resistor
			
	def testingInput(self, testArray):
		self.currentBoard = testArray

	#def updateBoard(self):

			
	def getBoard(self):
		# start testing at column 0
		cIdx = 0
		# loop until every column is tested
		while cIdx < self.numColumns:
			# send column code to one-hot decoder
			for i, cPin in enumerate(self.cPins):
				# use bitwise AND to set output column code
				if cIdx & (2 ** i):
					GPIO.output(cPin, GPIO.HIGH)
				else:
					GPIO.output(cPin, GPIO.LOW)
			# check which rows are high
			for rIdx, rPin in enumerate(self.rPins):
				if GPIO.input(rPin):
					#print "piece at", rIdx, cIdx
					self.currentBoard[rIdx][cIdx] = 1
				else:
					#print "no piece at", rIdx, cIdx
					self.currentBoard[rIdx][cIdx] = 0
			# increment to test next column
			cIdx += 1
			###
			# for testing
			#print(self.currentBoard)
			###
		return self.currentBoard
		
'''
	def printBoard(self):
		print ' ',
		for i in range(len(self.currentBoard[0])):
			print i,
		print
		for i, element in enumerate(self.currentBoard):
			print i,
			for item in element:
				print item,
			print
'''
