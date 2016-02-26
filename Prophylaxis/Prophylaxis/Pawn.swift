//
//  Pawn.swift
//  Prophylaxis
//
//  Created by Derek De Young on 1/17/16.
//  Copyright © 2016 Prophylaxis. All rights reserved.
//

import UIKit

class Pawn: ChessPiece {
    
    var firstMove = true
    var justMadeDoubleStep = false
    var enPessantCapturable = false
    
    //var enPassantCallback: ((enemyX: Int, enemyY: Int)->())
    
    override init(image: UIImage, color: PieceColor, size: CGSize){  //, enPassantEventHandler: ((enemyX: Int, enemyY: Int)->())
        //enPassantCallback = enPassantEventHandler
        super.init(image: image, color: color, size: size)
        self.stringRep = "P"
    }
    
    required init(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override func isValidMove(start: BoardSpace, target: BoardSpace, board: Board) -> (Bool){
        let startingPiece = start.getPiece()
        let boardInCheck:Bool = startingPiece.isSideInCheck(board)
        var validMove = false
        
        let boardSpaces = board.boardSpaces
        let startX = start.x
        let startY = start.y
        let destinationX = target.x
        let destinationY = target.y
        
        
        var maxYVariance = 1, maxXVariance = 0
        
        if let _ = boardSpaces[destinationY][destinationX].occupyingPiece{ // Piece at destination
            if(startX == destinationX){
                maxXVariance--;
            }
            else{
                maxXVariance++
            }
        }
        
        let isWhite = pieceColor == PieceColor.White
        var xCoordR = 7
        var xCoordL = 0
        if isWhite && startY == 4{
            //print("White can Possibly EnPassant")
            let space = self.parent as! BoardSpace
            if(startX != 7){
                xCoordR = space.x + 1
            }
            if(startX != 0){
                xCoordL = space.x - 1
            }
            let yCoord = space.y
            //print("coords: \(xCoordR) , \(yCoord) ")
            if(startX != 7){
                let pieceR = boardSpaces[yCoord][xCoordR].occupyingPiece
                if((pieceR) != nil){
                    if(pieceR.stringRep == "P"){
                        //print("pawn to capture on right")
                        let pawn = pieceR as! Pawn
                        if(pawn.enPessantCapturable){
                            if(destinationY == yCoord + 1 && destinationX == xCoordR){
                                validMove = true
                            }
                        }
                    }
                }
            }
            if(startX != 0){
                let pieceL = boardSpaces[yCoord][xCoordL].occupyingPiece
                if((pieceL) != nil){
                    if(pieceL.stringRep == "P"){
                        //print("pawn to capture on right")
                        let pawn = pieceL as! Pawn
                        if(pawn.enPessantCapturable){
                            if(destinationY == yCoord + 1 && destinationX == xCoordL){
                                validMove = true
                            }
                        }
                    }
                }
            }
        }else if !isWhite && startY == 3{
            //print("Black can Possibly EnPassant")
            let space = self.parent as! BoardSpace
            if(startX != 7){
                xCoordR = space.x + 1
            }
            if(startX != 0){
                xCoordL = space.x - 1
            }
            let yCoord = space.y
            //print("coords: \(xCoordR) , \(yCoord) ")
            if(startX != 7){
                let pieceR = boardSpaces[yCoord][xCoordR].occupyingPiece
                if((pieceR) != nil){
                    if(pieceR.stringRep == "P"){
                        //print("pawn to capture on right")
                        let pawn = pieceR as! Pawn
                        if(pawn.enPessantCapturable){
                            if(destinationY == yCoord - 1 && destinationX == xCoordR){
                                validMove =  true
                            }
                        }
                    }
                }
            }
            if(startX != 0){
                let pieceL = boardSpaces[yCoord][xCoordL].occupyingPiece
                if((pieceL) != nil){
                    if(pieceL.stringRep == "P"){
                        //print("pawn to capture on right")
                        let pawn = pieceL as! Pawn
                        if(pawn.enPessantCapturable){
                            if(destinationY == yCoord - 1 && destinationX == xCoordL){
                                validMove = true
                            }
                        }
                    }
                }
            }
        }
        
        let xVariance = abs(destinationX - startX), yVariance = abs(destinationY - startY)
        
        if(firstMove){
            maxYVariance++
            //print("First Move: Y Var= \(maxYVariance)")
        }
        
        
        if xVariance <= maxXVariance && yVariance <= maxYVariance && ((!(xVariance == 1 && yVariance == 2) && ((isWhite && startY < destinationY) || (!isWhite && startY > destinationY))) || (maxYVariance == 2 && ((isWhite && boardSpaces[startY + 1][destinationX].occupyingPiece != nil) || (!isWhite && boardSpaces[startY - 1][destinationX].occupyingPiece != nil)))){
            validMove = parseRookMovement(start, target: target, board: boardSpaces) || parseBishopMovement(start, target: target, board: boardSpaces)
        }
        
        
        if let capturedPiece = target.getPiece(){
            let movingPiece = start.getPiece()
            if capturedPiece.pieceColor == movingPiece.pieceColor{
                validMove = false
            }
        }
        
        if !boardInCheck && validMove{
            let tempBoard = board.copy() as! Board
            let currentSpace = self.parent as! BoardSpace
            let tempTarget = tempBoard.boardSpaces[target.y][target.x]
            let tempPiece = tempBoard.boardSpaces[currentSpace.y][currentSpace.x].getPiece()
            tempBoard.move(tempPiece, space: tempTarget, piecetotake: tempTarget.getPiece())
            if tempBoard.boardInCheck(startingPiece.pieceColor){
                return !validMove
            }else{
                return validMove
            }
            
        }else{
            return validMove
        }
    }
    
    override func copyWithZone(zone: NSZone) -> AnyObject {
        let copy = Pawn(image: self.image, color: self.pieceColor, size: self.size)
        copy.firstMove = self.firstMove
        copy.justMadeDoubleStep = self.justMadeDoubleStep
        copy.enPessantCapturable = self.enPessantCapturable
        return copy
        
    }
    
}

