import time
from game import *
from ledmatrix import *
from buttonListener import *

'''
#GameMode Input
gameMode = input(
        "Choose Game Mode \n   1 - Human vs AI \n   2 - Human vs Bluetooth \n   3 - Bluetooth vs AI \n   4 - Human vs Human \n")
'''

#Button Setup
pin1 = 19   
pin2 = 21
pin3 = 13   #not being used 
selectButton = ButtonListener(pin1)
scrollButton = ButtonListener(pin2)
newGameButton = ButtonListener(pin3)
  
#LED Display Setup  
ledMatrix = LEDMatrix()
smallFont = "/home/pi/Prophylaxis/rpi-rgb-led-matrix/fonts/4x6.bdf"
normFont = "/home/pi/Prophylaxis/rpi-rgb-led-matrix/fonts/5x8.bdf"
bigFont = "/home/pi/Prophylaxis/rpi-rgb-led-matrix/fonts/6x10.bdf"
fontColor = "135, 206, 250"
errorColor = "255,0,0"

'''
#New Game and Title Screen
newGameButton.startListener()
while True:
    if newGameButton.wasPressed():
        print("New Game Button was Pressed")
        newGameButton.stopListener()
        break
    else:
        ledMatrix.display("The","Knight")
        time.sleep(3)
        ledMatrix.display("Press", "NewGame")
'''

ledMatrix.draw_logo(2)
  
selectButton.startListener()

#Process Setup
mProcess = Process(target=ledMatrix.refresh, args=())
mProcess.start()
while(True):
    if selectButton.wasPressed():
        print("Select Button was Pressed")
        mProcess.terminate()
        break
mProcess.join()


time.sleep(3)
ledMatrix.clear()


#Game Mode Selection using LED Display
ledMatrix.clear()
ledMatrix.display(" CHOOSE","  MODE",fontColor, smallFont)  
scrollButton.startListener()
selectButton.startListener()
scrollCount = 0
sleepTime = 0.3
while True:
    if scrollButton.wasPressed():
        scrollButton.stopListener()
        time.sleep(sleepTime)
        scrollButton.startListener()
        scrollCount = scrollCount + 1
        if scrollCount == 5:
            scrollCount = 1
        print("Scroll Button was Pressed")
        print(scrollCount)
        scrollButton.stopListener()
        scrollButton.startListener()
        if scrollCount == 1:
            ledMatrix.display("HUMAN", "V AI", fontColor, normFont)
        elif scrollCount == 2:
            ledMatrix.display("HUMAN", "V APP", fontColor, normFont)
        elif scrollCount == 3:
            ledMatrix.display("APP", "V AI", fontColor, normFont)
        elif scrollCount == 4:
            ledMatrix.display("HUMAN", "v HUMAN", fontColor, smallFont)
        else:
            ledMatrix.display("CHOOSE"," MODE", fontColor, normFont)  
            
    if selectButton.wasPressed():
        print("Select Button was Pressed")
        if scrollCount == 0:
            selectButton.stopListener()
            time.sleep(sleepTime)
            selectButton.startListener()
            ledMatrix.display("ERROR","IDIOT", errorColor, bigFont)
            print("Error Handeling")
            print(scrollCount)
        else:
            ledMatrix.clear()
            gameMode = scrollCount
            print(gameMode)
            break

if gameMode == 1:
    btOption = 1
elif gameMode == 2:
    btOption = 0
elif gameMode == 3:
    btOption = 0
else:
    btOption = 1


'''
if gameMode == "1":
    gameMode = 1
    btOption = 1
elif gameMode == "2":
    gameMode = 2
    btOption = 0
elif gameMode == "3":
    gameMode = 3
    btOption = 0
else:
    gameMode = 4
    btOption = 0
'''

print("gameMode: ")
print(gameMode)

'''
#Motor Input
testingOption = input(
            "Are Motors Contected?[y/n]? ").lower()
testingOption = 0 if testingOption == "y" else 1
'''

ledMatrix.clear
time.sleep(sleepTime)
ledMatrix.display("MOTORS","[Y/N]?",fontColor, normFont)  
scrollButton.startListener()
selectButton.startListener()
scrollCount = 0
sleepTime = 0.3
while True:
    if scrollButton.wasPressed():
        scrollButton.stopListener()
        time.sleep(sleepTime)
        scrollButton.startListener()
        scrollCount = scrollCount + 1
        if scrollCount == 3:
            scrollCount = 1
        print("Scroll Button was Pressed")
        print(scrollCount)
        scrollButton.stopListener()
        scrollButton.startListener()
        if scrollCount == 1:
            ledMatrix.display("  YES", "", fontColor, normFont)
        elif scrollCount == 2:
            ledMatrix.display("  NO", "", fontColor, normFont)
        else:
            ledMatrix.display("MOTORS","[Y/N]?", fontColor, normFont)  
            
    if selectButton.wasPressed():
        print("Select Button was Pressed")
        ledMatrix.clear()
        motorOption = scrollCount
        print("Motor Option")
        print(motorOption)
        testingOption = 0 if motorOption == 1 else 1
        break
        
print("Testing Option: ")
print(testingOption)

'''
#Voice Control Input
voiceOption = input(
            "Is Voice Control Being Used?[y/n]? ").lower()
voiceOption = 0 if voiceOption == "y" else 1
if voiceOption == 0:
    voiceOption2 = input(
                "How Many Players are Using Voice Control?[1/2]? ")
    voiceOption2 = 2 if voiceOption2 == "2" else 1
'''
'''
ledMatrix.clear
ledMatrix.display("VOICE","[Y/N]?",fontColor, normFont)  
scrollButton.startListener()
selectButton.startListener()
scrollCount = 0
sleepTime = 0.3
while True:
    if scrollButton.wasPressed():
        scrollButton.stopListener()
        time.sleep(sleepTime)
        scrollButton.startListener()
        scrollCount = scrollCount + 1
        if scrollCount == 3:
            scrollCount = 1
        print("Scroll Button was Pressed")
        print(scrollCount)
        scrollButton.stopListener()
        scrollButton.startListener()
        if scrollCount == 1:
            ledMatrix.display("", " YES", fontColor, normFont)
        elif scrollCount == 2:
            ledMatrix.display("", "  NO", fontColor, normFont)
        else:
            ledMatrix.display("VOICE","[Y/N]?", fontColor, normFont)  
            
    if selectButton.wasPressed():
        print("Select Button was Pressed")
        ledMatrix.clear()
        voiceOption = scrollCount
        print(motorOption)
        voiceOption = 0 if voiceOption == '1' else 1
        break

print("Voice Option: ")
print(voiceOption) 
 
if voiceOption == 0:        
    ledMatrix.clear
    ledMatrix.display("VOICE","[1/2]?",fontColor, normFont)  
    scrollButton.startListener()
    selectButton.startListener()
    scrollCount = 0
    sleepTime = 0.3
    while True:
        if scrollButton.wasPressed():
            scrollButton.stopListener()
            time.sleep(sleepTime)
            scrollButton.startListener()
            scrollCount = scrollCount + 1
            if scrollCount == 3:
                scrollCount = 1
            print("Scroll Button was Pressed")
            print(scrollCount)
            scrollButton.stopListener()
            scrollButton.startListener()
            if scrollCount == 1:
                ledMatrix.display("  ONE", "   1", fontColor, normFont)
            elif scrollCount == 2:
                ledMatrix.display("  TWO", "   2", fontColor, normFont)
            else:
                ledMatrix.display("VOICE","[1/2]?", fontColor, normFont)  
                
        if selectButton.wasPressed():
            print("Select Button was Pressed")
            ledMatrix.clear()
            voiceOption = scrollCount
            print(motorOption)
            voiceOption = 1 if voiceOption == '1' else 2
            break
        
print("Voice Option: ")
print(voiceOption)
'''

#Bluetooth Input
'''
btOption = input(
            "BlueTooth On?[y/n]? ").lower()
btOption = 0 if btOption == "y" else 1
'''
if btOption == 1:
    print("Bluetooth is off")
else:
    print("Bluetooth is on")

    
#Set Up Game
game = Game(testingOption, btOption, gameMode)
game.askForPlayerSide()
print()
if gameMode != 2 and gameMode != 4:
    game.askForDepthOfAI()
    game.ai = AI(game.board, not game.playerSide, game.aiDepth)

try:
    game.startGame()
except KeyboardInterrupt:
    sys.exit()

