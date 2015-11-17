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
print("Test 2: Simple White Pawn Capture")
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
table5 = ChessTable()
table5.reedBoard.testingInput(newReed) 
move = table5.getMove(board5)
print(move)
print()
board5.makeChosenMove(move)
print(board5)

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
table6 = ChessTable()
table6.reedBoard.testingInput(newReed) 
move = table6.getMove(board6)
print(move)
print()
board6.makeChosenMove(move)
print(board6)
print()
print("###############################################")


#Test 6 currently not working...need to add special moves to getMove()




