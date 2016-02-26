//
//  King.swift
//  Chess
//
//  Created by Jack Cousineau on 10/23/15.
//

import UIKit

class King: ChessPiece {
    
    var moved = false
    
    override init(image: UIImage, color: PieceColor, size: CGSize){  //, enPassantEventHandler: ((enemyX: Int, enemyY: Int)->())
        //enPassantCallback = enPassantEventHandler
        super.init(image: image, color: color, size: size)
        self.stringRep = "K"
    }
    
    required init(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override func isValidMove(start: BoardSpace, target: BoardSpace, board: Board) -> (Bool){
        let startingPiece = start.getPiece()
        let boardInCheck:Bool = startingPiece.isSideInCheck(board)
        
        //let boardSpaces = board.boardSpaces
        if let capturedPiece = target.getPiece(){
            let movingPiece = start.getPiece()
            if capturedPiece.pieceColor == movingPiece.pieceColor{
                return false
            }
        }
        var validMove = false
        let startY = start.y
        let startX = start.x
        let destinationY = target.y
        let destinationX = target.x
        //print("King Moved: \(moved)")
        if(!moved && startY == destinationY && abs(startX - destinationX) == 2 && !boardInCheck){
            if(startX < destinationX){ // Castling right
                //print("Castle right possible")
                validMove = validCastlingMove(7, endRookX: 5, startEmptyX: 5, endEmptyX: 5, y: startY, movementLeft: false, board: board)
            }
            else{ // Castling left
                //print("Castle left possible")
                validMove = validCastlingMove(0, endRookX: 3, startEmptyX: 1, endEmptyX: 3, y: startY, movementLeft: true, board: board)
            }
        }
        
        if(!validMove){
            validMove = (abs(startX - destinationX) < 2 && abs(startY - destinationY) < 2)
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
    
    func validCastlingMove(startRookX: Int, endRookX: Int, startEmptyX: Int, endEmptyX: Int, y: Int, movementLeft: Bool, board: Board) -> Bool{
        let boardSpaces = board.boardSpaces
        if let castlingRook = boardSpaces[y][startRookX].occupyingPiece{
            if(parseHorizontal(startEmptyX, endPos: endEmptyX, destinationY: y, movementLeft: movementLeft, board: boardSpaces) && castlingRook.isKindOfClass(Rook) && !(castlingRook as! Rook).moved && castlingRook.pieceColor == pieceColor){
                return true
            }
        }
        return false
    }
    
    override func copyWithZone(zone: NSZone) -> AnyObject {
        let copy = King(image: self.image, color: self.pieceColor, size: self.size)
        copy.stringRep = self.stringRep
        copy.moved = self.moved
        return copy
        
    }

}
