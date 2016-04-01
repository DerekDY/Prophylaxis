from Rook import Rook
from Bishop import Bishop
from Knight import Knight
from Queen import Queen

from Piece import Piece
from Coordinate import Coordinate as C
from Move import Move

WHITE = True
BLACK = False


class Pawn(Piece):

    stringRep = 'p'
    value = 1

    def __init__(self, board, side, position, number, movesMade=0 ):
        super(Pawn, self).__init__(board, side, position, number)
        self.movesMade = movesMade

    # @profile
    def getPossibleMoves(self):
        currentPosition = self.position

        # Pawn moves one up
        movement = C(0, 1) if self.side == WHITE else C(0, -1)
        advanceOnePosition = currentPosition + movement
        if self.board.isValidPos(advanceOnePosition):
            #Check if piece at position to move to
            if self.board.pieceAtPosition(advanceOnePosition) is None:
                col = advanceOnePosition[1]
                if col == 7 or col == 0:
                    #print("promotion is happening without a capture")
                    '''
                    piecesForPromotion = \
                        [Rook(self.board, self.side, advanceOnePosition, self.number),      #added self.number to these
                         Knight(self.board, self.side, advanceOnePosition, self.number),
                         Bishop(self.board, self.side, advanceOnePosition, self.number),
                         Queen(self.board, self.side, advanceOnePosition, self.number)]
                    for piece in piecesForPromotion:
                    '''
                    move = Move(self, advanceOnePosition)
                    move.promotion = True
                    move.specialMovePiece = Queen(self.board, self.side, advanceOnePosition, self.number)
                    #print(move.specialMovePiece)
                    #print(move)
                    yield (move)
                else:
                    yield (Move(self, advanceOnePosition))

        # Pawn moves two up
        if self.movesMade == 0:
            movement = C(0, 2) if self.side == WHITE else C(0, -2)
            advanceTwoPosition = currentPosition + movement
            if self.board.isValidPos(advanceTwoPosition):
                if self.board.pieceAtPosition(advanceTwoPosition) is None and \
                   self.board.pieceAtPosition(advanceOnePosition) is None:
                    yield Move(self, advanceTwoPosition)

        # Pawn takes
        movements = [C(1, 1), C(-1, 1)] \
            if self.side == WHITE else [C(1, -1), C(-1, -1)]
        
        # Pawn captures another piece
        for m in movements:
            newPosition = self.position + m
            if self.board.isValidPos(newPosition):
                pieceToTake = self.board.pieceAtPosition(newPosition)
                if pieceToTake and pieceToTake.side != self.side:
                    col = newPosition[1]
                    #print("Piece for pawn to take: ")
                    #print(pieceToTake)
                    #print(pieceToTake.board)
                    
                    # Promotion with a capture
                    if col == 7 or col == 0:
                        #print("promotion is happening with capture")
                        '''
                        piecesForPromotion = \
                            [Knight(self.board, self.side, newPosition, self.number),
                             Rook(self.board, self.side, newPosition, self.number),
                             Bishop(self.board, self.side, newPosition, self.number),
                             Queen(self.board, self.side, newPosition, self.number)]
                        for piece in piecesForPromotion:
                        '''
                        move = Move(self, newPosition, pieceToCapture=pieceToTake)
                        move.promotion = True
                        move.specialMovePiece = Queen(self.board, self.side, newPosition, self.number)
                        #print("reset special move piece")
                        #print(move.specialMovePiece)
                        #print(move)
                        yield (move)
                    else:
                        yield (Move(self, newPosition,
                                   pieceToCapture=pieceToTake))

        # En pessant
        movements = [C(1, 1), C(-1, 1)] \
            if self.side == WHITE else [C(1, -1), C(-1, -1)]
        for movement in movements:
            posBesidePawn = self.position + C(movement[0], 0)
            if self.board.isValidPos(posBesidePawn):
                pieceBesidePawn = self.board.pieceAtPosition(posBesidePawn)
                lastPieceMoved = self.board.getLastPieceMoved()
                lastMoveWasAdvanceTwo = False
                lastMove = self.board.getLastMove()

                if lastMove:
                    if lastMove.newPos - lastMove.oldPos == C(0, 2) or \
                       lastMove.newPos - lastMove.oldPos == C(0, -2):
                        lastMoveWasAdvanceTwo = True

                if pieceBesidePawn and \
                   pieceBesidePawn.stringRep == 'p' and \
                   pieceBesidePawn.side != self.side and \
                   lastPieceMoved is pieceBesidePawn and \
                   lastMoveWasAdvanceTwo:
                    move = Move(self, self.position + movement,
                                pieceToCapture=pieceBesidePawn)
                    move.pessant = True
                    move.specialMovePiece = pieceBesidePawn
                    yield (move)
