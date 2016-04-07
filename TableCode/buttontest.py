import time
#from button import *
from buttonListener import *

b = ButtonListener(21)
'''
if b.waitForPress(5):
    print "button pressed"
else:
    print "button timeout"
#b.buttonTest()
b.startListener()
while True:
    if b.wasPressed():
        print "button pressed"
        b.stopListener()
        b.startListener()
    else:
        print "not pressed"
    time.sleep(1)
'''
sleepTime = 1
Buttoninput = input( " 1 - 1 second response \n 2 - 0.5 second response \n 3 - continuous response")
if Buttoninput == '1':
    sleepTime = 1
elif Buttoninput == '2':
    sleepTime = 0.5
else:
    sleepTime = 0
    
b.startListener()
while True:
    if b.wasPressed():
        print("button pressed")
        b.stopListener()
        b.startListener()
    else:
        print("button released")
        
    time.sleep(sleepTime)
