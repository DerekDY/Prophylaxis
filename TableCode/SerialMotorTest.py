import time
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600) #make connection

x = 0
y = 0
steps = 2000

def waitfordone(serial):
	done = False
	while (not done):
		if ("Done" in serial.readline().decode('utf-8')):
			done = True



def goto(newX, newY, carying):
	dx = newX - x
	dy = newY - y
	xfb = "f" if (dx > 0) else "b"
	yfb = "f" if (dy > 0) else "b"
	if(dx == dy or not carying):
		ser.write(bytes(xfb+str(abs(dx*steps))+"\n", 'UTF-8'))
		#ser2.write(bytes(yfb+str(abs(dy*steps))+"\n", 'UTF-8'))
		print("Other Motor Running")
		waitfordone(ser)
	else:
		ser.write(bytes(xfb+str(abs(dx*steps))+"\n", 'UTF-8'))
		waitfordone(ser)
		#ser2.write(bytes(yfb+str(abs(dy*steps))+"\n", 'UTF-8'))
		#waitfordone(ser2)
		print("Other Motor Sarting")
		time.sleep(1)
		print("Other Motor Done")


while True:
	print("At: " + str(x)+ ","+str(y))
	newX = int(input("New X: "))
	newY = int(input("New Y: "))
	cary = input("Carying? (y/n): ")
	carying = True if (cary.lower() == "y") else False
	goto(newX, newY, carying)
	x = newX
	y = newY
	
