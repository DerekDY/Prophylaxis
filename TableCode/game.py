from Board import Board
from InputParser import InputParser
from AI import AI
import chess.uci
import time
from chessTable import *
import sys
import random
#from Buttons import *
#from BlueTooth import *

WHITE = True
BLACK = False


class Game:
    def __init__(self, testingOptions = 0, btOption = 0, gameMode = 1, voiceControl = 0): #1 for use without motors
        self.board = Board()
        self.uciBoard = chess.Board()
        #self.uciBoard = chess.Board(chess960 = True)
        self.table = ChessTable(testingOptions)
        self.playerSide = WHITE
        self.btSide = BLACK
        self.aiDepth = 2
        self.ai = AI(self.board, not self.playerSide, self.aiDepth)
        self.engine = chess.uci.popen_engine(r"C:\Users\Owner\Desktop\stockfish-7-win\Windows\stockfish 7 x64.exe")
        self.engine.uci()
        #self.engine.setoption({"UCI_Chess960": True})
        self.engine.setoption({"Threads":4})
        self.engine.setoption({"Skill Level":3})
        #deleted
        self.table.drawMotors()  
        self.table.initialize_Coord()  
        
        #self.button = Button(16)
        #self.button2 = Button(5)
        
        self.voiceControl = voiceControl
        
        #self.bt = btOption
        #self.bluetooth = Bluetooth(self.table.motorY.serialPort)
        #self.bluetooth = Bluetooth(3)      #new code for bluetooth separate from motorY
        self.gameMode = gameMode

    def askForPlayerSide(self):
        playerChoiceInput = input(
            "What side would you like to play as [wB]? ").lower()
        if 'w' in playerChoiceInput:
            print("You will play as white")
            self.playerSide = WHITE
            self.btSide = BLACK
        else:
            print("You will play as black")
            self.playerSide = BLACK
            self.btSide = WHITE 		
        
        #print("Starting Button Tests")
        #self.button.testButton()
        #print("End of Button Tests")
        '''
        self.button.getButton()
        print(self.button.value)
        if(self.button.value == 1):
            print("You will play as white")
            self.playerSide = WHITE
        else:
            print("You will play as black")
            self.playerSide = BLACK
        '''

    def askForDepthOfAI(self):
        #depthInput = 5
        try:
            Input = int(input("Choose Your AI Difficulty\n   1 - Dumb As a Box of Rocks\n   2 - Beginner\n   3 - Intermediate\n   4 - Master\n   5 - GrandMaster\n   6 - Super GrandMaster\n"))
        except:
            print("Invalid Input, Defaulting to an Intermediate Player")
        
        #only take input if button is pressed
        #self.button2.getButton()
        #tmpValue = self.button2.value
        '''
        while(True):
            self.button2.getButton()
            if(self.button2.value != tmpValue):
                break
        '''
        if(Input == 1):
            self.engine.setoption({"Skill Level":0})
            depthInput = 1
        elif(Input == 2):
            self.engine.setoption({"Skill Level":1})
            depthInput = 2           
        elif(Input == 3):
            self.engine.setoption({"Skill Level":6})
            depthInput = 5           
        elif(Input == 4):
            self.engine.setoption({"Skill Level":11})
            depthInput = 10        
        elif(Input == 5):
            self.engine.setoption({"Skill Level":17})
            depthInput = 13      
        elif(Input == 6):
            self.engine.setoption({"Skill Level":20})
            depthInput = 15   
        else:
            self.engine.setoption({"Skill Level":6})               
            depthInput = 2
        #print("engine: \n")
        #print(self.engine)
        #print(self.engine.uci)
        print()      
        self.aiDepth = depthInput
        print("AI Depth: ")
        print(self.aiDepth)


    def printCommandOptions(self):
        undoOption = 'u : undo last move'
        printLegalMovesOption = 'l : show all legal moves'
        randomMoveOption = 'r : make a random move'
        quitOption = 'quit : resign'
        moveOption = 'a3, Nc3, Qxa2, etc : make the move'
        options = [undoOption, printLegalMovesOption, randomMoveOption,
                   quitOption, moveOption, '', ]
        print('\n'.join(options))


    def printAllLegalMoves(self, parser):
        for move in parser.getLegalMovesWithShortNotation(self.board.currentSide):
            #print(move)
            print(move.notation)
            
    def printAllUnfilteredMoves(self, board):
        for move in board.getAllMovesUnfiltered(board.currentSide):
            #print(move)
            print(move.notation)


    def getRandomMove(self, parser):
        legalMoves = self.board.getAllMovesLegal(self.board.currentSide)
        randomMove = random.choice(legalMoves)
        randomMove.notation = parser.notationForMove(randomMove)
        return randomMove


    def makeMove(self, move):
        print()
        #print("testing this dang thing")
        print(move)
        print(move.notation)
        print("Making move : " + move.notation)
        self.board.makeChosenMove(move)

        '''
        print("New Code: ")
        if move.queensideCastle:
            print("queen side castle")
            self.uciBoard.push_san('e1b1') 
        elif move.kingsideCastle:
            print("king side castle")
            self.uciBoard.push_san('e1g1')
        else:
        '''
        self.uciBoard.push_san(move.notation) 
        
    def printPointAdvantage(self):
        print("Currently, the point difference is : " +
              str(self.board.getPointAdvantageOfSide(self.board.currentSide)))


    def undoLastTwoMoves(self):
        if len(self.board.history) >= 2:
            self.board.undoLastMove()
            self.board.undoLastMove()

    #convert move from uci to current board moves 
    def findMove(self, moveFrom, moveTo):
        pos = self.board.humanCoordToPosition(moveFrom)
        endPos = self.board.humanCoordToPosition(moveTo)
        piece = self.board.pieceAtPosition(pos)
        for move in piece.getPossibleMoves():
            if move.newPos == endPos:
                print (move)
                return move
        print ("Move Not Found")

    def getUCIEngineMove(self, time):
        self.engine.position(self.uciBoard)
        uciMove = self.engine.go(depth=self.aiDepth, ponder = False) # Gets tuple of bestmove and ponder move. movetime=time,
        uciMove = uciMove[0].uci()
        print(uciMove)
        if (uciMove == 'e8g8' or uciMove == 'e8c8' or uciMove == 'e1g1' or uciMove == 'e1c1'):
            print( "Move is a castle")
        moveFrom = uciMove[:2]
        print("testing find move functionality...")
        print(moveFrom)
        moveTo = uciMove[2:]
        print(moveTo)
        move = self.findMove(moveFrom, moveTo)
        return move

    def btMove(self, parser):
        print("Taking move from phone")
        #switch parser side and find move from given coords
        parser.side = self.btSide
        pos = self.bluetooth.waitformove()               
        startPos = self.board.humanCoordToPosition(pos[0:2])
        endPos = self.board.humanCoordToPosition(pos[2:4])
        piece = self.board.pieceAtPosition(startPos)
        for move in piece.getPossibleMoves():
            if move.newPos == endPos:
                move.notation = parser.notationForMove(move)
                return move
        print("move is invalid")   
        self.btMove(parser)     

        
        '''          
                    #check if move is valid                     
                    if move:
                        print(move)
                    else:
                        print("Couldn't parse input, enter a valid command or move.")
                        message = self.bluetooth.waitformove()
                        print(message)
                        move = parser.moveForShortNotation(message)
        '''
        return move


    def startGame(self):
        parser = InputParser(self.board, self.playerSide)
        movecount = 0
        while True:
            #print("player side")
            #print(self.playerSide)
            print()
            print(self.board)
            #print(self.uciBoard)
            print()
            '''
            if self.board.isCheckmate():
                if self.board.currentSide == self.playerSide:
                    print("Checkmate, you lost")
                else:
                    print("Checkmate! You won!")
                return
            
            if self.board.isStalemate():
                if self.board.currentSide == self.playerSide:
                    print("Stalemate")
                else:
                    print("Stalemate")
                return
            '''
            if self.board.currentSide == self.playerSide:
                #self.button.getButton()
                #tmpValue2 = self.button2.value 
                #if(tmpValue2 != self.button.value):
                #    print("Button Test")
                
                #if Bluetooth vs AI
                if (self.gameMode == 3):
                    move = self.btMove(parser)
                    move.notation = parser.notationForMove(move)
                    '''
                    print("Taking move from phone")
                    message = self.bluetooth.waitformove()
                    print(message)
                    move = parser.moveForShortNotation(message)
                    if move:
                        print(move)
                    else:
                        print("Couldn't parse input, enter a valid command or move.")
                        message = self.bluetooth.waitformove()
                        print(message)
                        move = parser.moveForShortNotation(message)
                     '''
                else:
                    command = input("It's your move."
                                    " Type '?' for options. ? ").lower()
               
                    '''
                    #only take input  if button is pressed
                    self.button2.getButton()
                    tmpValue = self.button2.value
                    while(True):
                        self.button2.getButton()
                        if(self.button2.value != tmpValue):
                            break
                    '''    
                    if command == 'u':
                        self.undoLastTwoMoves()
                        continue
                    elif command == '?':
                        self.printCommandOptions()
                        continue
                    elif command == 'l':
                        self.printAllLegalMoves(parser)
                        continue
                    elif command == 'x':
                        self.printAllUnfilteredMoves(self.board)
                        continue
                    elif command == 'r':
                        move = self.getRandomMove(parser)
                    elif command == 'quit':
                        return
                    else:
                        parser.side = self.playerSide
                        move = parser.moveForShortNotation(command)

                if move:
                    #move = self.table.getmove(self.board)
                    self.makeMove(move)
                    '''
                    if self.bt == 0:
                        print("bluetooth is on")
                        moveStr = str(move.oldPos[0]) + str(move.oldPos[1]) + str(move.newPos[0]) + str(move.newPos[1])
                        print(moveStr)
                        self.bluetooth.sendmove(moveStr)
                    else:
                        print("bt is off ")
                        print(self.bt) 
                    '''
                else:
                    print("Couldn't parse input, enter a valid command or move.")

            else:
				#if Human vs Bluetooth
                if (self.gameMode == 2):
                    print("Bluetooth Player's Turn...")
                elif (self.gameMode == 4):
                    print("Player 2's Turn")
                else:
                    print("AI thinking...")
                    
                '''
                - - - - - Old AI OpenBook - - - - -
                movecount = movecount + 1
                #print(movecount)
                #starting moves
                #have multiple options for some of the starting moves -- need to implement a method
                #to choose between the options at random. Should also go deeper with the starting moves
                #as it heavily speeds up execution time of the AI
                if movecount < 1:
                    if movecount == 1:
                        #white side initial moves
                        if self.playerSide == BLACK:
                            parser.side = WHITE
                            move = parser.moveForShortNotation('e4')
                        #black side counter moves
                        else:
                            parser.side = BLACK
                            playersMove = self.board.getLastMove()  #white sides last move
                            if playersMove.oldPos == (4,1) and playersMove.newPos == (4,3):
                                moves = ['e5','c5','e6','d5','c6']
                                alpha = random.choice(moves)
                                
                                #alpha values:
                                #    e5 = Mirror
                                #    c5 = Sicilian Defense
                                #    e6 = French Defense
                                #    d5 = Scandinavian Defense
                                #    c6 = Caro-Kann
                                
                                move = parser.moveForShortNotation(alpha)          
                            else:
                                move = parser.moveForShortNotation('d5')
                                
                        parser.side = self.playerSide  #reset parser side
                    if movecount == 2:
                        #white side moves
                        if self.playerSide == BLACK:
                            parser.side = WHITE
                            playersMove = self.board.getLastMove()  #black sides last move
                            if playersMove.oldPos == (4,6) and playersMove.newPos == (4,4): 
                                moves = ['f4','Nf3']
                                alpha = random.choice(moves)
                                
                                #alpha values:
                                #    f4 = King's Gambit
                                #    Nf3 = Ruy Lopex
                                
                                move = parser.moveForShortNotation(alpha)          
                            elif playersMove.oldPos == (4,6) and playersMove.newPos == (4,5):
                                move = parser.moveForShortNotation('d4')    #French Defense Response
                            elif playersMove.oldPos == (3,6) and playersMove.newPos == (3,4):
                                move = parser.moveForShortNotation('exd5')  #Scandinavian Defense Response
                            elif playersMove.oldPos == (2,6) and playersMove.newPos == (2,5):
                                move = parser.moveForShortNotation('d4')    #Caro-Kann Response
                            else:
                                move = parser.moveForShortNotation('Nc3')
                        #black side moves  
                        else:
                            parser.side = BLACK
                            playersMove = self.board.getLastMove()  #white sides last move
                            playersMove2 = self.board.history[-2][0]  #black sides last move
                            if playersMove.oldPos == (3,1) and playersMove.newPos == (3,3):
                                if playersMove2.newPos != (3,4):
                                    move = parser.moveForShortNotation('d5') #French Defense / Caro-Kann Continued
                                else:
                                    move = self.getUCIEngineMove(self.aiDepth*1000)
                                    move.notation = parser.notationForMove(move) 
                            elif playersMove.oldPos == (4,3) and playersMove.newPos == (3,4):
                                move = parser.moveForShortNotation('Qxd5') #Scandinavian Defense Continued
                            elif playersMove.oldPos == (5,1) and playersMove.newPos == (5,3):
                                if playersMove2.newPos != (3,4):
                                    move = parser.moveForShortNotation('d5') #King's Gambit Defense
                                else:
                                    move = self.getUCIEngineMove(self.aiDepth*1000)
                                    move.notation = parser.notationForMove(move)
                            elif playersMove.oldPos == (6,0) and playersMove.newPos == (5,2):
                                if playersMove2.newPos != (2,5):
                                    move = parser.moveForShortNotation('Nc6') #Ruy Lopex
                                else:
                                    move = self.getUCIEngineMove(self.aiDepth*1000)
                                    move.notation = parser.notationForMove(move)
                            else:
                                move = self.ai.getBestMove()
                                move.notation = parser.notationForMove(move)
                                
                        parser.side = self.playerSide  #reset parser side 
                        
                    if movecount == 3:
                        #white side moves
                        if self.playerSide == BLACK:
                            parser.side = WHITE
                            playersMove = self.board.getLastMove()
                            if playersMove.oldPos == (1,7) and playersMove.newPos == (2,5):
                                move = parser.moveForShortNotation('Bb5') #Ruy Lopex
                            else:
                                move = self.getUCIEngineMove(self.aiDepth*1000)
                                move.notation = parser.notationForMove(move)
                        else:
                            move = self.getUCIEngineMove(self.aiDepth*1000)
                            move.notation = parser.notationForMove(move)
                            
                        parser.side = self.playerSide  #reset parser side 
                
                #following starting moves use the node tree to look for the best move  
                else:
                ''' 
                #if Human vs Bluetooth
                if (self.gameMode == 2):
                    move = self.btMove(parser)
                    move.notation = parser.notationForMove(move)
                    '''
                    print("Taking move from phone")
                    #switch parser side and find move from given coords
                    parser.side = self.btSide
                    pos = self.bluetooth.waitformove()               
                    startPos = self.board.humanCoordToPosition(pos[0:2])
                    endPos = self.board.humanCoordToPosition(pos[2:4])
                    piece = self.board.pieceAtPosition(startPos)
                    for move in piece.getPossibleMoves():
                        if move.newPos == endPos:
                            chosenMove = move
                        else:
							print("move is invalid")   
                            self.btMove()      
                    move = chosenMove 
                    move.notation = parser.notationForMove(move) 
                    #check if move is valid                     
                    if move:
                        print(move)
                    else:
                        print("Couldn't parse input, enter a valid command or move.")
                        message = self.bluetooth.waitformove()
                        print(message)
                        move = parser.moveForShortNotation(message)
                    '''
                elif (self.gameMode == 4):
                    print("gameMode is 4")
                    parser2 = InputParser(self.board, self.btSide)
                    command = input("It's your move."
                                    " Type '?' for options. ? ").lower()
               
                    '''
                    #only take input  if button is pressed
                    self.button2.getButton()
                    tmpValue = self.button2.value
                    while(True):
                        self.button2.getButton()
                        if(self.button2.value != tmpValue):
                            break
                    '''    
                    if command == 'u':
                        self.undoLastTwoMoves()
                        continue
                    elif command == '?':
                        self.printCommandOptions()
                        continue
                    elif command == 'l':
                        self.printAllLegalMoves(parser2)
                        continue
                    elif command == 'r':
                        move = self.getRandomMove(parser2)
                    elif command == 'quit':
                        return
                    else:
                        parser2.side = self.btSide
                        move = parser2.moveForShortNotation(command)

                    
                else:
                    move = self.getUCIEngineMove(self.aiDepth*1000)
                    move.notation = parser.notationForMove(move)
                    #print(move.oldPos)
                    #print(move.newPos)

                    #move = self.ai.getBestMove()
                    #move.notation = parser.notationForMove(move)
                
                #print("move: \n")      #for testing purposes
                #print(move)            #for testing purposes      
                
                if self.gameMode != 4:
                    self.table.move(move)          
                self.makeMove(move)
                 
                
