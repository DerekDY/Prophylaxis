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


    def printPointAdvantage():
        print("Currently, the point difference is : " +
              str(self.board.getPointAdvantageOfSide(self.board.currentSide)))


    def undoLastTwoMoves(self):
        if len(self.board.history) >= 2:
            self.board.undoLastMove()
            self.board.undoLastMove()


    def startGame(self):
        parser = InputParser(self.board, self.playerSide)
        while True:
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
                    undoLastTwoMoves()
                    continue
                elif command == '?':
                    printCommandOptions()
                    continue
                elif command == 'l':
                    printAllLegalMoves(parser)
                    continue
                elif command == 'r':
                    move = getRandomMove(parser)
                elif command == 'quit':
                    return
                else:
                    move = parser.moveForShortNotation(command)
                if move:
                    #self.table.getmove(self.board)
                    self.makeMove(move)

                else:
                    print("Couldn't parse input, enter a valid command or move.")

            else:
                print("AI thinking...")
                move = self.ai.getBestMove()
                move.notation = parser.notationForMove(move)
                self.table.move(move)
                self.makeMove(move)






