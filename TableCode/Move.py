from Coordinate import Coordinate as C

class Move:

    def __init__(self, piece, newPos, pieceToCapture=None, pessant=False):
        self.notation = None
        self.check = False
        self.checkmate = False
        self.kingsideCastle = False
        self.queensideCastle = False
        self.promotion = False
        self.pessant = pessant
        self.stalemate = False

        self.rookMovePos = C(0,0)

        self.piece = piece
        self.oldPos = piece.position
        self.newPos = newPos
        self.pieceToCapture = pieceToCapture
        # For en pessant and castling
        self.specialMovePiece = None
        # For castling
        self.rookMove = None

    def __str__(self):
        displayString = 'Piece Moving : ' + self.piece.stringRep + str(self.piece.number) +\
                        ' Old pos : ' + str(self.oldPos) + \
                        ' -- New pos : ' + str(self.newPos) +\
                        ' --  pieceToCapture: ' +str(self.pieceToCapture)
        if self.notation:
            displayString += ' Notation : ' + self.notation
        if self.pessant:
            displayString = 'Old pos : ' + str(self.oldPos) + \
                            ' -- New pos : ' + str(self.newPos) + \
                            ' -- Pawn taken : ' + str(self.specialMovePiece)
            displayString += ' PESSANT'
        return displayString

    def __eq__(self, other):
        if self.oldPos == other.oldPos and \
           self.newPos == other.newPos and \
           self.specialMovePiece == other.specialMovePiece:
            if not self.specialMovePiece:
                return True
            if self.specialMovePiece and \
               self.specialMovePiece == other.specialMovePiece:
                return True
            else:
                return False
        else:
            return False

    def __hash__(self):
        return hash((self.oldPos, self.newPos))

    def reverse(self):
        return Move(self.piece, self.piece.position,
                    pieceToCapture=self.pieceToCapture)
