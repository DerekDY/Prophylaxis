from Board import Board
from InputParser import InputParser
from AI import AI
import chess.uci
import time
from chessTable import *
import sys
import random

from buttonListener import *
#from BlueTooth import *
from ledmatrix import *

WHITE = True
BLACK = False


class Game:
    def __init__(self, table, testingOptions = 0, btOption = 0, gameMode = 1, voiceControl = 0, led = False): #1 for use without motors
        self.board = Board()
        self.led = led
        self.uciBoard = chess.Board()
        #self.uciBoard = chess.Board(chess960 = True)
        self.table = table
        self.playerSide = WHITE
        self.btSide = BLACK
        self.aiDepth = 2
        self.ai = AI(self.board, not self.playerSide, self.aiDepth)
        #self.engine = chess.uci.popen_engine(r"C:\Users\Owner\Desktop\stockfish-7-win\Windows\stockfish 7 x64.exe")
        self.engine = chess.uci.popen_engine("/usr/games/stockfish")
        self.engine.uci()
        #self.engine.setoption({"UCI_Chess960": True})
        self.engine.setoption({"Threads":4})
        self.engine.setoption({"Skill Level":3})
        self.bt = btOption
        self.ledMatrix = self.table.ledMatrix
        self.sleepTime = 0.3
        self.table.initialize_Coord() 
        #Set up buttons
        pin1 = 19   
        pin2 = 21
        pin3 = 13   #not being used 
        self.selectButton = ButtonListener(pin1)
        self.scrollButton = ButtonListener(pin2)
        self.newGameButton = ButtonListener(pin3)
        
        self.bluetooth = self.table.bt
        #self.bluetooth = Bluetooth(self.table.motorY.serialPort)
        
        self.voiceControl = voiceControl
        
        #self.bt = btOption
        #self.bluetooth = Bluetooth(self.table.motorY.serialPort)
        #self.bluetooth = Bluetooth(3)      #new code for bluetooth separate from motorY

        self.gameMode = gameMode

    def askForPlayerSide(self):
        if self.led == False:
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
        else:
            self.ledMatrix.sendString("clear")
            
            #Choose Player Side
            time.sleep(self.sleepTime)
            self.ledMatrix.sendMultLines("SIDE","W/B ?") 
            self.scrollButton.startListener()
            self.selectButton.startListener()
            scrollCount = 0
            while True:
                if self.scrollButton.wasPressed():
                    self.scrollButton.stopListener()
                    time.sleep(self.sleepTime)
                    self.scrollButton.startListener()
                    scrollCount = scrollCount + 1
                    if scrollCount == 3:
                        scrollCount = 1
                    print("Scroll Button was Pressed")
                    print(scrollCount)
                    self.scrollButton.stopListener()
                    self.scrollButton.startListener()
                    if scrollCount == 1:
                        self.ledMatrix.sendString("WHITE")
                    elif scrollCount == 2:
                        self.ledMatrix.sendString("BLACK")
                    else:
                        self.ledMatrix.sendMultLines("SIDE","W/B ?")  
                        
                if self.selectButton.wasPressed():
                    print("Select Button was Pressed")
                    self.ledMatrix.sendString("clear")
                    sideOption = scrollCount
                    self.playerSide = WHITE if sideOption == 1 else BLACK
                    break

    def askForDepthOfAI(self):
        #depthInput = 5
        if self.led == False:
            try:
                aiOption = int(input("Choose Your AI Difficulty\n   1 - Dumb As a Box of Rocks\n   2 - Beginner\n   3 - Intermediate\n   4 - Master\n   5 - GrandMaster\n   6 - Super GrandMaster\n"))
            except:
                print("Invalid Input, Defaulting to an Intermediate Player")
        else:
            
            #Set up LED Matrix
            self.ledMatrix.sendString("clear")
            
            #Choose Player Side
            time.sleep(self.sleepTime)
            self.ledMatrix.sendMultLines("AI","SKILL") 
            self.scrollButton.startListener()
            self.selectButton.startListener()
            scrollCount = 0
            while True:
                if self.scrollButton.wasPressed():
                    self.scrollButton.stopListener()
                    time.sleep(self.sleepTime)
                    self.scrollButton.startListener()
                    scrollCount = scrollCount + 1
                    if scrollCount == 7:
                        scrollCount = 1
                    print("Scroll Button was Pressed")
                    print(scrollCount)
                    self.scrollButton.stopListener()
                    self.scrollButton.startListener()
                    if scrollCount == 1:
                        self.ledMatrix.sendMultLines("LEVEL","1/6") 
                    elif scrollCount == 2:
                        self.ledMatrix.sendMultLines("LEVEL","2/6") 
                    elif scrollCount == 3:
                        self.ledMatrix.sendMultLines("LEVEL","3/6") 
                    elif scrollCount == 4:
                        self.ledMatrix.sendMultLines("LEVEL","4/6") 
                    elif scrollCount == 5:
                        self.ledMatrix.sendMultLines("LEVEL","5/6") 
                    elif scrollCount == 6:
                        self.ledMatrix.sendMultLines("LEVEL","6/6")                                                                                                 
                    else:
                        self.ledMatrix.sendMultLines("AI","SKILL")  
                        
                if self.selectButton.wasPressed():
                    print("Select Button was Pressed")
                    self.ledMatrix.sendString("clear")
                    aiOption = scrollCount
                    break
            
        if(aiOption == 1):
            self.engine.setoption({"Skill Level":0})
            depthInput = 1
        elif(aiOption == 2):
            self.engine.setoption({"Skill Level":1})
            depthInput = 2           
        elif(aiOption == 3):
            self.engine.setoption({"Skill Level":6})
            depthInput = 5           
        elif(aiOption == 4):
            self.engine.setoption({"Skill Level":11})
            depthInput = 10        
        elif(aiOption == 5):
            self.engine.setoption({"Skill Level":17})
            depthInput = 13      
        elif(aiOption == 6):
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
        if self.led:
            '''
            print("Testing LED Display")
            print(move.piece.stringRep)
            self.ledMatrix.sendString("move" + str(move.piece.stringRep) + str(move.newPos))
            time.sleep(3)
            if move.pieceToCapture:
                self.ledMatrix.sendString("capture" + str(move.pieceToCapture.stringRep))
            time.sleep(3)
            '''   
            self.board.makeChosenMove(move)
            #self.ledMatrix.sendString("clear")
        else:
            self.board.makeChosenMove(move)
        if move.kingsideCastle:
            if move.piece.side == WHITE:
                castleMove = chess.Move.from_uci("e1g1")
            else:
                castleMove = chess.Move.from_uci("e8g8")
            self.uciBoard.push(castleMove)
        elif move.queensideCastle:
            #get the notation of the move in 'e1b1' style
            if move.piece.side == WHITE:
                castleMove = chess.Move.from_uci("e1c1")
            else:
                castleMove = chess.Move.from_uci("e8c1")
            self.uciBoard.push(castleMove)
        else:
            self.uciBoard.push_san(move.notation)
        
        #self.uciBoard.push_san(move.notation) 
        
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
        print("Move from bluetooth: ")
        print(pos)             
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
                    if self.led:
                        self.ledMatrix.sendMultLines("YOUR","MOVE")
                    command = input("It's your move."
                                    " Type '?' for options. ? ").lower()
                  
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
                        '''
                        self.ledMatrix.sendString("clear")
                        alphaPos = self.board.positionToHumanCoord(move.newPos)
                        self.ledMatrix.sendString("move" + str(move.piece.stringRep) + str(alphaPos))
                        time.sleep(3)
                        '''
                if move:
                    #move = self.table.getmove(self.board)
                    self.makeMove(move)
                    print("Human Move: ")
                    print(move)
                    if self.bt == 0:
                        print("bluetooth is on")
                        moveStr = str(move.oldPos[0]) + str(move.oldPos[1]) + str(move.newPos[0]) + str(move.newPos[1])
                        print(moveStr)
                        self.bluetooth.sendmove(moveStr)
                    else:
                        print("bt is off ")
                        print(self.bt) 
                    
                else:
                    self.ledMatrix.sendMultLines("MOVE","ERROR")
                    print("Couldn't parse input, enter a valid command or move.")
                    time.sleep(3)
                    self.ledMatrix.sendMultLines("UNDO","MOVE")
                    time.sleep(3)
                    #wait for
                    #verify the board is in the same state!!!!!

            else:
				#if Human vs Bluetooth
                if (self.gameMode == 2):
                    print("Bluetooth Player's Turn...")
                elif (self.gameMode == 4):
                    print("Player 2's Turn")
                else:
                    print("AI thinking...")
                    
                
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
                    self.ledMatrix.sendString("load")
                    move = self.getUCIEngineMove(self.aiDepth*1000)
                    self.ledMatrix.sendString("l")
                    move.notation = parser.notationForMove(move)
                    #print(move.oldPos)
                    #print(move.newPos)

                    #move = self.ai.getBestMove()
                    #move.notation = parser.notationForMove(move)
                
                #print("move: \n")      #for testing purposes
                #print(move)            #for testing purposes      
                
                if self.gameMode != 4:
                    self.ledMatrix.sendString("clear")
                    alphaPos = self.board.positionToHumanCoord(move.newPos)
                    self.ledMatrix.sendString("move" + str(move.piece.stringRep).lower() + str(alphaPos).upper())
                        
                    self.table.move(move)
                    
                    if move.pieceToCapture:
                        print("there is a piece to capture")
                        self.ledMatrix.sendString("capture" + str(move.pieceToCapture.stringRep).lower())
                        time.sleep(5)
                        
                print("done making table move")
                self.makeMove(move)
                if self.uciBoard.is_check():
                    print("King was put in check")
                    self.ledMatrix.sendString("CHECK")
                    time.sleep(5)
                self.ledMatrix.sendString("clear")

                    
                 
                
