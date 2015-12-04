from motor import *

x = 0
y = 0
motorX = Motor(21,16,20)  
motorY = Motor(26,19,13) 


while(1):
	new_x = int(input("How far X (-1 to Stop): "))
	new_y = int(input("How far y: "))
	motorX.cw(0)
	motorY.cw(0)
	if(new_x == -1):
		break
	dx = new_x - x
	dy = new_y - y 
	if (dx < 0):
		motorX.cw(abs(dx))
	else:
		motorX.ccw(abs(dx))
	if (dy < 0):
		motorY.cw(abs(dy))
	else:
		motorY.ccw(abs(dy))
	x = new_x
	y = new_y
	print ("Coordinates are: " + str(x) + ", " + str(y))