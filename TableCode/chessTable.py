from xytable import *
from Move import *

'''
Class: 			chessTable
Author: 		Derek De Young
Revision Date: 	10-14-15
Last revision:	
Description: 	This class encapsulates the xyTable into a chess table 		
Paramaters: 	self 
Return: 		and Chess table object
To-Do: 			
'''

#[P0 B0]
#[P1 B0]
#[P2 N0]
#[P3 N1]
#[P4 R0] 
#[P5 R1] 
#[P6 Q0] 
#[P7   ] 
#
B = 0
N = 2
R = 4
Q = 6

WHITE = True
BLACK = False

class ChessTable(XYTable):
	def __init__(self):
		self.motorX = Motor(0)
		self.motorY = Motor(1)
		self.magnet = Magnet(0)
		self.x = None  #need to initialize table before knowing 
		self.y = None
		self.win = GraphWin('XY Table Testing', 310, 210)
		self.board = "board" #from reed switches 
		self.lightsW = "lights"
		self.lightsB = "lights"
		#self.whiteCaptured = [[]]
		#self.blackCaptured = [[]]
		#self.boardRep = [[]]

	def goto(self, space, carrying):
		if carrying:
			x = None #fill with oobstruction code
		else:
			x = None # can go straight there 
		column = space[0]
		row = space[1]
		self.moveto(column, row)
		#print (str(column) + " & " + str(row))

	
	#def getCurrentBoard(self):	
		#fullboard = self.board.getboard()
		#self.boardrep = fullboard [2:8]
		#self.whitecaptured = fullboard [2:iiii]
		#self.blackcaptured = fullboard [2:iiii]

	






	def move(self, move):
		print ("Moving: " + str(move.piece))
		print()
		firstSpace = move.oldPos + C(2,0)
		#print "From: " + firstSpace
		secondSpace = move.newPos + C(2,0)
		#print "To: " + secondSpace
		captured = move.pieceToCapture
		if (captured):
			#if all crazy things
			print ("Captured: " + str(captured))
			print()
			letter = captured.stringRep
			number = captured.number
			if captured.side == WHITE:
				if letter == "p":
					capturedspace = C(0, number)
				elif letter == "R":
					capturedspace = C(1, R + number)
				elif letter == "N":
					capturedspace = C(1, N + number)
				elif letter == "Q":
					capturedspace = C(1, Q + number)
				elif letter == "B":
					capturedspace = C(1, B + number)
			else:
				if letter == "p":
					capturedspace = C(11, 7-number)
				elif letter == "R":
					capturedspace = C(10, 7-(R + number))
				elif letter == "N":
					capturedspace = C(10, 7-(N + number))
				elif letter == "Q":
					capturedspace = C(10, 7-(Q + number))
				elif letter == "B":
					capturedspace = C(10, 7-(B + number))
			self.goto(secondSpace, False)
			self.grab()
			self.goto(capturedspace, True)
			self.release()

		self.goto(firstSpace, False)
		self.grab()
		self.goto(secondSpace, True)
		self.release()
