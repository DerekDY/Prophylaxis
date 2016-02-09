from xytable import *

table = XYTable()

print("Welcome to the Table Testing EXTRAVAGANZA!!!")
table.x = 0
table.y = 0
table.initialize_Coord()
while True:
	print("At: " + str(table.x))
	newX = int(input("New X: "))
	#newY = int(input("New Y: ")) 
	table.moveto(newX, 0)