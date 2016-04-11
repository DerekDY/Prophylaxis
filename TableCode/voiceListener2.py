from os import environ, path

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
from buttonListener import *
from Coordinate import Coordinate as C
import Move
import subprocess
import time

MODELDIR = "../../pocketsphinx-python/pocketsphinx/model"
DATADIR = "../../pocketsphinx-python/pocketsphinx/test/data"

class VoiceListener():

    def __init__(self, pin, card):
        config = Decoder.default_config()
        config.set_string('-hmm', path.join(MODELDIR, 'en-us/en-us'))
        config.set_string('-jsgf', path.join(MODELDIR, 'en-us/chess.jsgf'))
        config.set_string('-dict', path.join(MODELDIR, 'en-us/chess.dict'))
        self.decoder = Decoder(config)
        self.bl = ButtonListener(pin)
        self.card = card
	
    def listen(self, b, turn):
        self.board = b
        self.turn = turn
        self.bl.startListener()
        while not self.bl.wasPressed():
            pass
        self.bl.stopListener()
        subprocess.Popen(["arecord", "-D", "plughw:" + str(self.card) + ",0", "-d", "2.5", "-f", "S16_LE", "-r", "16000", "out.wav"])
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
        return self.decode(result)

    def decode(self, result):
        if len(result) == 0:
            return None
        if result[0] == "promote":
            return 1, result[2]
        if result[2] == "castle":
            if result[0] == "king":
                return 2
            return 3  # queen side
        if result[0] == "pawn":
            # check that only one pawn can do the move
            if self.turn == True:  # White
                piecesFound = []
                try:  #will fail if capture
                    if self.board.pieceAtPosition(C(self.convert(result[2]), self.convert(result[3]))) == None:  # no capture
                        piecesFound.append(self.isAt(result, "p", 0, -1))
                        try:
                            if piecesFound[0] == None:  # pawn might be 2 squares back
                                piecesFound.append(self.isAt(result, "p", 0, -2))
                        except:
                            pass
                except:  # capture
                    piecesFound.append(self.isAt(result, "p", -1, -1))
                    piecesFound.append(self.isAt(result, "p", 1, -1))
                return self.check(piecesFound, result)
            else:  # Black
                piecesFound = []
                if self.board.pieceAtPosition(C(self.convert(result[2]), self.convert(result[3]))) != None:  # capture
                    piecesFound.append(self.isAt(result, "p", -1, 1))
                    piecesFound.append(self.isAt(result, "p", 1, 1))
                else:  # no piece taken - forward move
                    piecesFound.append(self.isAt(result, "p", 0, 1))
                    try:
                        if piecesFound[0] == None:  # pawn might be 2 squares back
                            piecesFound.append(self.isAt(result, "p", 0, 2))
                    except:
                        pass
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
            piecesFound.append(self.isAt(result, "N", -1, 0))
            piecesFound.append(self.isAt(result, "N", 1, 0))
            piecesFound.append(self.isAt(result, "N", 0, -1))
            piecesFound.append(self.isAt(result, "N", 0, 1))
            piecesFound.append(self.isAt(result, "N", -1, -1))
            piecesFound.append(self.isAt(result, "N", -1, 1))
            piecesFound.append(self.isAt(result, "N", 1, -1))
            piecesFound.append(self.isAt(result, "N", 1, 1))
            return self.check(piecesFound, result)
        # else: user gave 2 coordinates
        try:
            return Move.Move(self.board.pieceAtPosition(C(self.convert(result[0]), self.convert(result[1]))), C(self.convert(result[3]), self.convert(result[4])), self.board.pieceAtPosition(C(self.convert(result[3]), self.convert(result[4]))))
        except:
            return 0

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
    
    def check(self, piecesFound, result):
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
            return Move.Move(pieces[0], C(self.convert(result[2]), self.convert(result[3])), self.board.pieceAtPosition(C(self.convert(result[2]), self.convert(result[3]))))
        return 0

    def convert(self, r):
        if r == "alpha":
            return 0
        elif r == "bravo":
            return 1
        elif r == "charlie":
            return 2
        elif r == "delta":
            return 3
        elif r == "echo":
            return 4
        elif r == "foxtrot":
            return 5
        elif r == "golf":
            return 6
        elif r == "hotel":
            return 7
        elif r == "one":
            return 0
        elif r == "two":
            return 1
        elif r == "three":
            return 2
        elif r == "four":
            return 3
        elif r == "five":
            return 4
        elif r == "six":
            return 5
        elif r == "seven":
            return 6
        else:
            return 7
 
