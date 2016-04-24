from Board import Board
from InputParser import InputParser
from AI import AI
import chess.uci
import time
from chessTable import *
import sys
import random
from voiceListener import *

from buttonListener import *
#from BlueTooth import *
from ledmatrix import *

WHITE = True
BLACK = False


class Game:
    def __init__(self, table, testingOptions = 0, btOption = 0, gameMode = 1, voiceControl = 1, led = False, reedBoard = True): #1 for use without motors
        self.board = Board()
        self.led = led
        self.uciBoard = chess.Board()
        self.table = table
        self.playerSide = WHITE
        self.btSide = BLACK
        self.aiDepth = 2
        self.ai = AI(self.board, not self.playerSide, self.aiDepth)
        #self.engine = chess.uci.popen_engine(r"C:\Users\Owner\Desktop\stockfish-7-win\Windows\stockfish 7 x64.exe")
        self.engine = chess.uci.popen_engine("/usr/games/stockfish")
        self.engine.uci()
        self.engine.setoption({"Threads":4})
        self.engine.setoption({"Skill Level":3})
        self.bt = btOption
        self.ledMatrix = self.table.ledMatrix
        self.sleepTime = 0.3
        self.table.initialize_Coord() 
        #Set up buttons
        self.selectButton = ButtonListener(15)
        self.scrollButton = ButtonListener(14)
        self.voice2 = ButtonListener(23)
        self.voice1 = ButtonListener(18)
        self.reedBoardOption = reedBoard
        self.bluetooth = self.table.bt
        self.voiceControl = voiceControl
        self.gameMode = gameMode
        if voiceControl:
            self.voiceListener1 = VoiceListener(1, True);
            if gameMode == 4:
                self.voiceListener2 = VoiceListener(2, False);

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
            optionChanged = False
            while True:
                if self.scrollButton.wasPressed():
                    optionChanged = True
                    self.scrollButton.stopListener()
                    scrollCount = scrollCount + 1
                    #self.scrollButton.stopListener()
                    #self.scrollButton.startListener()
                    if scrollCount == 1:
                        self.ledMatrix.sendString("WHITE")
                    elif scrollCount == 2:
                        self.ledMatrix.sendString("BLACK")
                    else:
                        self.ledMatrix.sendString("WHITE")
                        scrollCount = 1
                    time.sleep(self.sleepTime)
                    self.scrollButton.startListener()
                    
                    print("Scroll Button was Pressed")    
                if self.selectButton.wasPressed():
                    if optionChanged == False:
                        self.selectButton.stopListener()
                        self.selectButton.startListener()
                        continue
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
            optionChanged = False
            while True:
                if self.scrollButton.wasPressed():
                    optionChanged = True
                    self.scrollButton.stopListener()
                    
                    scrollCount = scrollCount + 1
                    print("Scroll Button was Pressed")
                    print(scrollCount)
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
                        self.ledMatrix.sendMultLines("LEVEL","1/6")
                        scrollCount = 1  
                    time.sleep(self.sleepTime)
                    self.scrollButton.startListener()    
                if self.selectButton.wasPressed():
                    if optionChanged == False:
                        self.selectButton.stopListener()
                        self.selectButton.startListener()
                        continue
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
        parser = InputParser(self.board, self.playerSide)
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
        elif move.notation:
            notation = move.notation
            self.uciBoard.push_san(notation)
        else:
            #notation = parser.notationForMove(move)
            fromString = self.board.positionToHumanCoord(move.oldPos)
            toString = self.board.positionToHumanCoord(move.newPos)
            moveString = fromString + toString
            if move.promotion:
                moveString = moveString + "q"
            chessMove = chess.Move.from_uci(moveString)
            self.uciBoard.push(chessMove)
            
        self.board.makeChosenMove(move)
        
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
        
    def printReedBoard(self, board):
        for x in range(len(board)):
            print(board[x])

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
            
            if self.uciBoard.is_game_over():
                if self.board.currentSide == self.playerSide:
                    print("Checkmate, you lost")
                    self.ledMatrix.sendMultLines("YOU","LOST")
                    time.sleep(5)
                else:
                    print("Checkmate! You won!")
                    self.ledMatrix.sendMultLines("YOU","WON")
                    time.sleep(5)
                return
            
            if self.uciBoard.is_stalemate():
                if self.board.currentSide == self.playerSide:
                    print("Stalemate")
                else:
                    print("Stalemate")
                return
            
            if self.board.currentSide == self.playerSide:
                voiceCommandMade = False
                #if Bluetooth vs AI
                if (self.gameMode == 3):
                    move = self.btMove(parser)
                    
                else:
                    if self.led:
                        if self.gameMode == 5:
                            self.ledMatrix.sendMultLines("DEMO","MOVE")
                        else:
                            self.ledMatrix.sendMultLines("YOUR","MOVE")
                        self.scrollButton.startListener()
                        self.selectButton.startListener()
                        self.voice1.startListener()
                    
                    if self.reedBoardOption:
                        scrollCount = 0
                        menuOpened = False
                        voiceCommandMade = False
                        while True:
                            if self.selectButton.wasPressed():
                                if menuOpened:
                                    if scrollCount == 1 or scrollCount == 2:
                                        move = None
                                        break
                                    #end the current game
                                    elif scrollCount == 4 or scrollCount == 3:
                                        self.table.moveto(0,0)
                                        return
                                else:
                                    if self.gameMode == 5:
                                        self.ledMatrix.sendString("load")
                                        move = self.getUCIEngineMove(self.aiDepth*1000)
                                        self.ledMatrix.sendString("l")
                                        break
                                    else:
                                        move = self.table.getMove(self.board)
                                        if move:
                                            print("FOUND IT!")
                                        else:
                                            self.printReedBoard(self.table.playableBoard)
                                        break
                                self.selectButton.stopListener()
                            elif self.scrollButton.wasPressed():
                                menuOpened = True
                                self.scrollButton.stopListener()
                                time.sleep(self.sleepTime)
                                self.scrollButton.startListener()
                                scrollCount = scrollCount + 1
                                print("Scroll Button was Pressed")
                                print(scrollCount)
                                if scrollCount == 1:
                                    self.ledMatrix.sendMultLines("GAME","MENU") 
                                elif scrollCount == 2:
                                    self.ledMatrix.sendMultLines("CARRY","ON") 
                                elif scrollCount == 3:
                                    self.ledMatrix.sendMultLines("NEW","GAME") 
                                elif scrollCount == 4:
                                    self.ledMatrix.sendMultLines("END","GAME")
                                else:
                                    self.ledMatrix.sendMultLines("CARRY","ON")
                                    scrollCount = 2
                            elif self.voiceControl:
                                if menuOpened == False:
                                    if self.voice1.wasPressed():
                                        voiceCommandMade = True
                                        result, voicemove = self.voiceListener1.listen(self.board)
                                        if result == "move":
                                            if self.board.moveIsLegal(voicemove):  # fails if king would be in check after move
                                                move = voicemove
                                            else:
                                                print("illegal move")
                                                move = None
                                        else:
                                            move = None
                                        break   
                                        
                                        
                                        
                                    
                                
                    else:                        
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
                    self.makeMove(move)
                    if voiceCommandMade or self.gameMode == 5:
                        alphaPos = self.board.positionToHumanCoord(move.newPos)
                        self.ledMatrix.sendString("move" + str(move.piece.stringRep).lower() + str(alphaPos).upper())
                        self.table.move(move)
                        if move.pieceToCapture:
                            self.ledMatrix.sendString("capture" + str(move.pieceToCapture.stringRep).lower())
                            time.sleep(3)
                    print("Human Move: ")
                    print(move)
                    if self.bt == 0:
                        print("bluetooth is on")
                        moveStr = str(move.oldPos[0]) + str(move.oldPos[1]) + str(move.newPos[0]) + str(move.newPos[1])
                        print(moveStr)
                        self.bluetooth.sendmove(moveStr)
                    else:
                        print("bt is off ")
                    
                else:
                    if voiceCommandMade:
                        if result == "illegal move":
                            print(result)
                            self.ledMatrix.sendMultLines("MOVE","ERROR")
                        elif result == "bad record":
                            print(result)
                            self.ledMatrix.sendMultLines("SPEAK","AGAIN")
                        elif result == "multiple targets":
                            print(result)
                            self.ledMatrix.sendMultLines("SPEAK","COORD")
                    elif menuOpened:
                        self.ledMatrix.sendMultLines("YOUR","MOVE")
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
                    self.ledMatrix.sendMultLines("BT","MOVE")
                    move = self.btMove(parser)
                    move.notation = parser.notationForMove(move)
                    
                elif (self.gameMode == 4):
                    print("gameMode is 4")
                    parser2 = InputParser(self.board, self.btSide)
                    if self.reedBoardOption:
                        scrollCount = 0
                        menuOpened = False
                        voiceCommandMade = False
                        while True:
                            if self.selectButton.wasPressed():
                                if menuOpened:
                                    if scrollCount == 1 or scrollCount == 2:
                                        move = None
                                        break
                                else:
                                    move = self.table.getMove(self.board)
                                    break
                            elif self.scrollButton.wasPressed():
                                menuOpened = True
                                self.scrollButton.stopListener()
                                time.sleep(self.sleepTime)
                                self.scrollButton.startListener()
                                scrollCount = scrollCount + 1
                                print("Scroll Button was Pressed")
                                print(scrollCount)
                                if scrollCount == 1:
                                    self.ledMatrix.sendMultLines("GAME","MENU") 
                                elif scrollCount == 2:
                                    self.ledMatrix.sendMultLines("CARRY","ON") 
                                elif scrollCount == 3:
                                    self.ledMatrix.sendMultLines("NEW","GAME") 
                                elif scrollCount == 4:
                                    self.ledMatrix.sendMultLines("END","GAME")
                                else:
                                    self.ledMatrix.sendMultLines("CARRY","ON")
                                    scrollCount = 2
                            elif self.voiceControl:
                                if menuOpened == False:
                                    if self.voice1.wasPressed():
                                        voiceCommandMade = True
                                        result2, voicemove = self.voiceListener2.listen(self.board)
                                        if result2 == "move":
                                            if self.board.moveIsLegal(voicemove):  # fails if king would be in check after move
                                                move = voicemove
                                            else:
                                                print("illegal move")
                                                move = None
                                        else:
                                            move = None
                                        break
                    
                    
                    
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
                        time.sleep(3)
                        
                print("done making table move")
                
                if move:
                    self.makeMove(move)
                else:
                    if voiceCommandMade:
                        if result2 == "illegal move":
                            print(result)
                            self.ledMatrix.sendMultLines("MOVE","ERROR")
                        elif result2 == "bad record":
                            print(result)
                            self.ledMatrix.sendMultLines("SPEAK","AGAIN")
                        elif result2 == "multiple targets":
                            print(result)
                            self.ledMatrix.sendMultLines("SPEAK","COORD")
                    elif menuOppened:
                        self.ledMatrix.sendMultLines("YOUR","MOVE")
                    else:
                        self.ledMatrix.sendMultLines("MOVE","ERROR")
                        print("Couldn't parse input, enter a valid command or move.")
                        time.sleep(3)
                        self.ledMatrix.sendMultLines("UNDO","MOVE")
                        time.sleep(3)
                    
                if self.uciBoard.is_game_over():
                    print("King was put in check")
                    self.ledMatrix.sendMultLines("CHECK", "MATE")
                    time.sleep(5)
                elif self.uciBoard.is_check():
                    print("King was put in check")
                    self.ledMatrix.sendMultLines("CHECK")
                    time.sleep(5)
                self.ledMatrix.sendString("clear")

                    
                 
                
