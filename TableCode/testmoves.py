#import stuff
from Board import Board
from chessTable import *
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



print()
print("###############################################")
print("Test 2: Simple Paun Capture")
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
table2 = ChessTable()
table2.reedBoard.testingInput(newReed) 
move = table2.getMove(board2)
print(move)
print()
board2.makeChosenMove(move)
print(board2)
'''
print()
print("###############################################")
print("Test 3: Paun with 2 captures possible")
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

'''

print()
print("###############################################")
print("Test 4: Piece able to be captured by 2 pieces")
board4 = Board(testing = 4)
print(board4)
print()



print()
print("###############################################")

'''