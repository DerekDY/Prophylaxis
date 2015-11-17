from Coordinate import Coordinate as C


WHITE = True
BLACK = False

class Captured:


    def __init__(self, pieceType, side, position, number):
        self.type = pieceType
        self.side = side
        self.position = position
        self.number = number