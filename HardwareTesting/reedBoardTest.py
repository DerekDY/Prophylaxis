
from reedBoard import *

def printBoard(board):
	for x in range(len(board)):
		print(board[x])
	
	
print("Testing Board Script")
testBoard = ReedBoard(4,[23,24],[17,27,22])
counter = 0
while(True):
	print("_____________________________")
	print("TEST " + str(counter))
	input("Press enter to get board: ")
	print("Getting Board")
	boardArray = testBoard.getBoard()
	printBoard(boardArray)
	print("_____________________________")
	counter+= 1

	
	
	
	
