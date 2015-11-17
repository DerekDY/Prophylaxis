from Pawn import Pawn
from Rook import Rook
from King import King
from Bishop import Bishop
from Knight import Knight
from Queen import Queen
from Captured import Captured  ### <- finish this 
from Coordinate import Coordinate as C
from termcolor import colored

from Move import Move

WHITE = True
BLACK = False
#array locations for the captured bins 

#[P0 B0]
#[P1 B1]
#[P2 N0]
#[P3 N1]
#[P4 R0] 
#[P5 R1] 
#[P6 Q0] 
#[P7   ] 
#

#   #   #   #   #   #   #   #
#7
#6
#5
#4
#3
#2
#1
#0
## 0  1   2   3   4   5   6   7

B = 0
N = 2
R = 4
Q = 6

class Board:

    def __init__(self, mateInOne=False, castleBoard=False,
                 pessant=False, promotion=False, testing= 0):
        self.pieces = []
        self.whiteCaptured = []
        self.blackCaptured = []
        self.history = []
        self.points = 0
        self.currentSide = WHITE
        self.movesMade = 0
        self.checkmate = False

        #testing 1: normal board 
        if not mateInOne and not castleBoard and not pessant and not promotion and testing < 2:
            self.pieces.extend([Rook(self, BLACK, C(0, 7), 0),
                                Knight(self, BLACK, C(1, 7), 0),
                                Bishop(self, BLACK, C(2, 7), 0),
                                Queen(self, BLACK, C(3, 7), 0),
                                King(self, BLACK, C(4, 7), 0),
                                Bishop(self, BLACK, C(5, 7), 1),
                                Knight(self, BLACK, C(6, 7), 1),
                                Rook(self, BLACK, C(7, 7), 1)])
            for x in range(8):
                self.pieces.append(Pawn(self, BLACK, C(x, 6), x))
            for x in range(8):
                self.pieces.append(Pawn(self, WHITE, C(x, 1), x))
            self.pieces.extend([Rook(self, WHITE, C(0, 0), 0),
                                Knight(self, WHITE, C(1, 0), 0),
                                Bishop(self, WHITE, C(2, 0), 0),
                                Queen(self, WHITE, C(3, 0), 0),
                                King(self, WHITE, C(4, 0), 0),
                                Bishop(self, WHITE, C(5, 0), 1),
                                Knight(self, WHITE, C(6, 0), 1),
                                Rook(self, WHITE, C(7, 0), 1)])

        elif promotion:
            pawnToPromote = Pawn(self, WHITE, C(1, 6), 8)
            pawnToPromote.movesMade = 1
            kingWhite = King(self, WHITE, C(4, 0), 2)
            kingBlack = King(self, BLACK, C(3, 2), 2)
            self.pieces.extend([pawnToPromote, kingWhite, kingBlack])

        elif pessant:
            pawn = Pawn(self, WHITE, C(1, 4), 8)
            pawn2 = Pawn(self, BLACK, C(2, 6), 8)
            kingWhite = King(self, WHITE, C(4, 0), 2)
            kingBlack = King(self, BLACK, C(3, 2), 2)
            self.pieces.extend([pawn, pawn2, kingWhite, kingBlack])
            self.history = []
            self.currentSide = BLACK
            self.points = 0
            self.movesMade = 0
            self.checkmate = False
            firstMove = Move(pawn2, C(2, 4))
            self.makeMove(firstMove)
            self.currentSide = WHITE
            return
        #white pawn being able to capture 1 piece 
        elif testing == 2:
            self.pieces.extend([Bishop(self, BLACK, C(5, 3), 0)])
            self.pieces.extend([Pawn(self, WHITE, C(6, 2), 0)])
        #testing for pawn being able to capture 2 pieces 
        elif testing ==3:
            self.pieces.extend([Bishop(self, BLACK, C(4, 3), 0)])
            self.pieces.extend([Knight(self, BLACK, C(2, 3), 0)])
            self.pieces.extend([Pawn(self, WHITE, C(3, 2), 0)])
        #testing taking a piece that can be captured by 2 pieces
        elif testing ==4:
            self.pieces.extend([Bishop(self, WHITE, C(3, 1), 0)])
            self.pieces.extend([Knight(self, BLACK, C(2, 2), 0)])
            self.pieces.extend([Queen(self, WHITE, C(5, 2), 0)])
        #black queen capturing 1 piece
        elif testing ==5:
            self.pieces.extend([Rook(self, WHITE, C(3, 4), 0)])
            self.pieces.extend([Knight(self, WHITE, C(7, 5), 0)])
            self.pieces.extend([Queen(self, BLACK, C(4, 5), 0)])
        #black castle queen side with scattered pieces
        elif testing ==6:
            self.pieces.extend([Rook(self, BLACK, C(0, 7), 0)])
            self.pieces.extend([King(self, BLACK, C(4, 7), 0)])
            self.pieces.extend([Pawn(self, WHITE, C(2, 3), 0)])
            self.pieces.extend([Pawn(self, WHITE, C(3, 2), 0)])
            self.pieces.extend([Pawn(self, WHITE, C(4, 3), 0)])
            self.pieces.extend([Pawn(self, WHITE, C(5, 2), 0)])
            self.pieces.extend([Pawn(self, WHITE, C(6, 3), 0)])
            self.pieces.extend([Rook(self, WHITE, C(0, 3), 0)])
            
            
    def __str__(self):
        return self.wrapStringRep(self.makeStringRep(self.pieces))

    def undoLastMove(self):
        lastMove, pieceTaken = self.history.pop()

        if lastMove.queensideCastle or lastMove.kingsideCastle:
            king = lastMove.piece
            rook = lastMove.specialMovePiece

            self.movePieceToPosition(king, lastMove.oldPos)
            self.movePieceToPosition(rook, lastMove.rookMove.oldPos)

            king.movesMade -= 1
            rook.movesMade -= 1

        elif lastMove.pessant:
            pawnMoved = lastMove.piece
            pawnTaken = pieceTaken
            self.pieces.append(pawnTaken)
            self.movePieceToPosition(pawnMoved, lastMove.oldPos)
            pawnMoved.movesMade -= 1
            if pawnTaken.side == WHITE:
                self.points += 1
            if pawnTaken.side == BLACK:
                self.points -= 1

        elif lastMove.promotion:
            pawnPromoted = lastMove.piece
            promotedPiece = self.pieceAtPosition(lastMove.newPos)
            self.pieces.remove(promotedPiece)
            self.pieces.append(pawnPromoted)
            if pawnPromoted.side == WHITE:
                self.points -= promotedPiece.value - 1
            elif pawnPromoted.side == BLACK:
                self.points += promotedPiece.value - 1
            pawnPromoted.movesMade -= 1

        else:
            pieceToMoveBack = lastMove.piece
            self.movePieceToPosition(pieceToMoveBack, lastMove.oldPos)
            if pieceTaken:
                if pieceTaken.side == WHITE:
                    self.points += pieceTaken.value
                if pieceTaken.side == BLACK:
                    self.points -= pieceTaken.value
                self.addPieceToPosition(pieceTaken, lastMove.newPos)
                self.pieces.append(pieceTaken)
            pieceToMoveBack.movesMade -= 1

        self.currentSide = not self.currentSide

    def isCheckmate(self):
        if len(self.getAllMovesLegal(self.currentSide)) == 0:
            for move in self.getAllMovesUnfiltered(not self.currentSide):
                pieceToTake = move.pieceToCapture
                if pieceToTake and pieceToTake.stringRep == "K":
                    return True
        return False

    def isStalemate(self):
        if len(self.getAllMovesLegal(self.currentSide)) == 0:
            for move in self.getAllMovesUnfiltered(not self.currentSide):
                pieceToTake = move.pieceToCapture
                if pieceToTake and pieceToTake.stringRep == "K":
                    return False
            return True
        return False

    def getLastMove(self):
        if self.history:
            return self.history[-1][0]

    def getLastPieceMoved(self):
        if self.history:
            return self.history[-1][0].piece

    def addMoveToHistory(self, move):
        pieceTaken = None
        if move.pessant:
            pieceTaken = move.specialMovePiece
            self.history.append([move, pieceTaken])
            return
        pieceTaken = move.pieceToCapture
        if pieceTaken:
            self.history.append([move, pieceTaken])
            return

        self.history.append([move, None])

    def getCurrentSide(self):
        return self.currentSide

    def makeStringRep(self, pieces):
        stringRep = ''
        for y in range(7, -1, -1):
            for x in range(8):
                piece = None
                for p in pieces:
                    if p.position == C(x, y):
                        piece = p
                        break
                pieceRep = ''
                if piece:
                    side = piece.side
                    #color = 'blue' if side == WHITE else 'red'
                    pieceRep = piece.stringRep.upper() if side == WHITE else piece.stringRep.lower()
                    #pieceRep = piece.stringRep
                else:
                    pieceRep = 'x'
                stringRep += pieceRep + ' '
            stringRep += '\n'
        stringRep = stringRep.strip()
        return stringRep

    '''This was written by Derek'''
    def makeStringRepBin(self, bin):
        stringRep = ''
        for y in range(8):
            for x in range(2):
                piece = None
                for p in bin:
                    if p.position == C(x, y):
                        piece = p
                        break
                pieceRep = ''
                if piece:
                    pieceRep = piece.type + str(piece.number)
                else:
                    pieceRep = 'xx'
                stringRep += pieceRep + ' '
            stringRep += '\n'
        stringRep = stringRep.strip()
        return stringRep

    def wrapStringRep(self, stringRep):
        sRep = '\n'.join(
            ['   a b c d e f g h   ', ' '*21] +
            ['%d  %s  %d' % (8-r, s.strip(), 8-r)
             for r, s in enumerate(stringRep.split('\n'))] +
            [' '*21, '   a b c d e f g h   ']
            ).rstrip()
        return sRep

    def rankOfPiece(self, piece):
        return str(piece.position[1] + 1)

    def fileOfPiece(self, piece):
        transTable = str.maketrans('01234567', 'abcdefgh')
        return str(piece.position[0]).translate(transTable)

    def getShortNotationOfMove(self, move):
        notation = ""
        pieceToMove = move.piece
        pieceToTake = move.pieceToCapture

        if move.queensideCastle:
            return "0-0-0"

        if move.kingsideCastle:
            return "0-0"

        if pieceToMove.stringRep != 'p':
            notation += pieceToMove.stringRep

        if pieceToTake is not None:
            if pieceToMove.stringRep == 'p':
                notation += self.fileOfPiece(pieceToMove)
            notation += 'x'

        notation += self.positionToHumanCoord(move.newPos)

        if move.promotion:
            notation += "=" + str(move.specialMovePiece.stringRep)

        return notation

    def getShortNotationOfMoveWithFile(self, move):
        # TODO: Use self.getShortNotationOfMove instead of repeating code
        notation = ""
        pieceToMove = self.pieceAtPosition(move.oldPos)
        pieceToTake = self.pieceAtPosition(move.newPos)

        if pieceToMove.stringRep != 'p':
            notation += pieceToMove.stringRep
            notation += self.fileOfPiece(pieceToMove)

        if pieceToTake is not None:
            notation += 'x'

        notation += self.positionToHumanCoord(move.newPos)
        return notation

    def getShortNotationOfMoveWithRank(self, move):
        # TODO: Use self.getShortNotationOfMove instead of repeating code
        notation = ""
        pieceToMove = self.pieceAtPosition(move.oldPos)
        pieceToTake = self.pieceAtPosition(move.newPos)

        if pieceToMove.stringRep != 'p':
            notation += pieceToMove.stringRep
            notation += self.rankOfPiece(pieceToMove)

        if pieceToTake is not None:
            notation += 'x'

        notation += self.positionToHumanCoord(move.newPos)
        return notation

    def getShortNotationOfMoveWithFileAndRank(self, move):
        # TODO: Use self.getShortNotationOfMove instead of repeating code
        notation = ""
        pieceToMove = self.pieceAtPosition(move.oldPos)
        pieceToTake = self.pieceAtPosition(move.newPos)

        if pieceToMove.stringRep != 'p':
            notation += pieceToMove.stringRep
            notation += self.fileOfPiece(pieceToMove)
            notation += self.rankOfPiece(pieceToMove)

        if pieceToTake is not None:
            notation += 'x'

        notation += self.positionToHumanCoord(move.newPos)
        return notation
        return

    def humanCoordToPosition(self, coord):
        transTable = str.maketrans('abcdefgh', '12345678')
        coord = coord.translate(transTable)
        coord = [int(c)-1 for c in coord]
        pos = C(coord[0], coord[1])
        return pos

    def positionToHumanCoord(self, pos):
        transTable = str.maketrans('01234567', 'abcdefgh')
        notation = str(pos[0]).translate(transTable) + str(pos[1]+1)
        return notation

    def isValidPos(self, pos):
        if 0 <= pos[0] <= 7 and 0 <= pos[1] <= 7:
            return True
        else:
            return False

    def getSideOfMove(self, move):
        return move.piece.side

    def getPositionOfPiece(self, piece):
        for y in range(8):
            for x in range(8):
                if self.boardArray[y][x] is piece:
                    return C(x, 7-y)

    def pieceAtPosition(self, pos):
        for piece in self.pieces:
            if piece.position == pos:
                return piece

    def movePieceToPosition(self, piece, pos):
        piece.position = pos

    def addPieceToPosition(self, piece, pos):
        piece.position = pos

    def clearPosition(self, pos):
        x, y = self.coordToLocationInArray(pos)
        self.boardArray[x][y] = None

    def coordToLocationInArray(self, pos):
        return (7-pos[1], pos[0])

    def locationInArrayToCoord(self, loc):
        return (loc[1], 7-loc[0])

    def makeMove(self, move):
        self.addMoveToHistory(move)
        if move.kingsideCastle or move.queensideCastle:
            kingToMove = move.piece
            rookToMove = move.specialMovePiece
            self.movePieceToPosition(kingToMove, move.newPos)
            self.movePieceToPosition(rookToMove, move.rookMovePos)
            kingToMove.movesMade += 1
            rookToMove.movesMade += 1

        elif move.pessant:
            pawnToMove = move.piece
            pawnToTake = move.specialMovePiece
            pawnToMove.position = move.newPos
            self.pieces.remove(pawnToTake)
            pawnToMove.movesMade += 1

        elif move.promotion:
            self.pieces.remove(move.piece)
            self.pieces.append(move.specialMovePiece)
            if move.piece.side == WHITE:
                self.points += move.specialMovePiece.value - 1
            if move.piece.side == BLACK:
                self.points -= move.specialMovePiece.value - 1

        else:
            pieceToMove = move.piece
            pieceToTake = move.pieceToCapture
            if pieceToTake:
                if pieceToTake.side == WHITE:
                    self.points -= pieceToTake.value
                if pieceToTake.side == BLACK:
                    self.points += pieceToTake.value
                self.pieces.remove(pieceToTake)

            self.movePieceToPosition(pieceToMove, move.newPos)
            pieceToMove.movesMade += 1
        self.movesMade += 1
        self.currentSide = not self.currentSide

    '''This was written by Derek'''
    def makeChosenMove(self, move):
        self.addMoveToHistory(move)
        if move.kingsideCastle or move.queensideCastle:
            kingToMove = move.piece
            rookToMove = move.specialMovePiece
            self.movePieceToPosition(kingToMove, move.newPos)
            self.movePieceToPosition(rookToMove, move.rookMovePos)
            kingToMove.movesMade += 1
            rookToMove.movesMade += 1

        elif move.pessant:
            pawnToMove = move.piece
            pawnToTake = move.specialMovePiece
            pawnToMove.position = move.newPos
            self.removePiece(pawnToTake)
            pawnToMove.movesMade += 1

        elif move.promotion:
            self.pieces.remove(move.piece)
            self.pieces.append(move.specialMovePiece)
            if move.piece.side == WHITE:
                self.points += move.specialMovePiece.value - 1
            if move.piece.side == BLACK:
                self.points -= move.specialMovePiece.value - 1

        else:
            pieceToMove = move.piece
            pieceToTake = move.pieceToCapture
            print(str(pieceToTake))
            if pieceToTake:
                if pieceToTake.side == WHITE:
                    self.points -= pieceToTake.value
                if pieceToTake.side == BLACK:
                    self.points += pieceToTake.value
                self.removePiece(pieceToTake)

            self.movePieceToPosition(pieceToMove, move.newPos)
            pieceToMove.movesMade += 1
        self.movesMade += 1
        self.currentSide = not self.currentSide

    '''This was written by Derek'''
    def removePiece(self, pieceToRemove):
        number = pieceToRemove.number
        side = pieceToRemove.side
        letter = pieceToRemove.stringRep
        #adding a captured piece to the bins 
        if side == WHITE:
            if letter == "p":
                self.whiteCaptured.extend([Captured( letter, WHITE, C(0, 7 - number), number)])
            elif letter == "R":
                self.whiteCaptured.extend([Captured( letter, WHITE, C(1, 7 - R + number), number)])
            elif letter == "N":
                self.whiteCaptured.extend([Captured( letter, WHITE, C(1, 7 - N + number), number)])
            elif letter == "Q":
                self.whiteCaptured.extend([Captured( letter, WHITE, C(1, 7 - Q + number), number)])
            elif letter == "B":
                self.whiteCaptured.extend([Captured( letter, WHITE, C(1, 7 - B + number), number)])
        else:
            if letter == "p":
                self.blackCaptured.extend([Captured( letter, BLACK, C(1, number), number)])
            elif letter == "R":
                self.blackCaptured.extend([Captured( letter, BLACK, C(0, (R + number)), number)])
            elif letter == "N":
                self.blackCaptured.extend([Captured( letter, BLACK, C(0, (N + number)), number)])
            elif letter == "Q":
                self.blackCaptured.extend([Captured( letter, BLACK, C(0, (Q + number)), number)])
            elif letter == "B":
                self.blackCaptured.extend([Captured( letter, BLACK, C(0, (B + number)), number)])
        #removing the piece from the 
        self.pieces.remove(pieceToRemove)
        print("Piece added to Captured bin")
        if side == WHITE:
            print(self.makeStringRepBin(self.whiteCaptured))
        else:
            print(self.makeStringRepBin(self.blackCaptured))
        print()



    def getPointValueOfSide(self, side):
        points = 0
        for piece in self.pieces:
            if piece.side == side:
                points += piece.value
        return points

    def getPointAdvantageOfSide(self, side):
        pointAdvantage = self.getPointValueOfSide(side) - \
            self.getPointValueOfSide(not side)
        return pointAdvantage
        if side == WHITE:
            return self.points
        if side == BLACK:
            return -self.points

    def getAllMovesUnfiltered(self, side, includeKing=True):
        unfilteredMoves = []
        for piece in self.pieces:
            if piece.side == side:
                if includeKing or piece.stringRep != 'K':
                    for move in piece.getPossibleMoves():
                        unfilteredMoves.append(move)
        return unfilteredMoves

    def testIfLegalBoard(self, side):
        for move in self.getAllMovesUnfiltered(side):
            pieceToTake = move.pieceToCapture
            if pieceToTake and pieceToTake.stringRep == 'K':
                return False
        return True

    def moveIsLegal(self, move):
        side = move.piece.side
        self.makeMove(move)
        isLegal = self.testIfLegalBoard(not side)
        self.undoLastMove()
        return isLegal

    # TODO: remove side parameter, unneccesary
    def getAllMovesLegal(self, side):
        unfilteredMoves = list(self.getAllMovesUnfiltered(side))
        legalMoves = []
        for move in unfilteredMoves:
            if self.moveIsLegal(move):
                legalMoves.append(move)
        return legalMoves
