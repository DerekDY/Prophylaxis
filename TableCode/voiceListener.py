from os import environ, path

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
from buttonListener import *
from Coordinate import Coordinate as C
import Move
import subprocess
import time
import copy

MODELDIR = "../../pocketsphinx-python/pocketsphinx/model"
DATADIR = "../../pocketsphinx-python/pocketsphinx/test/data"

class VoiceListener():

    def __init__(self, pin, card, turn):
        config = Decoder.default_config()
        config.set_string('-hmm', path.join(MODELDIR, 'en-us/en-us'))
        config.set_string('-jsgf', path.join(MODELDIR, 'en-us/chess.jsgf'))
        config.set_string('-dict', path.join(MODELDIR, 'en-us/chess.dict'))
        self.decoder = Decoder(config)
        self.bl = ButtonListener(pin)
        self.card = card
        self.turn = turn

    def listen(self, b):
        self.board = b
        self.bl.startListener()
        while not self.bl.wasPressed():
            pass
        self.bl.stopListener()
        subprocess.Popen(["arecord", "-D", "plughw:" + str(self.card)
+ ",0", "-d", "2.5", "-f", "S16_LE", "-r", "16000", "out.wav"])
        time.sleep(2.6)
        self.decoder.start_utt()
        stream = open("out.wav", 'rb')
        while True:
            buf = stream.read(1024)
            if buf:
                self.decoder.process_raw(buf, False, False)
            else:
                break
        self.decoder.end_utt()
        result = []
        for seg in self.decoder.seg():
            if seg.word != "<s>" and seg.word != "<sil>":
                result.append(seg.word)
                print(seg.word)
        # check for bad data
        if len(result) == 0:
            return "bad record", None  # can't decipher speech
        move = self.decode(result)
        # check for promotion
        try:
            if move[0] == 0:
                return "promote", move[1]
        except:
            pass
        # check for castling, multiple target error
        try:
            if move == 1:  # king side castle
                if self.turn:  # WHITE
                    pos = C(4, 0)
                else:  # BLACK
                    pos = C(4, 7)
                # find king -- shouldn't have moved
                p = self.board.pieceAtPosition(pos)
                if p is not None:
                    if p.stringRep == "K" and p.side == self.turn:
                        for m in p.getPossibleMoves():
                            if m.kingsideCastle:
                                return "move", m
                return "illegal move", None
            if move == 2:
                if self.turn:  # WHITE
                    pos = C(4, 0)
                else:  # BLACK
                    pos = C(4, 7)
                # find king -- shouldn't have moved
                p = self.board.pieceAtPosition(pos)
                if p is not None:
                    if p.stringRep == "K" and p.side == self.turn:
                        for m in p.getPossibleMoves():
                            if m.queensideCastle:
                                return "move", m
                return "illegal move", None
            if move == 3:
                return "multiple targets", None  # multiple targets
        except:
            pass
        return self.checkLegal(move)

    def decode(self, result):
        if result[0] == "promote":
            return 0, result[2]
        if result[2] == "castle":
            if result[0] == "king":
                return 1
            return 2  # queen side
        if result[0] == "pawn":
            if self.turn: # WHITE
                offset = -1
            else:  # BLACK
                offset = 1
            # check that only one pawn can do the move
            piecesFound = []
            try:  # will fail if capture
                if self.board.pieceAtPosition(C(self.convert(result[2]), self.convert(result[3]))) == None:  # no normal capture
                    # check for en passant
                    try:
                        lm = self.board.getLastMove()
                        if lm.piece.stringRep == "p" and lm.newPos - lm.oldPos == C(0, 2 * offset) and lm.oldPos + C(0, offset) == C(self.convert(result[2]), self.convert(result[3])):
                            # only legal possibility is en passant
                            piecesFound.append(self.isAt(result, "p",-1, offset))
                            piecesFound.append(self.isAt(result, "p",1, offset))
                            return self.check(piecesFound, result, offset)
                    except:
                        pass
                    piecesFound.append(self.isAt(result, "p", 0, offset))
                    try:
                        if piecesFound[0] == None:  # pawn might be 2 squares back
                            piecesFound.append(self.isAt(result, "p", 0, 2 * offset))
                    except:
                        pass
            except:  # capture
                piecesFound.append(self.isAt(result, "p", -1, offset))
                piecesFound.append(self.isAt(result, "p", 1, offset))
            return self.check(piecesFound, result)
        if result[0] == "knight":
            # check that only one knight can do the move
            piecesFound = []
            piecesFound.append(self.isAt(result, "N", -2, -1))
            piecesFound.append(self.isAt(result, "N", -2, 1))
            piecesFound.append(self.isAt(result, "N", 2, -1))
            piecesFound.append(self.isAt(result, "N", 2, 1))
            piecesFound.append(self.isAt(result, "N", -1, -2))
            piecesFound.append(self.isAt(result, "N", -1, 2))
            piecesFound.append(self.isAt(result, "N", 1, -2))
            piecesFound.append(self.isAt(result, "N", 1, 2))
            return self.check(piecesFound, result)
        if result[0] == "rook":
            # check that only one rook can do the move
            piecesFound = []
            piecesFound.append(self.scanLine(result, "R", -1, 0))
            piecesFound.append(self.scanLine(result, "R", 1, 0))
            piecesFound.append(self.scanLine(result, "R", 0, -1))
            piecesFound.append(self.scanLine(result, "R", 0, 1))
            return self.check(piecesFound, result)
        if result[0] == "bishop":
            # check that only one bishop can do the move
            piecesFound = []
            piecesFound.append(self.scanLine(result, "B", -1, -1))
            piecesFound.append(self.scanLine(result, "B", -1, 1))
            piecesFound.append(self.scanLine(result, "B", 1, -1))
            piecesFound.append(self.scanLine(result, "B", 1, 1))
            return self.check(piecesFound, result)
        if result[0] == "queen":
            # check that only one queen can do the move
            piecesFound = []
            piecesFound.append(self.scanLine(result, "Q", -1, 0))
            piecesFound.append(self.scanLine(result, "Q", 1, 0))
            piecesFound.append(self.scanLine(result, "Q", 0, -1))
            piecesFound.append(self.scanLine(result, "Q", 0, 1))
            piecesFound.append(self.scanLine(result, "Q", -1, -1))
            piecesFound.append(self.scanLine(result, "Q", -1, 1))
            piecesFound.append(self.scanLine(result, "Q", 1, -1))
            piecesFound.append(self.scanLine(result, "Q", 1, 1))
            return self.check(piecesFound, result)
        if result[0] == "king":
            piecesFound = []
            piecesFound.append(self.isAt(result, "K", -1, 0))
            piecesFound.append(self.isAt(result, "K", 1, 0))
            piecesFound.append(self.isAt(result, "K", 0, -1))
            piecesFound.append(self.isAt(result, "K", 0, 1))
            piecesFound.append(self.isAt(result, "K", -1, -1))
            piecesFound.append(self.isAt(result, "K", -1, 1))
            piecesFound.append(self.isAt(result, "K", 1, -1))
            piecesFound.append(self.isAt(result, "K", 1, 1))
            return self.check(piecesFound, result)
        # else: user gave 2 coordinates
        try:
            return Move.Move(self.board.pieceAtPosition(C(self.convert(result[0]), self.convert(result[1]))), C(self.convert(result[3]), self.convert(result[4])), self.board.pieceAtPosition(C(self.convert(result[3]), self.convert(result[4]))))
        except:
            return None

    def isAt(self, result, piece, x, y):
        p = self.board.pieceAtPosition(C(self.convert(result[2]) + x, self.convert(result[3]) + y))
        try:
            #print(p.stringRep)
            #print(p.position)
            #print(p.side)
            #print(self.convert(result[2]) + x)
            #print(self.convert(result[3]) + y)
            if p.stringRep == piece and p.side == self.turn:
                #print("POSSIBILITY!")
                return p
            return None
        except:
            return None

    def scanLine(self, result, piece, dx, dy):
        x = dx
        y = dy
        while abs(x) < 8 and abs(y) < 8:
            p = self.board.pieceAtPosition(C(self.convert(result[2]) + x, self.convert(result[3]) + y))
            try:  # if piece found, no exception will be thrown
                #print(p.stringRep)
                #print(p.position)
                #print(p.side)
                #print(self.convert(result[2]) + x)
                #print(self.convert(result[3]) + y)
                if p.stringRep == piece and p.side == self.turn:
                    #print("POSSIBILITY!")
                    return p
                return None
            except:
                pass
            x += dx
            y += dy
        return None

    def check(self, piecesFound, result, enPassantOffset = 0):
        # create new list without Nones
        pieces = []
        for piece in piecesFound:
            try:
                if piece == None:
                    pass
            except:
                pieces.append(piece)
        # see if there is exactly one match
        if len(pieces) == 1:
            return Move.Move(pieces[0], C(self.convert(result[2]), self.convert(result[3])), self.board.pieceAtPosition(C(self.convert(result[2]), self.convert(result[3]) - enPassantOffset)))
        if len(pieces) > 1:  # multiple targets
            return 3
        return None

    def convert(self, r):
        if r == "alpha":
            return 0
        if r == "bravo":
            return 1
        if r == "charlie":
            return 2
        if r == "delta":
            return 3
        if r == "echo":
            return 4
        if r == "foxtrot":
            return 5
        if r == "golf":
            return 6
        if r == "hotel":
            return 7
        if r == "one":
            return 0
        if r == "two":
            return 1
        if r == "three":
            return 2
        if r == "four":
            return 3
        if r == "five":
            return 4
        if r == "six":
            return 5
        if r == "seven":
            return 6
        if r == "eight":
            return 7
        return None  # should never get here

    def checkLegal(self, move):
        try:
            # check that piece to move is your color
            if move.piece.side != self.turn:
                return "illegal move", None
            # check that destination square is valid
            if move.pieceToCapture is not None:
                if move.pieceToCapture.side == self.turn:  # can't capture a piece of your color
                    return "illegal move", None
            if move.piece.stringRep == "p":
                dx = move.newPos[0] - move.oldPos[0]
                dy = move.newPos[1] - move.oldPos[1]
                if self.turn:  # WHITE
                    offset = 1
                    testPoint = 1
                else:  # BLACK
                    offset = -1
                    testPoint = 6
                if abs(dx) == 1 and dy == offset: # capturing
                    if move.pieceToCapture is not None:
                        return "move", move
                    # check for en passant
                    try:
                        lm = self.board.getLastMove()
                        if lm.piece.stringRep == "p" and lm.oldPos - lm.newPos == C(0, 2 * offset) and lm.newPos + C(0, offset) == move.newPos:
                            return "move", Move.Move(move.piece, move.newPos, self.board.pieceAtPosition(C(move.newPos[0], move.newPos[1] - offset)))
                    except:
                        return "illegal move", None
                if dx == 0 and dy == offset:
                    return "move", move
                if dx == 0 and dy == 2 * offset and move.oldPos[1] == testPoint and self.board.pieceAtPosition(C(move.oldPos[0], testPoint + offset)) is None:  # can move forward 2 spaces
                    return "move", move
                return "illegal move", None
            if move.piece.stringRep == "R":
                if self.checkLine(move) == 1:  # straight line move, no pieces in the way
                    return "move", move
                return "illegal move", None
            if move.piece.stringRep == "N":
                dx = move.newPos[0] - move.oldPos[0]
                dy = move.newPos[1] - move.oldPos[1]
                if (abs(dx) == 1 and abs(dy) == 2) or (abs(dx) == 2 and abs(dy) == 1):
                    return "move", move
                return "illegal move", None
            if move.piece.stringRep == "B":
                if self.checkLine(move) == 2:  # diagonal move, no pieces in the way
                    return "move", move
                return "illegal move", None
            if move.piece.stringRep == "Q":
                if self.checkLine(move) == 1 or self.checkLine(move) == 2:
                    return "move", move
                return "illegal move", None
            if move.piece.stringRep == "K":
                dx = move.newPos[0] - move.oldPos[0]
                dy = move.newPos[1] - move.oldPos[1]
                if abs(dx) > 1 or abs(dy) > 1:
                    return "illegal move", None
                return "move", move
            return "illegal move", None  # should never get here
        except:
            return "illegal move", None

    def checkLine(self, move):
        x0 = move.oldPos[0]
        x1 = move.newPos[0]
        y0 = move.oldPos[1]
        y1 = move.newPos[1]
        dx = x1 - x0
        dy = y1 - y0
        if dx == 0:
            if dy < 0:
                for i in range(y1 + 1, y0):
                    if self.board.pieceAtPosition(C(x0, i)) is not None:
                        return 0  # piece in the way
            else:
                for i in range(y0 + 1, y1):
                    if self.board.pieceAtPosition(C(x0, i)) is not None:
                        return 0
            return 1  # straight
        if dy == 0:
            if dx < 0:
                for i in range(x1 + 1, x0):
                    if self.board.pieceAtPosition(C(i, y0)) is not None:
                        return 0
            else:
                for i in range(x0 + 1, x1):
                    if self.board.pieceAtPosition(C(i, y0)) is not None:
                        return 0
            return 1  # straight
        if dx == dy:
            if dy < 0:
                j = x1 + 1
                for i in range(y1 + 1, y0):
                    if self.board.pieceAtPosition(C(j, i)) is not None:
                        return 0  #piece in the way
                    j += 1
            else:
                j = x0 + 1
                for i in range(y0 + 1, y1):
                    if self.board.pieceAtPosition(C(j, i)) is not None:
                        return 0
                    j += 1
            return 2  # diagonal
        if dx == -dy:
            if dy < 0:
                j = x1 - 1
                for i in range(y1 + 1, y0):
                    if self.board.pieceAtPosition(C(j, i)) is not None:
                        return 0
                    j -= 1
            else:
                j = x0 - 1
                for i in range(y0 + 1, y1):
                    if self.board.pieceAtPosition(C(j, i)) is not None:
                        return 0
                    j -= 1
            return 2  # diagonal
        return 0  # not on a line
