from xytable import *
from Move import *
from InputParser import InputParser

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
        ####### for testmoves #########
        #self.reedBoard = ReedBoard(0)
        ###############################
        self.row = 0
        self.column = 0
        #self.win = GraphWin('XY Table Testing', 310, 210)
        self.lightsW = "lights"
        self.lightsB = "lights"
        self.whiteCaptured = [[0 for x in range(2)] for y in range(8)]
        self.blackCaptured = [[0 for x in range(2)] for y in range(8)]
        self.playableBoard = [[0 for x in range(8)] for y in range(8)]
		#self.boardRep = [[]] 

    def goto(self, space, carrying, offset):
        newColumn = space[0]
        newRow = 7-space[1]
        dx = abs(self.column - newColumn)
        dy = abs(self.row - newRow)
        offsetX = .5 if dx > 1 else -.5
        offsetY = -.5 if dy > 1 else .5
        #Moving on a diagonal
        if (dx == dy or not carrying or not offset):
                self.moveto(newColumn*inchesPerSpace, newRow*inchesPerSpace)
        #Moving on lines
        elif (offset):
		        self.moveto(self.x + (offsetX*inchesPerSpace) , self.y)	#move over .5 space in X
		        self.moveto(self.x, (newRow*inchesPerSpace)+(offsetY*inchesPerSpace))	#move to .5 off space in Y
		        self.moveto(newColumn*inchesPerSpace, self.y) #move to correct X
		        self.moveto(self.x, newRow*inchesPerSpace) #move to correct Y 
		#Moving in Y then in X	
        else:
                self.moveto(self.x, newRow*inchesPerSpace)
                self.moveto(newColumn*inchesPerSpace, self.y)
        #print (str(column) + " & " + str(row))
        self.row = newRow
        self.column = newColumn

    def splitBoard(self, currentBoard):
        fullBoard = currentBoard #board from reed switches
        for i in range(8):
            for j in range(2):
                self.whiteCaptured[i][j] = fullBoard[i][j]
                
        for i in range(8):
            for j in range(2):
                self.blackCaptured[i][j] = fullBoard[i][j+10]
    
        for i in range(8):
            for j in range(8):
                self.playableBoard[i][j] = fullBoard[i][j+2] 
    
    
    def getMove(self, board, currentBoard):
        self.splitBoard(currentBoard)
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
        
        #check for changes and then assign the position that was moved to and moved from
        for i in range(8):
            for j in range(8):
                if engineBoard[i][j] != update[i][j]:
                    if update[i][j] == 1:
                        moveTo.extend([j,7-i])
                    else:
                        moveFrom.extend([j,7-i])
        
        
        print(moveTo)
        #go through all of the pieces of the original engine board
        for p in board.pieces:
            #find piece that correlates to the position that the piece was moved from
            if p.position[0] == moveFrom[0] and p.position[1] == moveFrom[1]:   #reverse indexing
                print("position of moved piece: ")
                print(p.position)
                

                #the string rep notation may be wrong with upper-case letters???
                #had to switch it to lower-case to make the pawn notation work
                #notation seems like only pawns are lower-case
                #saw this in Board code
                
                for move in p.getPossibleMoves():
                    #print("move: ")
                    #print(move)
                    if move.pieceToCapture:     #move includes the capturing of a piece
                        print("Captured Piece \n")
                        print(move.pieceToCapture)
                        captured = move.pieceToCapture
                        #check for piece capture
                        print(blackCaptured)
                        print(whiteCaptured)
                        #print(blackCaptured[0][0])
                        if captured.side == WHITE:
                            print("white captured side")
                            if captured.stringRep == "p":
                                print(captured.number)
                                if whiteCaptured[captured.number][0]== 1:
                                    print("test")
                                    moveMade = move
                                    print("pawn captured")
                            elif captured.stringRep == "B":
                                if whiteCaptured[B + captured.number][1]== 1:
                                    moveMade = move
                            elif captured.stringRep == "N":
                                print(whiteCaptured[3])
                                if whiteCaptured[N + captured.number][1]== 1:
                                    moveMade = move
                                    print("knight captured")
                            elif captured.stringRep == "R":
                                if whiteCaptured[R + captured.number][1]== 1:
                                    moveMade = move
                            elif captured.stringRep == "Q":
                                if whiteCaptured[Q + captured.number][1]== 1:
                                    moveMade = move
                        else:
                            print("black captured side")
                            print(captured.number)
                            if captured.stringRep == "p":
                                if blackCaptured[captured.number][1]== 1:
                                    moveMade = move    
                            elif captured.stringRep == "B":
                                if blackCaptured[B + captured.number][0]== 1:
                                    moveMade = move
                            elif captured.stringRep == "N":
                                if blackCaptured[N + captured.number][0]== 1:
                                    moveMade = move
                            elif captured.stringRep == "R":
                                if blackCaptured[R + captured.number][0]== 1:
                                    moveMade = move
                            elif captured.stringRep == "Q":
                                if blackCaptured[Q + captured.number][0]== 1:
                                    moveMade = move

                                #print(caploc)   #for testing purposes
                    else:
                        #print("No Piece to Capture")
                        #if no pieces were captured then find which moves new position lines up with the position
                        #that the piece was moved to
                        #print("move to: ")
                        #print(moveTo)
                        #print(move.newPos)
                        if move.queensidecastle
                        if len(moveTo) != 0:
                            #castle moves
                            if len(moveTo) == 4:
                                print("multiple moves")
                                print(moveTo)
                                print(move.newPos[0:2])
                                #black castle queen side
                                if moveTo[0:2] == [2,7] and move.newPos[0:2] == (2,7):
                                    print("black queen side castle was made")
                                    print(move)
                                    print(move.piece.side)
                                    side = move.piece.side
                                    parser = InputParser(board, side)
                                    moveMade = parser.moveForShortNotation("0-0-0")
                                #black castle king side
                                if moveTo[0:2] == [5,7] and move.newPos[0:2] == (6,7):
                                    print("black king side castle was made")
                                    print(move)
                                    print(move.piece.side)
                                    side = move.piece.side
                                    parser = InputParser(board, side)
                                    moveMade = parser.moveForShortNotation("O-O")
                                #white castle queen side
                                if moveTo[0:2] == [2,0] and move.newPos[0:2] == (3,0):
                                    print("white queen side castle was made")
                                    print(move)
                                    print(move.piece.side)
                                    side = move.piece.side
                                    parser = InputParser(board, side)
                                    moveMade = parser.moveForShortNotation("Ka1")
                                    print(moveMade)
                                    moveMade = parser.moveForShortNotation("Kb1")
                                    print(moveMade)
                                    moveMade = parser.moveForShortNotation("0-0")
                                    print(moveMade)
                                    moveMade = parser.moveForShortNotation("0-0-0")
                                    print(moveMade)
                                #white castle king side
                                if moveTo[0:2] == [5,0] and move.newPos[0:2] == (6,0):
                                    print("white king side castle was made")
                                    print(move)
                                    print(move.piece.side)
                                    side = move.piece.side
                                    parser = InputParser(board, side)
                                    moveMade = parser.moveForShortNotation("O-O")
                                #else:
                                #    print("none of the if statements were true")
                            else:
                                if move.promotion:
                                    print("promotion move")
                                    moveMade = move

                                else:
                                    if moveTo[0] == move.newPos[0] and moveTo[1] == move.newPos[1]:
                                        moveMade = move
                                '''
                                if move.piece.stringRep == 'p':
                                    print("piece is a pawn")
                                    print(move.newPos)
                                    if move.newPos[1] == 0:
                                        print("promotion")
                                        moveMade = move
                                        #need to add code here
                                    else:
                                        if moveTo[0] == move.newPos[0] and moveTo[1] == move.newPos[1]:
                                            moveMade = move
                                '''
                                
                                '''
                                print(blackCaptured)
                                print(whiteCaptured)
                                for i in range(8):
                                    if blackCaptured[i][0] == 1:
                                        print("white pawn captured via en passant")
                                        
                                        print(move.piece.position[0]) 
                                        pawnX = move.piece.position[0]
                                        pawnXalpha = chr(97 + pawnX)
                                        print(pawnXalpha)
                                        
                                        side = move.piece.side
                                        parser = InputParser(board, side)
                                        
                                        #piece to capture on right
                                        fullString = str(pawnXalpha + "x" + chr(97 + pawnX + 1) + str(move.piece.position[1]))
                                        print("full string: ")
                                        print(fullString)
                                        
                                        moveMade = parser.moveForShortNotation(fullString)                                        
                                '''

                                    
                            '''
                            if move.piece.stringRep == 'R' or move.piece.stringRep == 'K': #maybe get rid of king statmenet
                                #deal with castling 
                                print("castling")
                                print(move.piece)
                                print(move.newPos[0]) #0
                                print(move.newPos[1]) #4
                                if move.newPos[0] == 0 and move.newPos[1] == 4:
                                    print("rook moved to castling position")
                                    tempSide = move.piece.side
                                    for p in board.pieces:
                                        if p.stringRep == 'K' and p.side == tempSide:
                                            print("found king after rook")
                                            print(p.position[0:2])
                                            
                                            #need to get move to position not starting position
                                            #maybe got position from default board and need it from reed board
                                            #if p.position[0] == 0 and p.position[1] == 5:
                                            #    print("castle was made")
                                            
                                            for move in p.getPossibleMoves():
                                                print("new position move")
                                                print(move.newPos[0:2])
                                                if move.newPos[0] == 0 and move.newPos[1] == 5:
                                                    print("castle was made")
                                            
                            ''' 
                                    
        
        print("Move Made: ")  
        print(moveMade)
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
            self.goto(secondSpace, False, False)
            self.grab()
            self.goto(capturedspace, True, True)
            self.release()
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
