from game import *
 
game = Game()
game.askForPlayerSide()
print()
game.askForDepthOfAI()
game.ai = AI(game.board, not game.playerSide, game.aiDepth)

try:
    game.startGame()
except KeyboardInterrupt:
    sys.exit()
