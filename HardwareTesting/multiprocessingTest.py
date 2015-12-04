import time
from motor import *
from subprocess import call
from multiprocessing import Process


def moveX(motorX, dx):
	print ("Thread: x")
	start_time = time.time()
	motorX.cw(0)
	if (dx < 0):
		motorX.cw(abs(dx))
	else:
		motorX.ccw(abs(dx))
	end_time = time.time()
	elapsed_time = end_time - start_time
	print ("Thread x took %.2f seconds" % elapsed_time)

def moveY(motorY, dy):
	print ("Thread: y")
	start_time = time.time()
	motorY.cw(0)
	if (dy < 0):
		motorY.cw(abs(dy))
	else:
		motorY.ccw(abs(dy))
	end_time = time.time()
	elapsed_time = end_time - start_time
	print ("Thread y took %.2f seconds" % elapsed_time)



motorX = Motor(21,16,20)  
motorY = Motor(26,19,13)
x = 0
y = 0

while(1):
	new_x = int(input("X-Location\n>"))
	new_y = int(input("Y-Location\n>"))

	dx = new_x - x
	dy = new_y - y
	xProcess = Process(target=moveX, args=(motorX,dx))
	yProcess = Process(target=moveY, args=(motorY,dy))
	xProcess.start()
	yProcess.start()
	xProcess.join()
	yProcess.join()
	x = new_x
	y = new_y