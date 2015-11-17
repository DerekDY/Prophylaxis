from xytable import *
from Move import *
from reedBoard import *

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
        self.reedBoard = ReedBoard(0)
        self.x = None  #need to initialize table before knowing 
        self.y = None
        self.win = GraphWin('XY Table Testing', 310, 210)
        self.lightsW = "lights"
        self.lightsB = "lights"
        self.whiteCaptured = [[0 for x in range(2)] for y in range(8)]
        self.blackCaptured = [[0 for x in range(2)] for y in range(8)]
        self.playableBoard = [[0 for x in range(8)] for y in range(8)]
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

    def splitBoard(self):
        fullBoard = self.reedBoard.getBoard() #board from reed switches
        for i in range(8):
            for j in range(2):
                self.whiteCaptured[i][j] = fullBoard[i][j]
                
        for i in range(8):
            for j in range(2):
                self.blackCaptured[i][j] = fullBoard[i][j+10]
    
        for i in range(8):
            for j in range(8):
                self.playableBoard[i][j] = fullBoard[i][j+2] 
    
    def getMove(self, board):
        self.splitBoard()
        update = self.playableBoard
        whiteCaptured = self.whiteCaptured
        blackCaptured = self.blackCaptured
        changes = []
        legalMoves = []
        moveTo = []
        moveFrom = []
        moveMade = []
        caploc = []
        
        #create board code which should be put inside of the board class most likely
        #it converts the engine's board into 1's and 0's
        #tempBoard = Board()
        
        engineBoard = [[0 for x in range(8)] for y in range(8)]
        for p in board.pieces:
            #print(p.position)
            engineBoard[7 - p.position[1]][p.position[0]] = 1   #engine boards sides were flipped from the engine board
        '''
        print()
        print("Engine Board: \n")
        for i in range(8):
            print(engineBoard[i])
        print()
        
        print("Updated Board: \n")
        for i in range(8):
            print(update[i])
        print()
        '''
        
        #check for changes and then assign the position that was moved to and moved from
        for i in range(8):
            for j in range(8):
                if engineBoard[i][j] != update[i][j]:
                    #changes.extend([chr(j + ord('A')) + str(i)])    #for testing purposes
                    if update[i][j] == 1:
                        moveTo.extend([i,j])
                    else:
                        moveFrom.extend([i,j])
        
        #go through all of the pieces of the original engine board
        for p in board.pieces:
            #find piece that correlates to the position that the piece was moved from
            if p.position[0] == moveFrom[1] and p.position[1] == moveFrom[0]:   #reverse indexing
                print("Test1: \n")
                for move in p.getPossibleMoves():
                    if move.pieceToCapture != None:     #move includes the capturing of a piece
                        print("Captured Piece \n")
                        print(move.pieceToCapture)
                        #check for piece capture
                        for i in range(8):
                            for j in range(2):
                                if whiteCaptured[i][j] == 1:
                                    caploc = ['white',i,j]                               
                                elif blackCaptured[i][j] == 1:
                                    caploc = ['black',i,j]
                                print(caploc)   #for testing purposes
                    else:
                        print("No Piece to Capture")
                        #if no pieces were captured then find which moves new position lines up with the position
                        #that the piece was moved to
                        if moveTo[1] == move.newPos[0] and moveTo[0] == move.newPos[1]:
                            moveMade = move

        print("\nMove Made: \n")                   
        return moveMade



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
