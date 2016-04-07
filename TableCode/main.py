from game import *
#from ledmatrix import *
#from button import *
#from buttonListener import *

#GameMode Input
gameMode = input(
        "Choose Game Mode \n   1 - Human vs AI \n   2 - Human vs Bluetooth \n   3 - Bluetooth vs AI \n   4 - Human vs Human \n")
'''
#Button Setup
pin1 = 19
pin2 = 21
pin3 = 23
selectButton = ButtonListener(pin1)
scrollButton = ButtonListener(pin2)
newGameButton = ButtonListener(pin3)
  
#LED Display Setup  
ledMatrix = LEDMatrix()
smallFont = "/fonts/4x6.bdf"
fontColor = "255,205,0")

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
        
#Game Mode Selection using LED Display
ledMatrix.clear
ledMatrix.display("Choose Game Mode","Scroll For Options","fonts/4x6.bdf")  
scrollButton.startListener()
selectButton.startListener()
scrollCount = 0
while True:
    if scrollButton.wasPressed():
        scrollCount = scrollCount + 1
        if scrollCount == 5:
            scrollCount = 1
        print("Scroll Button was Pressed")
        print(scrollCount)
        scrollButton.stopListener()
        scrollButton.startListener()
        if scrollCount == 1:
            ledMatrix.display("Human", "v AI", fontColor)
        elif scrollCount == 2:
            ledMatrix.display("Human", "v App", fontColor)
        elif scrollCount == 3:
            ledMatrix.display("App", "v AI", fontColor)
        elif scrollCount == 4:
            ledMatrix.display("Human", "v Human", fontColor, smallFont)
        else:
            ledMatrix.display("Choose"," Mode")  
            
    if selectButton.wasPressed():
        print("Select Button was Pressed")
        gameMode = scrollCount
        print(gameMode)
        break
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

print("gameMode: ")
print(gameMode)

#Motor Input
testingOption = input(
            "Are Motors Contected?[y/n]? ").lower()
testingOption = 0 if testingOption == "y" else 1

#Voice Control Input
voiceOption = input(
            "Is Voice Control Being Used?[y/n]? ").lower()
voiceOption = 0 if voiceOption == "y" else 1
if voiceOption == 0:
    voiceOption2 = input(
                "How Many Players are Using Voice Control?[1/2]? ")
    voiceOption2 = 2 if voiceOption2 == "2" else 1

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

