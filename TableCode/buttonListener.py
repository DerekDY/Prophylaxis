import RPi.GPIO as GPIO
import threading

class ButtonListener():

    def __init__(self, pin):
        self.myPin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.myPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def startListener(self):
        self.myThread = threading.Thread(target=self.listen, args=[])
        self.myThread.daemon = True  # exits with main thread just in case
        self.buttonPressed = False
        self.exitFlag = False
        self.myThread.start()

    def stopListener(self):
        self.exitFlag = True
        self.myThread.join()

    def listen(self):
        while not self.exitFlag:
            if GPIO.input(self.myPin):
                self.buttonPressed = True

    def reset(self):
        self.buttonPressed = False

    def wasPressed(self):
        return self.buttonPressed