#import stuff
from Board import Board
from chessTable import *
from InputParser import InputParser
import time


'''
print("###############################################")
print("Testing Moves:")
print("Test 1: Single Knight Move - Normal setup")
board1 = Board(testing = 1)
print(board1)
print()
newReed =  [[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], \
			[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0]]
table1 = ChessTable()
table1.reedBoard.testingInput(newReed) 
move = table1.getMove(board1)
print(move)
print()
board1.makeChosenMove(move)
print(board1)

'''
'''

print()
print("###############################################")
print("Test 2: Simple White Pawn Capture Bishop")
board2 = Board(testing = 2)
print(board2)
print()
newReed =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
table2 = ChessTable(1)
currentBoard = newReed
move = table2.getMove(board2, currentBoard)
print(move)
print()
board2.makeChosenMove(move)
print(board2)

'''
'''


print()
print("###############################################")
print("Test 3: White Pawn with 2 captures possible")
board3 = Board(testing = 3)
print(board3)
print()
newReed =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
table3 = ChessTable()
table3.reedBoard.testingInput(newReed) 
move = table3.getMove(board3)
print(move)
print()
board3.makeChosenMove(move)
print(board3)



print()
print("###############################################")
print("Test 4: Piece able to be captured by 2 pieces")
board4 = Board(testing = 4)
print(board4)
print()
newReed =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
table4 = ChessTable()
table4.reedBoard.testingInput(newReed) 
move = table4.getMove(board4)
print(move)
print()
board4.makeChosenMove(move)
print(board4)
print()



print("###############################################")
print("Test 5: Black Queen able to capture 1 piece")
board5 = Board(testing = 5)
print(board5)
print()
newReed =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], \
			[0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
table5 = ChessTable(1)
currentBoard = newReed
move = table5.getMove(board5, currentBoard)
print(move)
print()
board5.makeChosenMove(move)
print(board5)

'''

'''

print("###############################################")
print("Test 6: black castle queen side with scattered pieces")
board6 = Board(testing = 6)
print(board6)
print()
newReed =  [[0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0], \
			[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
table6 = ChessTable(1)
currentBoard = newReed
move = table6.getMove(board6, currentBoard)
board6.makeChosenMove(move)
print(board6)
print()
print("###############################################")


'''
'''

print("###############################################")
print("Test 7: black castle king side with scattered pieces")
board7 = Board(testing = 7)
print(board7)
print()
newReed =  [[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0], \
			[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
table7 = ChessTable(1)
currentBoard = newReed
move = table7.getMove(board7, currentBoard)
print(move)
print()
board7.makeChosenMove(move)
print(board7)
print()
print("###############################################")

'''
'''

print("###############################################")
print("Test 8: white castle queen side with scattered pieces")
board8 = Board(testing = 8)
print(board8)
print()
newReed =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0], \
			[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]]
table8 = ChessTable(1)
currentBoard = newReed
move = table8.getMove(board8, currentBoard)
print(move)
print()
board8.makeChosenMove(move)
print(board8)
print()
print("###############################################")


'''
'''

print("###############################################")
print("Test 9: white castle king side with scattered pieces")
board9 = Board(testing = 9)
print(board9)
print()
newReed =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0], \
			[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0]]
table9 = ChessTable(1)
currentBoard = newReed
move = table9.getMove(board9, currentBoard)
print(move)
print()
board9.makeChosenMove(move)
print(board9)
print()
print("###############################################")


'''
'''

print("Test 10: white pawn en passant capture")
board10 = Board(testing = 10)
print(board10)

parser = InputParser(board10, BLACK)
board10.makeMove(parser.moveForShortNotation("g5"))
board10.currentSide = WHITE
print(board10)
print()
newReed =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
table10 = ChessTable(1)
currentBoard = newReed
move = table10.getMove(board10, currentBoard)
print(move)
print()
board10.makeChosenMove(move)
print(board10)
print()
print("###############################################")


'''
'''

#using to test the possible upper case letter problem in the getMove function capture section
print()
print("###############################################")
print("Test 11: White Queen Capture Knight")
board11 = Board(testing = 11)
print(board11)
print()
newReed =  [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
table11 = ChessTable(1)
currentBoard = newReed
move = table11.getMove(board11, currentBoard)
print(move)
print()
board11.makeChosenMove(move)
print(board11)

'''


print()
print("###############################################")
print("Test 12: Multiple Tests")
board12 = Board(testing = 12)
print(board12)
print()
numPassed = 0

#---------------------- 1 of 30 ---------------------------#

newReed =  [[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]
            
table12 = ChessTable(1)
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == "e4":
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 1 of 30")
    print()
    print(board12)
else:
    print("Failed move 1 of 30")

enter = input("Enter to continue")

#---------------------- 2 of 30 ---------------------------#

newReed =  [[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == "e5":
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 2 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 2 of 30")

enter = input("Enter to continue")

#---------------------- 3 of 30 ---------------------------#

newReed =  [[0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], \
			[0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
print(notation)
if notation == str("Nf3"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 3 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 3 of 30")

enter = input("Enter to continue")

#---------------------- 4 of 30 ---------------------------#

newReed =  [[0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], \
			[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], \
			[0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("Nc6"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 4 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 4 of 30")

enter = input("Enter to continue")


#---------------------- 5 of 30 ---------------------------#

newReed =  [[0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], \
			[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], \
			[0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == "d4":
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 5 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 5 of 30")

enter = input("Enter to continue")


#---------------------- 6 of 30 ---------------------------#

newReed =  [[0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], \
			[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], \
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], \
			[0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("exd4"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 6 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 6 of 30")

enter = input("Enter to continue")


#---------------------- 7 of 30 ---------------------------#

newReed =  [[0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], \
			[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], \
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("Nxd4"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 7 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 7 of 30")

enter = input("Enter to continue")


#---------------------- 8 of 30 ---------------------------#

newReed =  [[0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("Nxd4"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 8 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 8 of 30")

enter = input("Enter to continue")


#---------------------- 9 of 30 ---------------------------#

newReed =  [[0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("Qxd4"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 9 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 9 of 30")

enter = input("Enter to continue")


#---------------------- 10 of 30 ---------------------------#

newReed =  [[0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("Bb4"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 10 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 10 of 30")

enter = input("Enter to continue")


#---------------------- 11 of 30 ---------------------------#

newReed =  [[0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1], \
			[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0], \
			[0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("Nc3"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 11 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 11 of 30")

enter = input("Enter to continue")


#---------------------- 12 of 30 ---------------------------#

newReed =  [[0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], \
			[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1], \
			[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0], \
			[0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("Bxc3"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 12 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 12 of 30")

enter = input("Enter to continue")


#---------------------- 13 of 30 ---------------------------#

newReed =  [[0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0], \
			[0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0], \
			[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], \
			[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0], \
			[0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("Qxc3"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 13 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 13 of 30")

enter = input("Enter to continue")


#---------------------- 14 of 30 ---------------------------#

newReed =  [[0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0], \
			[0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0], \
			[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], \
			[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0], \
			[0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("a5"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 14 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 14 of 30")

enter = input("Enter to continue")


#---------------------- 15 of 30 ---------------------------#

newReed =  [[0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1], \
			[0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0], \
			[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0], \
			[0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("Qxa5"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 15 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 15 of 30")

enter = input("Enter to continue")


#---------------------- 16 of 30 ---------------------------#

newReed =  [[0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1], \
			[0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0], \
			[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0], \
			[0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("Rxa5"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 16 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 16 of 30")

enter = input("Enter to continue")


#---------------------- 17 of 30 ---------------------------#

newReed =  [[0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1], \
			[0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0], \
			[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], \
			[0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("Bd2"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 17 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 17 of 30")

enter = input("Enter to continue")



#---------------------- 18 of 30 ---------------------------#

newReed =  [[0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1], \
			[0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0], \
			[0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0], \
			[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], \
			[0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("Nf6"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 18 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 18 of 30")

enter = input("Enter to continue")


#---------------------- 19 of 30 ---------------------------#

newReed =  [[0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1], \
			[0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0], \
			[0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0], \
			[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], \
			[0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("0-0-0"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 19 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 19 of 30")

enter = input("Enter to continue")


#---------------------- 20 of 30 ---------------------------#

newReed =  [[0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1], \
			[0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0], \
			[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0], \
			[0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("Nxe4"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 20 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 20 of 30")

enter = input("Enter to continue")


#---------------------- 21 of 30 ---------------------------#

newReed =  [[0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1], \
			[0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0], \
			[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0], \
			[0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("Bxa5"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 21 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 21 of 30")

enter = input("Enter to continue")


#---------------------- 22 of 30 ---------------------------#

newReed =  [[0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1], \
			[0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0], \
			[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], \
			[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0], \
			[0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("g5"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 22 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 22 of 30")

enter = input("Enter to continue")



#---------------------- 23 of 30 ---------------------------#

newReed =  [[0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1], \
			[0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0], \
			[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], \
			[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], \
			[0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("a4"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 23 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 23 of 30")

enter = input("Enter to continue")



#---------------------- 24 of 30 ---------------------------#

newReed =  [[0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1], \
			[0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0], \
			[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], \
			[0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("g4"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 24 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 24 of 30")

enter = input("Enter to continue")


#---------------------- 25 of 30 ---------------------------#

newReed =  [[0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1], \
			[0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0], \
			[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0], \
			[0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("h4"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 25 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 25 of 30")

enter = input("Enter to continue")


#---------------------- 26 of 30 ---------------------------#

newReed =  [[0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1], \
			[0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0], \
			[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], \
			[0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0], \
			[1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("gxh3"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 26 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 26 of 30")

enter = input("Enter to continue")


#---------------------- 27 of 30 ---------------------------#

newReed =  [[0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1], \
			[0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0], \
			[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1], \
			[0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0], \
			[0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0], \
			[1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("f3"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 27 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 27 of 30")

enter = input("Enter to continue")


#---------------------- 28 of 30 ---------------------------#

newReed =  [[0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1], \
			[0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0], \
			[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1], \
			[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], \
			[1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0], \
			[1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
if notation == str("hxg2"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 28 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 28 of 30")

enter = input("Enter to continue")


#---------------------- 29 of 30 ---------------------------#

newReed =  [[0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1], \
			[0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0], \
			[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0], \
			[1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print(move)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
print(notation)
if notation == str("fxe4"):
    numPassed = numPassed + 1
    board12.makeChosenMove(move)
    print("Passed move 29 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 29 of 30")

enter = input("Enter to continue")


#---------------------- 30 of 30 ---------------------------#

#this is the pawn promotion test
#pawn promotion currently has problems
#no code in getMove for pawn promotions right now

newReed =  [[0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1], \
			[0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0], \
			[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
			[1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1], \
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			[1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], \
			[1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0]]
            
currentBoard = newReed
move = table12.getMove(board12, currentBoard)
print("promotion move: ")
print(move)
print("Promotion: ")
print(move.promotion)
print()

parser = InputParser(board12, WHITE)
notation = parser.notationForMove(move)
print(notation)
if notation == str("g1=Q"):
    numPassed = numPassed + 1
    print("move: ")
    print(move)
    print(move.specialMovePiece)
    board12.makeChosenMove(move)
    print("Passed move 30 of 30")
    print()
    print(board12)
    
else:
    print("Failed move 30 of 30")

enter = input("Enter to continue")

print("Tests Complete")
print("Passed %d of 30 Tests" % numPassed)









