import time
from ledmatrix import *
from buttonListener import *

normFont = "/home/pi/Prophylaxis/rpi-rgb-led-matrix/fonts/5x8.bdf"
fontColor = "135, 206, 250"
color = 1

#Button Setup
pin1 = 21   
selectButton = ButtonListener(pin1)
selectButton.startListener()

def test(x,y,sleepTime):
    m = LEDMatrix()
    while(True):
        m.box_circle(x,y,sleepTime,6)
    '''
    m1 = Process(target=box_circle, args=(x, y, sleepTime, 6))
    m1.start()
    time.sleep(sleepTime*16)
    m1.join()
    m1.terminate()

    m1 = Process(target=box_circle, args=(x, y-4, sleepTime, 6))
    m1.start()
    time.sleep(sleepTime*16)
    m1.join()
    m1.terminate()

    m1 = Process(target=box_circle, args=(x-4, y-4, sleepTime, 6))
    m1.start()
    time.sleep(sleepTime*16)
    m1.join()
    m1.terminate()

    m1 = Process(target=box_circle, args=(x-4, y,sleepTime, 6))
    m1.start()
    time.sleep(sleepTime*16)
    m1.join()
    m1.terminate()

    m1 = Process(target=box_circle, args=(x-4, y+4, sleepTime, 6))
    m1.start()
    time.sleep(sleepTime*16)
    m1.join()
    m1.terminate()

    m1 = Process(target=box_circle, args=(x, y+4, sleepTime, 6))
    m1.start()
    time.sleep(sleepTime*16)
    m1.join()
    m1.terminate()

    m1 = Process(target=box_circle, args=(x+4, y+4, sleepTime, 6))
    m1.start()
    time.sleep(sleepTime*16)
    m1.join()
    m1.terminate()

    m1 = Process(target=box_circle, args=(x+4, y, sleepTime, 6))
    m1.start()
    time.sleep(sleepTime*16)
    m1.join()
    m1.terminate()

    m1 = Process(target=box_circle, args=(x+4, y-4, sleepTime, 6))
    m1.start()
    time.sleep(sleepTime*16)
    m1.join()
    m1.terminate()

    m1 = Process(target=box_circle, args=(x, y-4, sleepTime, 6))
    m1.start()
    time.sleep(sleepTime*16)
    m1.join()
    m1.terminate()

    m1 = Process(target=box_circle, args=(x, y, sleepTime, 6))
    m1.start()
    time.sleep(sleepTime*16)
    m1.join()
    m1.terminate()
    '''


x = 12 
y = 4
sleepTime = .1
color = 6


def func1():
    i = 0
    print("In function 1")
    m = LEDMatrix()
    #m1 = Process(target=m.box_circle, args=(x,y,sleepTime,6))
    #m.start()
    while(True):
        m.box_circle(12,4,0.1,6)
        print(i)
        i = i + 1
        if i == 2500:
            print("func1 is complete")
            #m1.join()
            m1.terminate()
            break
    print("m1 has been terminated")


func1()

