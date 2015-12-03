import time
from chessTable import *
from subprocess import call
from threading import Thread


def moveX(table, dx):
	print ("Thread: x")
	start_time = time.time()
	if (dx < 0):
		table.motorX.cw(abs(dx))
	else:
		table.motorX.ccw(abs(dx))
	end_time = time.time()
	elapsed_time = end_time - start_time
	print ("Thread x took %.2f seconds" % elapsed_time)

def moveY(table, dy):
	print ("Thread: y")
	start_time = time.time()
	if (dy < 0):
		table.motorY.cw(abs(dy))
	else:
		table.motorY.ccw(abs(dy))
	end_time = time.time()
	elapsed_time = end_time - start_time
	print ("Thread y took %.2f seconds" % elapsed_time)


testTable = ChessTable()
testTable.drawMotors()
testTable.initialize_Coord()

while(1):
	new_x = int(input("X-Location\n>"))
	new_y = int(input("Y-Location\n>"))

	dx = new_x - testTable.x
	dy = new_y - testTable.y
	xThread = Thread(target=moveX, args=(testTable,dx))
	yThread = Thread(target=moveY, args=(testTable,dy))
	xThread.start()
	yThread.start()
	xThread.join()
	yThread.join()
	testTable.x = new_x
	testTable.y = new_y