from Board import Board
from InputParser import InputParser
from AI import AI
from chessTable import *
import sys
import random

WHITE = True
BLACK = False

class Game:
    def __init__(self):
        self.board = Board()
        self.table = ChessTable()
        self.playerSide = WHITE
        self.aiDepth = 2
        self.ai = AI(self.board, not self.playerSide, self.aiDepth)
        #deleted
        self.table.drawMotors()  
        self.table.initialize_Coord()  



    def askForPlayerSide(self):
        playerChoiceInput = input(
            "What side would you like to play as [wB]? ").lower()
        if 'w' in playerChoiceInput:
            print("You will play as white")
            self.playerSide = WHITE
        else:
            print("You will play as black")
            self.playerSide = BLACK


    def askForDepthOfAI(self):
        depthInput = 2
        try:
            depthInput = int(input("How deep should the AI look for moves?\n"
                                   "Warning : values above 3 will be very slow."
                                   " [n]? "))
        except:
            print("Invalid input, defaulting to 2")
        self.aiDepth = depthInput


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
            print(move.notation)


    def getRandomMove(self, parser):
        legalMoves = self.board.getAllMovesLegal(self.board.currentSide)
        randomMove = random.choice(legalMoves)
        randomMove.notation = parser.notationForMove(randomMove)
        return randomMove


    def makeMove(self, move):
        print()
        print("Making move : " + move.notation)
        self.board.makeChosenMove(move)


    def printPointAdvantage(self):
        print("Currently, the point difference is : " +
              str(self.board.getPointAdvantageOfSide(self.board.currentSide)))


    def undoLastTwoMoves(self):
        if len(self.board.history) >= 2:
            self.board.undoLastMove()
            self.board.undoLastMove()


    def startGame(self):
        parser = InputParser(self.board, self.playerSide)
        movecount = 0
        while True:
            #print("player side")
            #print(self.playerSide)
            print()
            print(self.board)
            print()
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

            if self.board.currentSide == self.playerSide:
                # printPointAdvantage(self.board)
                move = None
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
                elif command == 'r':
                    move = self.getRandomMove(parser)
                elif command == 'quit':
                    return
                else:
                    move = parser.moveForShortNotation(command)
                if move:
                    #move = self.table.getmove(self.board)
                    self.makeMove(move)

                else:
                    print("Couldn't parse input, enter a valid command or move.")

            else:
                print("AI thinking...")
                movecount = movecount + 1
                print(movecount)
                #starting moves
                #have multiple options for some of the starting moves -- need to implement a method
                #to choose between the options at random. Should also go deeper with the starting moves
                #as it heavily speeds up execution time of the AI
                if movecount < 4:
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
                                '''
                                alpha values:
                                    e5 = Mirror
                                    c5 = Sicilian Defense
                                    e6 = French Defense
                                    d5 = Scandinavian Defense
                                    c6 = Caro-Kann
                                '''
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
                                '''
                                alpha values:
                                    f4 = King's Gambit
                                    Nf3 = Ruy Lopex
                                '''
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
                                    move = self.ai.getBestMove()
                                    move.notation = parser.notationForMove(move) 
                            elif playersMove.oldPos == (4,3) and playersMove.newPos == (3,4):
                                move = parser.moveForShortNotation('Qxd5') #Scandinavian Defense Continued
                            elif playersMove.oldPos == (5,1) and playersMove.newPos == (5,3):
                                if playersMove2.newPos != (3,4):
                                    move = parser.moveForShortNotation('d5') #King's Gambit Defense
                                else:
                                    move = self.ai.getBestMove()
                                    move.notation = parser.notationForMove(move)
                            elif playersMove.oldPos == (6,0) and playersMove.newPos == (5,2):
                                if playersMove2.newPos != (2,5):
                                    move = parser.moveForShortNotation('Nc6') #Ruy Lopex
                                else:
                                    move = self.ai.getBestMove()
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
                                move = self.ai.getBestMove()
                                move.notation = parser.notationForMove(move)
                        else:
                            move = self.ai.getBestMove()
                            move.notation = parser.notationForMove(move)
                            
                        parser.side = self.playerSide  #reset parser side 
                
                #following starting moves use the node tree to look for the best move  
                else:
                    move = self.ai.getBestMove()
                    move.notation = parser.notationForMove(move)
                
                #print("move: \n")      #for testing purposes
                #print(move)            #for testing purposes   
                self.table.move(move)
                self.makeMove(move)





