from game import *


testingOption = input(
            "Are Motors Contected?[y/n]? ").lower()
testingOption = 0 if testingOption == "y" else 1

game = Game(testingOption)
game.askForPlayerSide()
print()
game.askForDepthOfAI()
game.ai = AI(game.board, not game.playerSide, game.aiDepth)

try:
    game.startGame()
except KeyboardInterrupt:
    sys.exit()

