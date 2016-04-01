from game import *


gameMode = input(
        "Choose Game Mode \n   1 - Human vs AI \n   2 - Human vs Bluetooth \n   3 - Bluetooth vs AI \n")

if gameMode == "1":
    gameMode = 1
    btOption = 1
elif gameMode == "2":
    gameMode = 2
    btOption = 0
else:
    gameMode = 3
    btOption = 0

#print("gameMode: ")
#print(gameMode)

testingOption = input(
            "Are Motors Contected?[y/n]? ").lower()
testingOption = 0 if testingOption == "y" else 1

'''
btOption = input(
            "BlueTooth On?[y/n]? ").lower()
btOption = 0 if btOption == "y" else 1
'''

if btOption == 1:
    print("Bluetooth is off")
else:
    print("Bluetooth is on")

game = Game(testingOption, btOption, gameMode)
game.askForPlayerSide()
print()
if gameMode != 2:
    game.askForDepthOfAI()
    game.ai = AI(game.board, not game.playerSide, game.aiDepth)

try:
    game.startGame()
except KeyboardInterrupt:
    sys.exit()

