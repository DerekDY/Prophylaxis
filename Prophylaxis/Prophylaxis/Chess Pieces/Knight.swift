//
//  Knight.swift
//  Chess
//
//  Created by Jack Cousineau on 10/23/15.
//

import UIKit

class Knight: ChessPiece {
    
    
    override init(image: UIImage, color: PieceColor, size: CGSize){  //, enPassantEventHandler: ((enemyX: Int, enemyY: Int)->())
        //enPassantCallback = enPassantEventHandler
        super.init(image: image, color: color, size: size)
        self.stringRep = "N"
    }
    
    required init(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override func isValidMove(start: BoardSpace, target: BoardSpace, board: Board) -> (Bool){
        let startingPiece = start.getPiece()
        let boardInCheck:Bool = startingPiece.isSideInCheck(board)
        var validMove = false
        
        //let boardSpaces = board.boardSpaces
        
        let xChange = abs(start.x - target.x)
        let yChange = abs(start.y - target.y)
        
        if ((xChange == 1&&yChange == 2)||(xChange == 2&&yChange == 1)){
            validMove = true
        }else{
            validMove = false
        }
        
        if let capturedPiece = target.getPiece(){
            let movingPiece = start.getPiece()
            if capturedPiece.pieceColor == movingPiece.pieceColor{
                validMove = false
            }
        }
        
        
        if boardInCheck && validMove{
            let tempBoard = board.copy() as! Board
            let currentSpace = self.parent as! BoardSpace
            let tempTarget = tempBoard.boardSpaces[target.y][target.x]
            let tempPiece = tempBoard.boardSpaces[currentSpace.y][currentSpace.x].getPiece()
            tempBoard.move(tempPiece, space: tempTarget, piecetotake: tempTarget.getPiece())
            var opColor = PieceColor.White
            if startingPiece.pieceColor == PieceColor.White{
                opColor = PieceColor.Black
            }
            if(boardInCheck){
                if startingPiece.pieceColor == PieceColor.White{
                    tempBoard.whiteInCheck = false
                }else{
                    tempBoard.blackInCheck = false
                }
                
            }
            //            if tempBoard.boardInCheck(opColor){
            //                print("This is working")
            //            }
            if tempBoard.boardInCheck(startingPiece.pieceColor){
                return !validMove
            }else{
                return validMove
            }
            
        }else if !boardInCheck && validMove{
            let tempBoard = board.copy() as! Board
            let currentSpace = self.parent as! BoardSpace
            let tempTarget = tempBoard.boardSpaces[target.y][target.x]
            let tempPiece = tempBoard.boardSpaces[currentSpace.y][currentSpace.x].getPiece()
            tempBoard.move(tempPiece, space: tempTarget, piecetotake: tempTarget.getPiece())
            if let capturedPiece = target.getPiece(){
                if capturedPiece.stringRep == "K"{
                    return validMove
                }else if tempBoard.boardInCheck(startingPiece.pieceColor){
                    return !validMove
                }else{
                    return validMove
                }
            }else{
                if tempBoard.boardInCheck(startingPiece.pieceColor){
                    return !validMove
                }else{
                    return validMove
                }
            }
            
        }
        return validMove
    }
    
    override func copyWithZone(zone: NSZone) -> AnyObject {
        let copy = Knight(image: self.image, color: self.pieceColor, size: self.size)
        copy.stringRep = self.stringRep
        return copy
        
    }

}
