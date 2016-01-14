import time
import serial
ser = serial.Serial('/dev/ttyUSB0', 9600) #make connection

while True:
	userText = input('Send Out: ')
	ser.write(("%s\n" %(userText)).encode())
	time.sleep(.5)
	print(ser.readline().decode('utf-8'))
	time.sleep(1)
	
