
from reedBoard import *

def printBoard(board):
	for x in range(len(board)):
		print(board[x])
	
	
print("Testing Board Script")
testBoard = ReedBoard(12,[5,6,13,19],[24,25,8,7,12,16,20,21])
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

	
	
	
	
