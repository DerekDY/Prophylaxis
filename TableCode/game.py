from Board import Board
from InputParser import InputParser
import chess.uci
import time
from chessTable import *
import sys
import random
from voiceListener import *
from datetime import datetime

import sys
import os

from buttonListener import *
from buttonListener2 import *
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
        self.moveTime = 0
        #self.engine = chess.uci.popen_engine(r"C:\Users\Owner\Desktop\stockfish-7-win\Windows\stockfish 7 x64.exe")
        self.engine = chess.uci.popen_engine("/usr/games/stockfish")
        self.engine.setoption({"Threads":4})
        #self.engine.setoption({"Skill Level":1})
        self.engine.uci()
        print(self.engine.name)
        self.bt = btOption
        self.ledMatrix = self.table.ledMatrix
        self.sleepTime = 0.3
        self.ledMatrix.sendString("zero")
        self.table.initialize_Coord() 
        self.ledMatrix.sendString("z")
        self.ledMatrix.sendString("clear")
        #Set up buttons
        self.selectButton = ButtonListener2(15)
        self.scrollButton = ButtonListener2(14)
        self.voice2 = ButtonListener(23)
        self.voice1 = ButtonListener2(18)
        self.reedBoardOption = reedBoard
        self.bluetooth = self.table.bt
        self.voiceControl = voiceControl
        self.gameMode = gameMode
        self.moveWasMade = 0
        
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
            self.ledMatrix.sendMultLines("@SIDE","W/B ?") 
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
            self.ledMatrix.sendMultLines("@AI","SKILL") 
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
        print()
        print("AI LEVEL: ")
        print(aiOption)
        depthInput = 0
        timeInput = 0
        if(aiOption == 1):
            self.engine.setoption({'Skill Level': 0})
            self.engine.setoption({'Contempt Factor': -50})
            self.engine.setoption({"UCI_LimitStrength":True})
            self.engine.setoption({"UCI_Elo":10})
            depthInput = 2
        elif(aiOption == 2):
            #self.engine.setoption({'Skill Level': 3})  
            #depthInput = 4
            self.engine.setoption({'Skill Level': 0})
            self.engine.setoption({'Contempt Factor': 50})
            self.engine.setoption({"UCI_LimitStrength":True})
            self.engine.setoption({"UCI_Elo":10})
            depthInput = 4      
        elif(aiOption == 3):
            depthInput = 6   
            self.engine.setoption({'Skill Level': 5})        
        elif(aiOption == 4):
            depthInput = 10
            self.engine.setoption({'Skill Level': 10})        
        elif(aiOption == 5):
            depthInput = 12
            self.engine.setoption({'Skill Level': 15})     
        elif(aiOption == 6):
            depthInput = 15 
            self.engine.setoption({'Skill Level': 20})  
        else:             
            depthInput = 2
            self.engine.setoption({'Skill Level': 0}) 
        print() 
        self.engine.setoption({"Ponder": False})       
        self.aiDepth = depthInput
        self.moveTime = timeInput
        print("AI Depth: ")
        print(self.aiDepth)
        print("Move Time: ")
        print(self.moveTime)
        print("Engine: ")
        print(self.engine)
        print(self.engine.options)
        time.sleep(.5)


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
        print(self.aiDepth)
        uciMoveString = uciMove[0].uci()
        print(uciMoveString)
        if (uciMoveString == 'e8g8' or uciMoveString == 'e8c8' or uciMoveString == 'e1g1' or uciMoveString == 'e1c1'):
            print( "Move is a castle")
        moveFrom = uciMoveString[:2]
        print("testing find move functionality...")
        print(moveFrom)
        moveTo = uciMoveString[2:4]
        print(moveTo)
        move = self.findMove(moveFrom, moveTo)
        return move
        
    def compareBoard(self, reedBoard, moveError = False): # reed board  is full board of 1s and 0s from the matrix
        #convet current board and capture bins to ones and zeros 
        white = self.board.whiteCaptured
        black = self.board.blackCaptured
        whiteCaptured = [[0 for x in range(2)] for y in range(8)]
        for p in white:
            whiteCaptured[7 - p.position[1]][p.position[0]] = 1   #engine boards sides were flipped from the engine board
        blackCaptured = [[0 for x in range(2)] for y in range(8)]
        for p in black:
            blackCaptured[7 - p.position[1]][p.position[0]] = 1   #engine boards sides were flipped from the engine board
        engineBoard = [[0 for x in range(8)] for y in range(8)]
        for p in self.board.pieces:
            engineBoard[7 - p.position[1]][p.position[0]] = 1   #engine boards sides were flipped from the engine board
        totalBoard = [[0 for x in range(12)] for y in range(8)]
        for y in range(8):
            for x in range(12):
                if x<2:
                    totalBoard[y][x] = blackCaptured[y][x]
                elif x <10:
                    totalBoard[y][x] = engineBoard[y][x-2]
                else:
                    totalBoard[y][x] = whiteCaptured[y][x-10]
        
        #print("Total")
        #self.printReedBoard(totalBoard)
        #print("Real")
        #self.printReedBoard(reedBoard)
        
        '''
        incorrectPos = ""
        for y in range(8):
            for x in range(12):
                if totalBoard[y][x] != reedBoard[y][x]:
                    print("incorrect board")
                    print(x)
                    print(y)
                    incorrectPos += str(x)
                    incorrectPos += str(y)
                    
        print("incorrect position string: ")
        print(incorrectPos)
        '''
        
        if totalBoard == reedBoard:
            print("board is good")
        else:
            self.ledMatrix.sendMultLines("!FIX","BOARD") 
            time.sleep(2)
            reedString = ""
            for y in range(8):
                for x in range (12):
                    if totalBoard[y][x] != reedBoard[y][x]:
                        if totalBoard[y][x] == 1:
                            reedString += 'g'
                        else:
                            reedString += 'r'
                    else:
                        if totalBoard[y][x] == 1:
                            reedString += 'b'
                        else:
                            reedString += 'x'
                            
            print("reedString")
            print(reedString)
            
            #get length of incorrectPos and send that into the ledMatrix
            
            #length = len(incorrectPos)
            
            self.selectButton.stopListener()
            self.selectButton.startListener()
            
            self.ledMatrix.sendString("rb" + reedString)
            
            while(True):
                if self.selectButton.wasPressed():
                    print("breaking out of while loop")
                    self.selectButton.stopListener()
                    break
            reedBoard = self.table.reedBoard.getBoard()              
            self.compareBoard(reedBoard)    

        return totalBoard == reedBoard

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
                    self.table.moveto(0,0)
                    self.ledMatrix.sendMultLines("YOU","LOST")
                    time.sleep(3)
                else:
                    print("Checkmate! You won!")
                    self.table.moveto(0,0)
                    self.ledMatrix.sendMultLines("YOU","WON")
                    time.sleep(3)
                return
            
            if self.uciBoard.is_stalemate():
                if self.board.currentSide == self.playerSide:
                    print("Stalemate")
                else:
                    print("Stalemate")
                return
                
            reedBoard = self.table.reedBoard.getBoard()
            
            self.compareBoard(reedBoard)
                
                
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
                            if self.playerSide == WHITE:
                                self.ledMatrix.sendMultLines("WHITE","MOVE")
                            else:
                                self.ledMatrix.sendMultLines("BLACK","MOVE")
                        self.scrollButton.startListener()
                        self.selectButton.startListener()
                        self.voice1.startListener()
                    
                    if self.reedBoardOption:
                        scrollCount = 0
                        menuOpened = False
                        voiceCommandMade = False
                        startTime = datetime.now()
                        timerUp = False
                        while True:
                            if (datetime.now() - startTime).total_seconds() >= 2:
                                timerUp = True
                            if self.selectButton.wasPressed() or (timerUp and not(menuOpened) and self.gameMode == 5):
                                if menuOpened:
                                    if scrollCount == 1 or scrollCount == 2:
                                        move = None
                                        self.scrollButton.stopListener()
                                        self.selectButton.stopListener()
                                        self.voice1.stopListener()
                                        break
                                    #end the current game
                                    elif scrollCount == 3:
                                        self.table.moveto(0,0)
                                        self.scrollButton.stopListener()
                                        self.selectButton.stopListener()
                                        self.voice1.stopListener()
                                        return
                                    elif scrollCount == 4:
                                        print("Closing the program and shutting down the Pi")
                                        self.table.moveto(0,0)
                                        self.scrollButton.stopListener()
                                        self.selectButton.stopListener()
                                        self.voice1.stopListener()
                                        self.ledMatrix.sendMultLines("!SHUT","DOWN")
                                        time.sleep(1)
                                        self.ledMatrix.sendMultLines("!IN","5 SEC")
                                        time.sleep(2)
                                        self.ledMatrix.sendString("clear")
                                        os.system("sudo shutdown -h now")
                                        sys.exit(0)
                                else:
                                    if self.gameMode == 5:
                                        self.ledMatrix.sendString("load")
                                        move = self.getUCIEngineMove(self.aiDepth*1000)
                                        self.ledMatrix.sendString("l")
                                        self.scrollButton.stopListener()
                                        self.selectButton.stopListener()
                                        self.voice1.stopListener()
                                        break
                                    else:
                                        moveReturn = self.table.getMove(self.board)
                                        move = moveReturn[0]
                                        if move:
                                            print("FOUND IT!")
                                        else:
                                            moveError = moveReturn[1]
                                            self.printReedBoard(self.table.playableBoard)
                                        self.scrollButton.stopListener()
                                        self.selectButton.stopListener()
                                        self.voice1.stopListener()
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
                                    self.ledMatrix.sendMultLines("@GAME","MENU") 
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
                                        self.ledMatrix.sendMultLines("REC","VOICE") 
                                        voiceCommandMade = True
                                        result, voicemove = self.voiceListener1.listen(self.board)
                                        if result == "move":
                                            #if self.board.moveIsLegal(voicemove):  # fails if king would be in check after move
                                            move = voicemove
                                            #else:
                                            #    print("illegal move")
                                            #    move = None
                                            #    self.ledMatrix.sendMultLines("MOVE","ERROR")
                                            #    time.sleep(2)
                                        else:
                                            move = None
                                        self.scrollButton.stopListener()
                                        self.selectButton.stopListener()
                                        self.voice1.stopListener()
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
                    if self.board.moveIsLegal(move):
                        self.makeMove(move)
                        self.moveWasMade = 1
                        if voiceCommandMade or self.gameMode == 5:
                            '''
                            alphaPos = self.board.positionToHumanCoord(move.newPos)
                            self.ledMatrix.sendString("move" + str(move.piece.stringRep).lower() + str(alphaPos).upper())
                            self.table.move(move)
                            if move.pieceToCapture:
                                self.ledMatrix.sendString("capture" + str(move.pieceToCapture.stringRep).lower())
                                time.sleep(3)
                            '''
                            alphaPos = self.board.positionToHumanCoord(move.newPos)
                            self.table.move(move, self.ledMatrix, alphaPos)
                            
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
                        self.ledMatrix.sendMultLines("MOVE","ERROR")
                        time.sleep(2)
                    
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
                        time.sleep(2)
                    elif menuOpened:
                        if self.playerSide == WHITE:
                            self.ledMatrix.sendMultLines("WHITE","MOVE")
                        else:
                            self.ledMatrix.sendMultLines("BLACK","MOVE")
                    else:
                        reedBoard = self.table.reedBoard.getBoard()              
                         
                        if moveError == 1:
                            self.ledMatrix.sendMultLines("CHECK","BOARD")
                            time.sleep(2)
                            self.compareBoard(reedBoard)
                        elif moveError == 3:
                            self.ledMatrix.sendMultLines("MOVE","ERROR")
                            time.sleep(2)
                            self.compareBoard(reedBoard)
                        elif moveError == 2:
                            self.ledMatrix.sendMultLines("MAKE","MOVE")
                            time.sleep(2)
                        else:
                            self.ledMatrix.sendMultLines("MOVE","ERROR")
                            time.sleep(2)
                            self.compareBoard(reedBoard)

            #Player 2
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
                    
                    if self.led:
                        if self.playerSide == WHITE:
                            self.ledMatrix.sendMultLines("BLACK","MOVE")
                        else:
                            self.ledMatrix.sendMultLines("WHITE","MOVE")
                        self.scrollButton.startListener()
                        self.selectButton.startListener()
                        self.voice2.startListener()
                        
                    if self.reedBoardOption:
                        scrollCount = 0
                        menuOpened = False
                        voiceCommandMade = False
                        while True:
                            if self.selectButton.wasPressed():
                                if menuOpened:
                                    if scrollCount == 1 or scrollCount == 2:
                                        move = None
                                        self.scrollButton.stopListener()
                                        self.selectButton.stopListener()
                                        self.voice2.stopListener()      #switched from voice 1 to voice 2
                                        break
                                    elif scrollCount == 3:
                                        self.table.moveto(0,0)
                                        self.scrollButton.stopListener()
                                        self.selectButton.stopListener()
                                        self.voice2.stopListener()
                                        return
                                    elif scrollCount == 4:
                                        print("Closing the program and shutting down the Pi")
                                        self.table.moveto(0,0)
                                        self.scrollButton.stopListener()
                                        self.selectButton.stopListener()
                                        self.voice1.stopListener()
                                        self.ledMatrix.sendMultLines("!SHUT","DOWN")
                                        time.sleep(1)
                                        self.ledMatrix.sendMultLines("!IN","5 SEC")
                                        time.sleep(2)
                                        self.ledMatrix.sendString("clear")
                                        os.system("sudo shutdown -h now")
                                        sys.exit(0)
                                else:
                                    moveReturn = self.table.getMove(self.board)
                                    move = moveReturn[0]
                                    moveError = moveReturn[1]
                                    self.scrollButton.stopListener()
                                    self.selectButton.stopListener()
                                    self.voice2.stopListener()
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
                                    self.ledMatrix.sendMultLines("@GAME","MENU") 
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
                                    if self.voice2.wasPressed():
                                        self.ledMatrix.sendMultLines("REC","VOICE")
                                        voiceCommandMade = True
                                        result2, voicemove = self.voiceListener2.listen(self.board)
                                        if result2 == "move":
                                            #if self.board.moveIsLegal(voicemove):  # fails if king would be in check after move
                                            move = voicemove
                                        else:
                                            move = None
                                        self.scrollButton.stopListener()
                                        self.selectButton.stopListener()
                                        self.voice2.stopListener()
                                        
                                        break
                    
                else:
                    self.ledMatrix.sendString("load")
                    move = self.getUCIEngineMove(self.aiDepth*1000)
                    self.ledMatrix.sendString("l")
                    
                
                if move:
                    if self.board.moveIsLegal(move):
                        self.makeMove(move)
                        if self.gameMode != 4:
                            alphaPos = self.board.positionToHumanCoord(move.newPos) 
                            self.table.move(move, self.ledMatrix, alphaPos)  
                        elif voiceCommandMade:
                            alphaPos = self.board.positionToHumanCoord(move.newPos)
                            self.ledMatrix.sendString("move" + str(move.piece.stringRep).lower() + str(alphaPos).upper())
                            self.table.move(move)
                            if move.pieceToCapture:
                                self.ledMatrix.sendString("capture" + str(move.pieceToCapture.stringRep).lower())
                                time.sleep(3)
                    else:
                        self.ledMatrix.sendMultLines("MOVE","ERROR")
                        time.sleep(2)
                else:
                    if voiceCommandMade:
                        if result2 == "illegal move":
                            print(result2)
                            self.ledMatrix.sendMultLines("MOVE","ERROR")
                        elif result2 == "bad record":
                            print(result2)
                            self.ledMatrix.sendMultLines("SPEAK","AGAIN")
                        elif result2 == "multiple targets":
                            print(result2)
                            self.ledMatrix.sendMultLines("SPEAK","COORD")
                        time.sleep(2)
                    elif menuOpened:
                        if self.playerSide == WHITE:
                            self.ledMatrix.sendMultLines("BLACK","MOVE")
                        else:
                            self.ledMatrix.sendMultLines("WHITE","MOVE")
                    else:
                        reedBoard = self.table.reedBoard.getBoard()              
                         
                        if moveError == 1:
                            self.ledMatrix.sendMultLines("CHECK","BOARD")
                            time.sleep(2)
                            self.compareBoard(reedBoard)
                        elif moveError == 3:
                            self.ledMatrix.sendMultLines("MOVE","ERROR")
                            time.sleep(2)
                            self.compareBoard(reedBoard)
                        elif moveError == 2:
                            self.ledMatrix.sendMultLines("MAKE","MOVE")
                            time.sleep(2)
                        else:
                            self.ledMatrix.sendMultLines("MOVE","ERROR")
                            time.sleep(2)
                            self.compareBoard(reedBoard)
                        print("Couldn't parse input, enter a valid command or move.")
                    
                if self.uciBoard.is_game_over():
                    print("King was put in check")
                    self.ledMatrix.sendMultLines("CHECK", "MATE")
                    time.sleep(5)
                elif self.uciBoard.is_check():
                    print("King was put in check")
                    self.ledMatrix.sendString("CHECK")
                    time.sleep(5)
                self.ledMatrix.sendString("clear")

                    
                 
                
