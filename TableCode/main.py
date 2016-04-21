import time
from game import *
from ledmatrix import *
from buttonListener import *


table = ChessTable(1)
print("Table Made")



led = int(input(
        "Is LED Matrix Connected?\n   1 - Yes \n   2 - No \n"))
#GameMode Input

ledOption = False if led == 2 else True

if ledOption == False:
    gameMode = int(input(
        "Choose Game Mode \n   1 - Human vs AI \n   2 - Human vs Bluetooth \n   3 - Bluetooth vs AI \n   4 - Human vs Human \n"))
        
        
#Button Setup
pin1 = 19   
pin2 = 21
pin3 = 13   #not being used 
selectButton = ButtonListener(pin1)
scrollButton = ButtonListener(pin2)
newGameButton = ButtonListener(pin3)

'''
#New Game and Title Screen
newGameButton.startListener()
while True:
    if newGameButton.wasPressed():
        print("New Game Button was Pressed")
        newGameButton.stopListener()
        break
    else:
        table.ledMatrix.display("The","Knight")
        time.sleep(3)
        table.ledMatrix.display("Press", "NewGame")
'''

print(ledOption)
if ledOption:
    table.ledMatrix.sendString("logo")      #switch with draw logo
    time.sleep(3)
    table.ledMatrix.sendString("clear")
    
    #Game Mode Selection using LED Display
    table.ledMatrix.sendMultLines("PICK","MODE") 
    
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
                table.ledMatrix.sendMultLines("HUMAN","V AI")
            elif scrollCount == 2:
                table.ledMatrix.sendMultLines("HUMAN","V APP")
            elif scrollCount == 3:
                table.ledMatrix.sendMultLines("APP","V AI")
            elif scrollCount == 4:
                table.ledMatrix.sendMultLines("HUMAN","HUM")
            else:
                table.ledMatrix.sendMultLines("PICK","MODE")  
                
        if selectButton.wasPressed():
            print("Select Button was Pressed")
            if scrollCount == 0:
                selectButton.stopListener()
                time.sleep(sleepTime)
                selectButton.startListener()
                table.ledMatrix.sendMultLines("ERROR","IDIOT") 
                print("Error Handeling")
                print(scrollCount)
            else:
                table.ledMatrix.sendString("clear")
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
    
    
print("gameMode: ")
print(gameMode)

'''
#Motor Input
testingOption = input(
            "Are Motors Contected?[y/n]? ").lower()
testingOption = 0 if testingOption == "y" else 1
'''
'''
if ledOption:
table.ledMatrix.clear
time.sleep(sleepTime)
table.ledMatrix.display("MOTORS","[Y/N]?",fontColor, normFont)  
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
            table.ledMatrix.display("  YES", "", fontColor, normFont)
        elif scrollCount == 2:
            table.ledMatrix.display("  NO", "", fontColor, normFont)
        else:
            table.ledMatrix.display("MOTORS","[Y/N]?", fontColor, normFont)  
            
    if selectButton.wasPressed():
        print("Select Button was Pressed")
        table.ledMatrix.clear()
        motorOption = scrollCount
        print("Motor Option")
        print(motorOption)
        testingOption = 0 if motorOption == 1 else 1
        break
        
print("Testing Option: ")
print(testingOption)
'''
testingOption = 1
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
table.ledMatrix.clear
table.ledMatrix.display("VOICE","[Y/N]?",fontColor, normFont)  
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
            table.ledMatrix.display("", " YES", fontColor, normFont)
        elif scrollCount == 2:
            table.ledMatrix.display("", "  NO", fontColor, normFont)
        else:
            table.ledMatrix.display("VOICE","[Y/N]?", fontColor, normFont)  
            
    if selectButton.wasPressed():
        print("Select Button was Pressed")
        table.ledMatrix.clear()
        voiceOption = scrollCount
        print(motorOption)
        voiceOption = 0 if voiceOption == '1' else 1
        break

print("Voice Option: ")
print(voiceOption) 
 
if voiceOption == 0:        
    table.ledMatrix.clear
    table.ledMatrix.display("VOICE","[1/2]?",fontColor, normFont)  
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
                table.ledMatrix.display("  ONE", "   1", fontColor, normFont)
            elif scrollCount == 2:
                table.ledMatrix.display("  TWO", "   2", fontColor, normFont)
            else:
                table.ledMatrix.display("VOICE","[1/2]?", fontColor, normFont)  
                
        if selectButton.wasPressed():
            print("Select Button was Pressed")
            table.ledMatrix.clear()
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
'''
if btOption == 1:
    print("Bluetooth is off")
else:
    print("Bluetooth is on")
'''
    
#Set Up Game
game = Game(table, testingOption, btOption, gameMode, led = ledOption)
game.askForPlayerSide()
print()
if gameMode != 2 and gameMode != 4:
    game.askForDepthOfAI()
    game.ai = AI(game.board, not game.playerSide, game.aiDepth)

try:
    game.startGame()
except KeyboardInterrupt:
    sys.exit()

