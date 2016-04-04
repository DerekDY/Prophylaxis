import time
from button import *
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
b.startListener()
while True:
    if b.wasPressed():
        print "button pressed"
        b.stopListener()
        b.startListener()
    else:
        print "button released"
    time.sleep(3)
