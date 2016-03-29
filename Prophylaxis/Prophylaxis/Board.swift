//
//  Board.swift
//  Prophylaxis
//
//  Created by Derek De Young on 1/17/16.
//  Copyright © 2016 Prophylaxis. All rights reserved.
//

import UIKit

class Board: NSObject, NSCopying {
    
    /**
     The game's corresponding `ChessGame` instance
     */
    //var chessGame: ChessGame!
    
    /**
     2D array to hold the game's `BoardSpace`s in a grid pattern.
     Note that the coordinates start from the bottom-left, at 0,0.
     */
    var boardSpaces = [[BoardSpace]]()
    
    
    var highlightedSpaces = [BoardSpace]()
    
    /**
     The `BoardSpace` currently highlighted.
     */
    var highlightedSpace: BoardSpace!
    
    /**
     The normal background `NSColor` of the `BoardSpace` that is currently highlighted.
     Needed to restore the `BoardSpace`'s color back to normal after its highlight is removed.
     */
    var highlightedSpaceColor: UIColor!
    
    
    /**
     The `ChessPiece` that moved during the last turn. Used to detect the conditions for an en passant move.
     */
    var lastPieceMoved: ChessPiece!
    
    /**
     Indicates whether the game has finished.
     */
    var gameOver = false
    
    var selectedPiece: ChessPiece!
    var whiteInCheck = false
    var blackInCheck = false
    
    
    init(boardspaces: [[BoardSpace]]){
        self.boardSpaces = boardspaces
    }
    
    
    func selectPiece(piece: ChessPiece){
        self.selectedPiece = piece
        unhighlightSpaces()
        highlightSpace(piece.parent as! BoardSpace)
        highlightLegalMoves(piece)
    }
    
    func highlightLegalMoves(piece: ChessPiece){
        let currentSpace = piece.parent as! BoardSpace
        for y in 0...7{
            for x in 0...7{
                if piece.isValidMove(currentSpace, target: self.boardSpaces[x][y], board: self){
                    //reset the pawns firstmove since not actually making a move
                    self.highlightSpace(boardSpaces[x][y])
                }
            }
        }
        
    }
    
    func boardInCheck(side: PieceColor) -> Bool{
        print("Calling Board in Check for \(side)")
        var kingSpace = boardSpaces[0][0]
        var kingFound = false
        for y in 0...7{
            for x in 0...7{
                let currentSpace = boardSpaces[x][y]
                if let currentPiece = currentSpace.getPiece(){
                    if currentPiece.stringRep == "K"{
                        if currentPiece.pieceColor == side{
                            kingSpace = boardSpaces[x][y]
                            //print("FOUND THAT EFIN KING")
                            kingFound = true
                            break
                        }
                    }
                }
            }
            if kingFound {
                break
            }
        }
        if(!kingFound){
            print("KING NOT FOUNDDDDDD!!!!")
        }
        for y in 0...7{
            for x in 0...7{
                let currentSpace = boardSpaces[x][y]
                if let currentPiece = currentSpace.getPiece(){
                    if currentPiece.pieceColor != side{
                        print("Calling is Valid Move for: \(currentPiece.stringRep)")
                        if currentPiece.isValidMove(boardSpaces[x][y], target: kingSpace, board: self) {
                            if currentPiece.pieceColor == PieceColor.White{
                                self.blackInCheck = true
                            }else{
                                self.whiteInCheck = true
                            }
                            return true
                        }
                    }
                }
            }
        }
        return false
    }
    
    
    func boardInCheckMate(side:PieceColor) -> Bool{
        var inCheckMate = true
        for y in 0...7{
            for x in 0...7{
                let currentSpace = boardSpaces[x][y]
                if let piece = currentSpace.getPiece(){
                    if piece.pieceColor == side{
                        for column in 0...7{
                            for row in 0...7{
                                if piece.isValidMove(self.boardSpaces[x][y], target: self.boardSpaces[row][column], board: self){
                                    inCheckMate = false
                                }
                            }
                        }
                    }
                }
            }
        }
        return inCheckMate
    }
    
    
    
    func newMoveReset(side: PieceColor){
        for y in 0...7{
            for x in 0...7{
                let currentSpace = boardSpaces[x][y]
                if let piece = currentSpace.getPiece(){
                    if piece.pieceColor == side{
                        if piece.stringRep == "P"{
                            let pawn = piece as! Pawn
                            pawn.enPessantCapturable = false
                            pawn.justMadeDoubleStep = false
                            
                        }
                        
                    }
                }
            }
        }
        
    }
    
    
    
    
    
    
    func move(piece: ChessPiece, space: BoardSpace!, piecetotake: ChessPiece!){
        let currentSpace = piece.parent as! BoardSpace
        var y = 0
        if piece.stringRep == "K"{
            let king = piece as! King
            king.moved = true
        }
        if piece.stringRep == "R"{
            let rook = piece as! Rook
            rook.moved = true
        }
        if piece.stringRep == "P"{
            let pawn = piece as! Pawn
            if pawn.firstMove {
                pawn.firstMove = false
            }
            if space != nil {
                if abs(currentSpace.y - space.y) == 2{
                    pawn.justMadeDoubleStep = true
                    pawn.enPessantCapturable = true
                }
            }
            
        }
        let fromSpace = piece.parent as! BoardSpace
        fromSpace.removePiece()
        if (piecetotake != nil){
            let spacetaken = piecetotake.parent as! BoardSpace
            //print("removing piece")
            //print("Took Piece: " + piecetotake.stringRep)
            spacetaken.removePiece()
            spacetaken.setPiece(piece)
            y = spacetaken.y
        }else {
            y = space.y
            space.setPiece(piece)
//            print("Coords: ")
//            print(space.x)
//            print(space.y)
        }
        //space.addChild(piece)
        //currentSpace?.removeAllChildren()
        unhighlightSpaces()
        self.selectedPiece = nil
        if(piece.stringRep == "P"){
            let pawn = piece as! Pawn
            if pawn.pieceColor == PieceColor.White{
                if y == 7{
                    space.removePiece()
                    space.setPiece(Queen(image: UIImage(named: "white_queen")!, color: PieceColor.White, size: boardSpaces[0][0].size))
                }
            }else{
                if y == 0{
                    space.removePiece()
                    space.setPiece(Queen(image: UIImage(named: "black_queen")!, color: PieceColor.Black, size: boardSpaces[0][0].size))
                }
            }
        }
    }

    
    /**
     Highlights a `BoardSpace`.
     
     - Parameter space: The `BoardSpace` to highlight.
     */

    func highlightSpace(space: BoardSpace){
        self.highlightedSpaces.append(space)
        let highlight = UIColor(red: 0.941, green: 0.765, blue: 0.188, alpha: 1)
        space.color = highlight
    }
    
    
    func unhighlightSpaces(){
        //print("In highlight Piece funciton...")
        //print(piece.stringRep)
        for space in self.highlightedSpaces{
            space.color = space.originalColor
        }
        self.highlightedSpaces.removeAll()
    }
    
    
    func emptyBoard(){
        for y in 0...7{
            for x in 0...7{
                let currentSpace = boardSpaces[x][y]
                if let _ = currentSpace.getPiece(){
                    currentSpace.removePiece()
                }
            }
        }
    }
    
    
    /**
     Places all pieces on the `Board`.
     
     - Parameter iconSet: The `IconSet` to populate with.
     */
    func populateBoard(){
        var spriteSize = boardSpaces[0][0].size
        spriteSize.height = round(spriteSize.height*(9/10))
        
        for i in 0...7{
            boardSpaces[1][i].setPiece(Pawn(image: UIImage(named: "white_pawn")!, color: PieceColor.White, size: spriteSize))
        }
        boardSpaces[0][0].setPiece(Rook(image: UIImage(named: "white_rook")!, color: PieceColor.White, size: spriteSize))
        boardSpaces[0][1].setPiece(Knight(image: UIImage(named: "white_knight")!, color: PieceColor.White, size: spriteSize))
        boardSpaces[0][2].setPiece(Bishop(image: UIImage(named: "white_bishop")!, color: PieceColor.White, size: spriteSize))
        boardSpaces[0][3].setPiece(Queen(image: UIImage(named: "white_queen")!, color: PieceColor.White, size: spriteSize))
        boardSpaces[0][4].setPiece(King(image: UIImage(named: "white_king")!, color: PieceColor.White, size: spriteSize))
        boardSpaces[0][5].setPiece(Bishop(image: UIImage(named: "white_bishop")!, color: PieceColor.White, size: spriteSize))
        boardSpaces[0][6].setPiece(Knight(image: UIImage(named: "white_knight")!, color: PieceColor.White, size: spriteSize))
        boardSpaces[0][7].setPiece(Rook(image: UIImage(named: "white_rook")!, color: PieceColor.White, size: spriteSize))
        
        for i in 0...7{
            boardSpaces[6][i].setPiece(Pawn(image: UIImage(named: "black_pawn")!, color: PieceColor.Black, size: spriteSize))
        }
        boardSpaces[7][0].setPiece(Rook(image: UIImage(named: "black_rook")!, color: PieceColor.Black, size: spriteSize))
        boardSpaces[7][1].setPiece(Knight(image: UIImage(named: "black_knight")!, color: PieceColor.Black, size: spriteSize))
        boardSpaces[7][2].setPiece(Bishop(image: UIImage(named: "black_bishop")!, color: PieceColor.Black, size: spriteSize))
        boardSpaces[7][3].setPiece(Queen(image: UIImage(named: "black_queen")!, color: PieceColor.Black, size: spriteSize))
        boardSpaces[7][4].setPiece(King(image: UIImage(named: "black_king")!, color: PieceColor.Black, size: spriteSize))
        boardSpaces[7][5].setPiece(Bishop(image: UIImage(named: "black_bishop")!, color: PieceColor.Black, size: spriteSize))
        boardSpaces[7][6].setPiece(Knight(image: UIImage(named: "black_knight")!, color: PieceColor.Black, size: spriteSize))
        boardSpaces[7][7].setPiece(Rook(image: UIImage(named: "black_rook")!, color: PieceColor.Black, size: spriteSize))
    }
    
    func copyWithZone(zone: NSZone) -> AnyObject {
        var newSpaces = [[BoardSpace]]()
        for row in 0...7 {
            var columnSection = [BoardSpace]()
            for col in 0...7 {
                let square = self.boardSpaces[row][col].copy() as! BoardSpace
                columnSection.append(square)
                
            }
        newSpaces.append(columnSection)
        }
        
        let copy = Board(boardspaces: newSpaces)
        copy.whiteInCheck = self.whiteInCheck
        copy.blackInCheck = self.blackInCheck
        return copy
    }
    
}
