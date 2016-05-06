from xytable import *
from Move import *
from InputParser import InputParser
from Coordinate import Coordinate as C
from reedBoard import *

####### for testmoves #########
#from reedBoard import *
###############################
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

inchesPerSpace = 2.25

WHITE = True
BLACK = False

class ChessTable(XYTable):  #testing on when 1
    def __init__(self, testingOption = 0):
        print("Making a chessTable")
        super(ChessTable, self).__init__(testingOption)
        self.row = 0
        self.column = 0
        self.whiteCaptured = [[0 for x in range(2)] for y in range(8)]
        self.blackCaptured = [[0 for x in range(2)] for y in range(8)]
        self.playableBoard = [[0 for x in range(8)] for y in range(8)]
        self.boardRep = [[]] 
        self.reedBoard = ReedBoard(12,[5,6,13,19],[24,25,8,7,12,16,20,21])

    def goto(self, space, carrying, offset):
        newColumn = space[0]
        correction = inchesPerSpace/8
        newRow = 7-space[1]
        dxAbs = abs(self.column - newColumn)
        dyAbs = abs(self.row - newRow)
        dx = self.column - newColumn
        dy = self.row - newRow
        if dy == 0:
           offsetY = -.5 if newRow > 6 else .5 
        else:
            offsetY = .5 if dy > 0 else -.5
        offsetX = -.5 if dx > 0 else .5
        correctionX = -correction if dx > 0 else correction
        correctionY = -correction if dy > 0 else correction
        #Moving on a diagonal
        if ((dxAbs == dyAbs or not carrying) and (not offset)):
            print("in if statement ----------------------------------->")
            if carrying:
                self.moveto(newColumn*inchesPerSpace + correctionX, newRow*inchesPerSpace + correctionY)
            self.moveto(newColumn*inchesPerSpace, newRow*inchesPerSpace)
        #Moving on lines
        elif (offset):
            print("in elif statement ----------------------------------->")
            self.moveto(self.x + (offsetX*inchesPerSpace) , self.y)	#move over .5 space in X
            self.moveto(self.x, (newRow*inchesPerSpace)+(offsetY*inchesPerSpace))	#move to .5 off space in Y
            if newColumn > 9:
                columnPosition = newColumn*inchesPerSpace + .2*inchesPerSpace
            elif newColumn < 2:
                columnPosition = newColumn*inchesPerSpace - .2*inchesPerSpace
            else:
                columnPosition = newColumn*inchesPerSpace
                
            self.moveto(columnPosition, self.y) #move to correct X
            self.moveto(columnPosition, newRow*inchesPerSpace + correctionY) #move to correct Y with correction
            self.moveto(columnPosition, newRow*inchesPerSpace)
                
		#Moving in Y then in X	
        else:
            print("in else statement ----------------------------------->")
            print(dx)
            if dx == 0:
                print("dx = 0 ---------------------------------------------->")
                self.moveto(self.x, newRow*inchesPerSpace + correctionY)
            self.moveto(self.x, newRow*inchesPerSpace)
            if dx != 0:
                print("dx != 0 ---------------------------------------------->")
                self.moveto(newColumn*inchesPerSpace + correctionX, self.y)
            self.moveto(newColumn*inchesPerSpace, self.y)
        #print (str(column) + " & " + str(row))
        self.row = newRow
        self.column = newColumn

    def splitBoard(self):
        fullBoard = self.boardRep #board from reed switches
        for i in range(8):
            for j in range(2):
                self.blackCaptured[i][j] = fullBoard[i][j]
                
        for i in range(8):
            for j in range(2):
                self.whiteCaptured[i][j] = fullBoard[i][j+10]
    
        for i in range(8):
            for j in range(8):
                self.playableBoard[i][j] = fullBoard[i][j+2] 
                
    def pieceInCaptureBin(self, captured):
        found = False
        if captured.side == BLACK:
            if captured.stringRep == "p":
                if self.blackCaptured[captured.number][0]== 1:
                    found = True
            elif captured.stringRep == "B":
                if self.blackCaptured[(B + captured.number)][1]== 1:
                    found = True
            elif captured.stringRep == "N":
                if self.blackCaptured[(N + captured.number)][1]== 1:
                    found = True
            elif captured.stringRep == "R":
                if self.blackCaptured[(R + captured.number)][1]== 1:
                    found = True
            elif captured.stringRep == "Q":
                if self.blackCaptured[(Q + captured.number)][1]== 1:
                    found = True
        else:
            if captured.stringRep == "p":
                if self.whiteCaptured[7-captured.number][1]== 1:
                    found = True    
            elif captured.stringRep == "B":
                if self.whiteCaptured[7-(B + captured.number)][0]== 1:
                    found = True
            elif captured.stringRep == "N":
                if self.whiteCaptured[7-(N + captured.number)][0]== 1:
                    found = True
            elif captured.stringRep == "R":
                if self.whiteCaptured[7-(R + captured.number)][0]== 1:
                    found = True
            elif captured.stringRep == "Q":
                if self.whiteCaptured[7-(Q + captured.number)][0]== 1:
                    found = True
        return found
    
    def updateBoard(self):
        self.boardRep = self.reedBoard.getBoard()
        self.splitBoard()
        
                
    def getMove(self, board):
        self.updateBoard()
        update = self.playableBoard
        whiteCaptured = self.whiteCaptured
        blackCaptured = self.blackCaptured
        moveMade = None
        moveTo = []
        moveFrom= []
        
        engineBoard = [[0 for x in range(8)] for y in range(8)]
        for p in board.pieces:
            #print(p.position)
            engineBoard[7 - p.position[1]][p.position[0]] = 1   #engine boards sides were flipped from the engine board
        
        #check for changes and then assign the position that was moved to and moved from
        complexMove = False
        for i in range(8):
            for j in range(8):
                if engineBoard[i][j] != update[i][j]:
                    if update[i][j] == 1:
                        moveTo.append(C(j,7-i))
                    else:
                        moveFrom.append(C(j,7-i))
        print(moveFrom)
        print(moveTo)
        #Check if there is an error
        if len(moveTo) > 2 or len(moveFrom) > 2:
            print("To Many Moves")
            return [None, 1]
        else:
            #special moves
            if len(moveFrom) == 2:
                piece1 = board.pieceAtPosition(moveFrom[0])
                piece2 = board.pieceAtPosition(moveFrom[1])
                king = None
                pawn1 = None
                print("Special Move")
                if piece1.stringRep == "K":
                    king = piece1
                    if piece2.stringRep == "R":
                        rook = piece2
                elif piece1.stringRep == "R":
                    rook = piece1
                    if piece2.stringRep == "K":
                        king = piece2
                elif piece1.stringRep == "p":
                    if piece2.stringRep == "p":
                        if piece1.side == board.currentSide:
                            pawn1 = piece1
                            pawn2 = piece2
                        else:
                            pawn1 = piece2
                            pawn2 = piece1
                else:
                    print("Could not find Special Move")
                    
                if king:
                    for move in king.getPossibleMoves():
                        if move.queensideCastle or move.kingsideCastle:
                            print("It is a castle move")
                            if rook == move.rookMove.piece:
                                print("rookMove is the rook")
                                moveMade = move
                            #this is redundent 
                            elif rook == move.specialMovePiece:
                                print("special move piece found")
                                moveMade = move
                            else:
                                print("Couldnt Find it")
                                
                        if moveMade:
                            return [moveMade, 0]
                            break
                            
                if pawn1 and pawn2:
                    print("It is a en pessant")
                    for move in pawn1.getPossibleMoves():
                        if move.pessant: 
                            if pawn2 == move.pieceToCapture:
                                if self.pieceInCaptureBin(pawn2):
                                    moveMade = move
                        else:
                            moveMade = None
                        if moveMade:
                            return [moveMade, 0]
                            break
                
            #normal moves
            elif len(moveFrom) == 1:
                print("Normal Move")
                piece = board.pieceAtPosition(moveFrom[0])
                print(piece)
                for move in piece.getPossibleMoves():
                    #check if it is a capture 
                    if len(moveTo) == 0:
                        if move.pieceToCapture:
                            captured = move.pieceToCapture
                            if self.pieceInCaptureBin(captured):
                                moveMade = move
                        #something broke
                        else:
                            moveMade = None
                                
                    #simple move
                    else:
                        if move.newPos == moveTo[0]:
                            moveMade = move
                        
                    if moveMade:
                        return [moveMade, 0]
                        break
                
                
            else:
                print("Piece Not Moved")
                return [None, 2]
        piece1 = board.pieceAtPosition(moveFrom[0])
        return [None, 3]
        print("*******************************")
    
    



    def move(self, move, ledMatrix = None, alphaPos = None):
        #print("MADE IT TO MOVE IN TABLE")
        #print ("Moving: " + str(move.piece))
        print()
        firstSpace = move.oldPos + C(2,0)
        #print ("From: " + str(firstSpace[0]) + "," + str(firstSpace[1]))
        secondSpace = move.newPos + C(2,0)
        #print ("To: " + str(secondSpace[0]) + "," + str(secondSpace[1]))
        captured = move.pieceToCapture
        if (captured): 
            if ledMatrix:
                ledMatrix.sendString("capture" + str(move.pieceToCapture.stringRep).lower())   #New Code
            
            #if all crazy things
            print ("Captured: " + str(captured))
            print()
            letter = captured.stringRep
            number = captured.number
            if captured.side == BLACK:
                if letter == "p":
                    capturedspace = C(0, 7-number)
                elif letter == "R":
                    capturedspace = C(1, 7-(R + number))
                elif letter == "N":
                    capturedspace = C(1, 7-(N + number))
                elif letter == "Q":
                    capturedspace = C(1, 7-(Q + number))
                elif letter == "B":
                    capturedspace = C(1, 7-(B + number))
            else:
                if letter == "p":
                    capturedspace = C(11, number)
                elif letter == "R":
                    capturedspace = C(10,(R + number))
                elif letter == "N":
                    capturedspace = C(10,(N + number))
                elif letter == "Q":
                    capturedspace = C(10,(Q + number))
                elif letter == "B":
                    capturedspace = C(10,(B + number))
            if move.pessant:
                print(move.pieceToCapture.position)
                if move.piece.side == WHITE:
                    self.goto(move.newPos + C(2,-1), False, False)
                else:
                    self.goto(move.newPos + C(2,1), False, False)
            else:
                self.goto(secondSpace, False, False)
            self.grab()
            self.goto(capturedspace, True, True)
            self.release()
            
        if ledMatrix:
            ledMatrix.sendString("move" + str(move.piece.stringRep).lower() + str(alphaPos).upper())   #New Code
        
        if(move.piece.stringRep == 'N'):
            self.goto(firstSpace, False, False)
            self.grab()
            self.goto(secondSpace, True, True)
            self.release()
        else:
            self.goto(firstSpace, False, False)
            self.grab()
            self.goto(secondSpace, True, False)
            self.release()
            if move.kingsideCastle or move.queensideCastle:
                rookStart = move.rookMove.oldPos + C(2,0)
                rookEnd = move.rookMove.newPos + C(2,0)
                self.goto(rookStart, False, False)
                self.grab()
                self.goto(rookEnd, True, True)
                self.release()
                
