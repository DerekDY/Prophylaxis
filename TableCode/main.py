import time
from game import *
from ledmatrix import *
from buttonListener import *
import sys
import os



table = ChessTable(1)
print("Table Made")


'''
led = int(input(
        "Is LED Matrix Connected?\n   1 - Yes \n   2 - No \n"))
#GameMode Input
'''
led = 1
ledOption = False if led == 2 else True

'''
reedBoard = int(input(
        "Is Reed Board Connected?\n   1 - Yes \n   2 - No \n"))
#GameMode Input
'''
reedBoard = 1
reedOption = False if reedBoard == 2 else True

while True:
    
    
    if ledOption == False:
        gameMode = int(input(
            "Choose Game Mode \n   1 - Human vs AI \n   2 - Human vs Bluetooth \n   3 - Bluetooth vs AI \n   4 - Human vs Human \n"))
            
            
    #Button Setup
    selectButton = ButtonListener2(15)
    scrollButton = ButtonListener2(14)
    print(ledOption)
    if ledOption:
        table.ledMatrix.sendString("logo")
        time.sleep(1)
        
        table.ledMatrix.sendString("clear")
        
        #Game Mode Selection using LED Display
        table.ledMatrix.sendMultLines("@PICK","MODE") 
        
        scrollButton.startListener()
        selectButton.startListener()
        scrollCount = 0
        sleepTime = 0.5
        while True:
            if scrollButton.wasPressed():
                scrollButton.stopListener()
                scrollCount = scrollCount + 1
                print("Scroll Button was Pressed")
                print(scrollCount)
                if scrollCount == 3:
                    scrollCount = 4
                if scrollCount == 1:
                    table.ledMatrix.sendMultLines("HUMAN","V AI")
                elif scrollCount == 2:
                    table.ledMatrix.sendMultLines("HUMAN","V APP")
                elif scrollCount == 3:
                    table.ledMatrix.sendMultLines("APP","V AI")
                elif scrollCount == 4:
                    table.ledMatrix.sendMultLines("HUMAN","HUMAN")
                elif scrollCount == 5:
                    table.ledMatrix.sendMultLines("DEMO","MODE")
                elif scrollCount == 6:
                    table.ledMatrix.sendMultLines("!TURN","OFF")
                else:
                    table.ledMatrix.sendMultLines("HUMAN","V AI")
                    scrollCount = 1  
                time.sleep(sleepTime)
                scrollButton.startListener()    
            if selectButton.wasPressed():
                print("Select Button was Pressed")
                if scrollCount == 0:
                    selectButton.stopListener()
                    selectButton.startListener()
                    continue
                else:
                    if scrollCount == 6:
                        table.ledMatrix.sendMultLines("!SHUT","DOWN")
                        time.sleep(1)
                        table.ledMatrix.sendMultLines("!IN","5 SEC")
                        time.sleep(2)
                        table.ledMatrix.sendString("clear")
                        os.system("sudo shutdown -h now")
                        sys.exit(0)
                    table.ledMatrix.sendString("clear")
                    gameMode = scrollCount
                    print(gameMode)
                    selectButton.stopListener()
                    scrollButton.stopListener()
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
    testingOption = 1
        
    #Set Up Game
    game = Game(table, testingOption, btOption, gameMode, led = ledOption, reedBoard = reedOption)
    game.askForPlayerSide()
    print()
    if gameMode != 2 and gameMode != 4:
        game.askForDepthOfAI()

    try:
        if ledOption:
            selectButton.stopListener()
            scrollButton.stopListener()
        game.startGame()
    except KeyboardInterrupt:
        sys.exit()

