#language:Python
# External module imports
import RPi.GPIO as GPIO
import time

#Pin Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.IN)
time.sleep(1)

'''

p = GPIO.PWM(21, 4000)

time.sleep(1)
p.start(25)
time.sleep(10)

time.sleep(0.1)
p.ChangeFrequency(50000)
time.sleep(0.1)
p.ChangeFrequency(45000)
time.sleep(0.1)
p.ChangeFrequency(40000)
time.sleep(0.1)
p.ChangeFrequency(35000)
time.sleep(0.1)
p.ChangeFrequency(30000)
time.sleep(0.1)
p.ChangeFrequency(25000)
time.sleep(0.1)
p.ChangeFrequency(60000)

#input('Press return to stop...')

def stop_event():
	print('test3')
	p.stop(1)
'''



startFrequency = 500
frequency = 0
rotation = 1998
while(1):
	turns = int(input("Number of Rotations (0 to Stop): "))
	count = 0
	if(turns == 0):
		break
	frequency = startFrequency
	p = GPIO.PWM(21, frequency)
	p.start(25)
	while(count <= turns*rotation):
		GPIO.wait_for_edge(20, GPIO.RISING)
		if (count > (rotation*turns) - 249):
			frequency -= 10
		elif (frequency < startFrequency + 2000):
			frequency += 10
		p.ChangeFrequency(frequency)
		count += 1
	p.stop()
GPIO.cleanup()

'''
Testing:

freq	dc	revs
10000	1	19.25	
10000	1	19.50
10000	1	19.75
10000	1	19.25

10000	95	18 7/8
10000	5	19 7/8
10000	25	20 1/4
10000	25	20 1/3

Notes:
-can only change duty cycle after p.start() otherwise it will have no effect

'''



