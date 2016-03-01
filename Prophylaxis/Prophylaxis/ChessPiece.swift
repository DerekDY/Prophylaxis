//
//  ChessPiece.swift
//  Chess
//
//  Created by Jack Cousineau on 10/14/15.
//

import UIKit
import SpriteKit

enum PieceColor{
    case Black
    case White
}

class ChessPiece: SKSpriteNode{
    var stringRep: String!
    var pieceColor: PieceColor!
    var image: UIImage!
    init(image: UIImage, color: PieceColor, size: CGSize){
        let Image = image
        self.image = image
        let Texture = SKTexture(image: Image)
        super.init(texture: Texture, color: UIColor.clearColor(), size: size)
        pieceColor = color
        self.name = "Piece"
    }
    
    required init(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    func isValidMove(start: BoardSpace, target: BoardSpace, board: Board) -> (Bool){
        return false
    }
    
    func spaceIsEmpty(x: Int, y: Int, board: [[BoardSpace]]) -> Bool{
        return board[y][x].occupyingPiece == nil
    }
    
    func isSideInCheck(board: Board) ->Bool{
        let color = self.pieceColor
        if color == PieceColor.White{
            if board.whiteInCheck{
                return true
            }
        }else{
            if board.blackInCheck{
                return true
            }
        }
        return false
    }
    
    func parseBishopMovement(start: BoardSpace, target: BoardSpace, board: [[BoardSpace]]) -> (Bool){
        let startX = start.x
        let startY = start.y
        let destinationX = target.x
        let destinationY = target.y
        let xChange = abs(startX - destinationX)
        let yChange = abs(startY - destinationY)
        
        if(xChange == yChange){
            if(xChange == 0){
                return false
            }
            if(startX > destinationX){
                if(startY > destinationY){ // Southwest
                    for i in 1...xChange{
                        if(board[startY - i][startX - i].occupyingPiece != nil && (i != xChange)){
                            return false;
                        }
                    }
                }
                else{ // Northwest
                    for i in 1...xChange{
                        if(board[startY + i][startX - i].occupyingPiece != nil && (i != xChange)){
                            return false;
                        }
                    }
                }
            }
            else{
                if(startY > destinationY){ // Southeast
                    for i in 1...xChange{
                        if(board[startY - i][startX + i].occupyingPiece != nil && (i != xChange)){
                            return false;
                        }
                    }
                }
                else{ // Northeast
                    for i in 1...xChange{
                        if(board[startY + i][startX + i].occupyingPiece != nil && (i != xChange)){
                            return false;
                        }
                    }
                }
            }
            return true
        }
        return false
    }
    
    func parseRookMovement(start: BoardSpace, target: BoardSpace, board: [[BoardSpace]]) -> (Bool){
        let startX = start.x
        let startY = start.y
        let destinationX = target.x
        let destinationY = target.y
        if(startX == destinationX || startY == destinationY){ // Straight line
            
            if(startX != destinationX){
                if(startX < destinationX){ // Moving to the right
                    return (parseHorizontal(startX+1, endPos: destinationX, destinationY: destinationY, movementLeft: false, board: board))
                }
                else{ // Moving to the left
                    return (parseHorizontal(destinationX, endPos: startX-1, destinationY: destinationY, movementLeft: true, board: board))
                }
            }
            else{
                if(startY < destinationY){ // Moving up
                    return (parseVertical(startY+1, endPos: destinationY, destinationX: destinationX, movementDown: false, board: board))
                }
                else{ // Moving down
                    return (parseVertical(destinationY, endPos: startY-1, destinationX: destinationX, movementDown: true, board: board))
                }
            }
        }
        return false
    }
    
    func parseHorizontal(startPos: Int, endPos: Int, destinationY: Int, movementLeft: Bool, board: [[BoardSpace]]) -> Bool{
        if endPos == 0{
            return false
        }
        for i in startPos...endPos{
            if let obstructingPiece = board[destinationY][i].occupyingPiece{ // board is backwards [y][x]
                if(((!movementLeft && i == endPos) || (movementLeft && i == startPos)) && obstructingPiece.pieceColor != pieceColor){
                    continue
                }
                return false
            }
        }
        return true
    }
    
    func parseVertical(startPos: Int, endPos: Int, destinationX: Int, movementDown: Bool, board: [[BoardSpace]]) -> Bool{
        if endPos < startPos{
            return false
        }
        for i in startPos...endPos{
            if let obstructingPiece = board[i][destinationX].occupyingPiece{
                if(((!movementDown && i == endPos) || (movementDown && i == startPos)) && obstructingPiece.pieceColor != pieceColor){
                    continue
                }
                return false
            }
        }
        return true
    }
    
    override func copyWithZone(zone: NSZone) -> AnyObject {
        let copy = ChessPiece(image: self.image, color: self.pieceColor, size: self.size)
        copy.stringRep = self.stringRep
        return copy
        
    }
    
    
    
}