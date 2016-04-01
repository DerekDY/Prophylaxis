from game import *

#GameMode Input
gameMode = input(
        "Choose Game Mode \n   1 - Human vs AI \n   2 - Human vs Bluetooth \n   3 - Bluetooth vs AI \n   4 - Human vs Human \n")

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

#print("gameMode: ")
#print(gameMode)

#Motor Input
testingOption = input(
            "Are Motors Contected?[y/n]? ").lower()
testingOption = 0 if testingOption == "y" else 1

<<<<<<< HEAD
=======
#Voice Control Input
voiceOption = input(
            "Is Voice Control Being Used?[y/n]? ").lower()
voiceOption = 0 if voiceOption == "y" else 1
if voiceOption == 0:
    voiceOption2 = input(
                "How Many Players are Using Voice Control?[1/2]? ")
    voiceOption2 = 2 if voiceOption2 == "2" else 1

#Bluetooth Input
>>>>>>> bb847f689d18231a02e61d36829320d026207be4
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

