#language:Python
# External module imports
import RPi.GPIO as GPIO
import time

rotation = 1998
maxFreq = 8000
unitRotations = 1
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class Motor:

	def __init__(self, step, dir, cnt):
		print ("Motor was made")
		GPIO.setup(step, GPIO.OUT)
		GPIO.setup(dir, GPIO.OUT)
		GPIO.setup(cnt, GPIO.IN)
		self.frequency = 500
		self.pcnt = cnt
		self.dir = dir
		self.pstep = GPIO.PWM(step, self.frequency)
		GPIO.add_event_detect(self.pcnt, GPIO.RISING)


	def cw(self, dist):
		GPIO.output(self.dir, GPIO.LOW) 
		steps = dist * unitRotations * rotation
		count = 0
		freq = self.frequency
		self.pstep.start(25) 
		while(count < steps):
			if(GPIO.event_detected(self.pcnt)):	
				if(count > steps - 249):
					freq -= 10
				elif (freq < maxFreq):
					freq+= 10
				self.pstep.ChangeFrequency(freq)
				count += 1
		print(count)
		print(steps)
		self.pstep.stop()
		
			
			
	def ccw(self, dist):
		GPIO.output(self.dir, GPIO.HIGH)
		steps = dist * unitRotations  * rotation
		count = 0
		freq = self.frequency
		self.pstep.start(25) 
		while(count < steps):
			if(GPIO.event_detected(self.pcnt)):
				if(count > steps - 249):
					freq -= 10
				elif (freq < maxFreq):
					freq += 10
				self.pstep.ChangeFrequency(freq)
				count += 1
		print(count)
		print(steps)
		self.pstep.stop()
				
			
	


	