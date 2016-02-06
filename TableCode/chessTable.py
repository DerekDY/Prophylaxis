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

class ChessTable(XYTable):  #testing on when 1
    def __init__(self, testingOption = 0):
        print("I'm making a chessTable")
        super(ChessTable, self).__init__(testingOption)
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
        #print("MADE IT TO GOTO IN TABLE")
        column = space[0]
        #print(column)
        row = 7-space[1]
        #print(row)
        dx = abs(self.x - column)
        dy = abs(self.y - row)
        if (dx == dy or not carrying):
                self.moveto(column, row)
        else:
                self.moveto(self.x, row)
                self.moveto(column, self.y)
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
        
        
        print()
        print("Engine Board: \n")
        for i in range(8):
            print(engineBoard[i])
        print()
        
        print("Updated Board: \n")
        for i in range(8):
            print(update[i])
        print()
        
        
        #check for changes and then assign the position that was moved to and moved from
        for i in range(8):
            for j in range(8):
                if engineBoard[i][j] != update[i][j]:
                    if update[i][j] == 1:
                        moveTo.extend([j,7-i])
                    else:
                        moveFrom.extend([j,7-i])
        
        #go through all of the pieces of the original engine board
        for p in board.pieces:
            #find piece that correlates to the position that the piece was moved from
            if p.position[0] == moveFrom[0] and p.position[1] == moveFrom[1]:   #reverse indexing
                print(p.position)
                for move in p.getPossibleMoves():
                    print(move)
                    if move.pieceToCapture:     #move includes the capturing of a piece
                        print("Captured Piece \n")
                        print(move.pieceToCapture)
                        captured = move.pieceToCapture
                        #check for piece capture
                        print(blackCaptured)
                        print(whiteCaptured)
                        print(blackCaptured[0][0])
                        if captured.side == WHITE:
                            if captured.stringRep == "P":
                                if whiteCaptured[7 - captured.number][0]== 1:
                                    moveMade = move
                            elif captured.stringRep == "B":
                                if whiteCaptured[7 - B + captured.number][1]== 1:
                                    moveMade = move
                            elif captured.stringRep == "N":
                                if whiteCaptured[7 - N + captured.number][1]== 1:
                                    moveMade = move
                            elif captured.stringRep == "R":
                                if whiteCaptured[7 - R + captured.number][1]== 1:
                                    moveMade = move
                            elif captured.stringRep == "Q":
                                if whiteCaptured[7 - Q + captured.number][1]== 1:
                                    moveMade = move
                        else:
                            if captured.stringRep == "P":
                                if blackCaptured[captured.number][1]== 1:
                                    moveMade = move
                            elif captured.stringRep == "B":
                                if blackCaptured[B - captured.number][0]== 1:
                                    moveMade = move
                            elif captured.stringRep == "N":
                                if blackCaptured[N - captured.number][0]== 1:
                                    moveMade = move
                            elif captured.stringRep == "R":
                                if blackCaptured[R - captured.number][0]== 1:
                                    moveMade = move
                            elif captured.stringRep == "Q":
                                if blackCaptured[Q - captured.number][0]== 1:
                                    moveMade = move

                                #print(caploc)   #for testing purposes
                    else:
                        print("No Piece to Capture")
                        #if no pieces were captured then find which moves new position lines up with the position
                        #that the piece was moved to
                        print(moveTo)
                        print(move.newPos)
                        if len(moveTo) != 0:
                            #if move.piece.stringRep == 'R' or move.piece.stringRep == 'K':
                                #deal with castling 
                            #else:
                            if moveTo[0] == move.newPos[0] and moveTo[1] == move.newPos[1]:
                                moveMade = move
                                    
        print("\nMove Made: ")                   
        return moveMade



    def move(self, move):
        #print("MADE IT TO MOVE IN TABLE")
        #print ("Moving: " + str(move.piece))
        print()
        firstSpace = move.oldPos + C(2,0)
        #print ("From: " + str(firstSpace[0]) + "," + str(firstSpace[1]))
        secondSpace = move.newPos + C(2,0)
        #print ("To: " + str(secondSpace[0]) + "," + str(secondSpace[1]))
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
