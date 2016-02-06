import time
import serial
ser = serial.Serial('/dev/ttyUSB1', 9600) #make connection

x = 0
y = 0
steps = 2000

def waitfordone(serial):
	while (True):
		serialmsg = serial.readline().decode('UTF-8')
		print(serialmsg)
		if ("Done" in serialmsg):
			return 0 # no error
		elif ("Zero Error" in serialmsg):
			return 1 #error



def goto(newX, newY, carying):
	dx = newX - x
	dy = newY - y
	xfb = "f" if (dx > 0) else "b"
	yfb = "f" if (dy > 0) else "b"
	if(dx == dy or not carying):
		ser.write(bytes(xfb+str(abs(dx*steps))+"\n", 'UTF-8'))
		#ser2.write(bytes(yfb+str(abs(dy*steps))+"\n", 'UTF-8'))
		print("Other Motor Running")
		if (waitfordone(ser) == 1):
			print("Error - Reseting Table")
			zero()
	
	else:
		ser.write(bytes(xfb+str(abs(dx*steps))+"\n", 'UTF-8'))
		if (waitfordone(ser) == 1):
			print("Error - Reseting Table")
			zero()
		#ser2.write(bytes(yfb+str(abs(dy*steps))+"\n", 'UTF-8'))
		#if (waitfordone(ser) == 1):
			#print("Error - Reseting Table")
			#zero()
		print("Other Motor Sarting")
		time.sleep(1)
		print("Other Motor Done")
	x = newX
	y = newY

def zero():
	print("Zeroing")
	ser.write(bytes("zero\n", 'UTF-8'))
	print(waitfordone(ser))
	x = 0
	y = 0

time.sleep(1.5)
zero()
while True:
	print("At: " + str(x)+ ","+str(y))
	newX = int(input("New X: "))
	newY = int(input("New Y: "))
	cary = input("Carying? (y/n): ")
	carying = True if (cary.lower() == "y") else False
	goto(newX, newY, carying)
	
	
