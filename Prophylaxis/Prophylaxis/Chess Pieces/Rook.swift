//
//  Rook.swift
//  Chess
//
//  Created by Jack Cousineau on 10/23/15.
//

import UIKit

class Rook: ChessPiece{
    
    var moved = false
    
    override init(image: UIImage, color: PieceColor, size: CGSize){  //, enPassantEventHandler: ((enemyX: Int, enemyY: Int)->())
        //enPassantCallback = enPassantEventHandler
        super.init(image: image, color: color, size: size)
        self.stringRep = "R"
    }

    required init(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override func isValidMove(start: BoardSpace, target: BoardSpace, board: Board) -> (Bool){
        let startingPiece = start.getPiece()
        let boardInCheck:Bool = startingPiece.isSideInCheck(board)
        var validMove = false

        let boardSpaces = board.boardSpaces
        
        validMove = parseRookMovement(start, target: target, board: boardSpaces)
        
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
        let copy = Rook(image: self.image, color: self.pieceColor, size: self.size)
        copy.moved = self.moved
        return copy
    }

}
