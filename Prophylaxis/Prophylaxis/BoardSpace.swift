//
//  BoardSpace.swift
//  Prophylaxis
//
//  Created by Derek De Young on 1/16/16.
//  Copyright © 2016 Prophylaxis. All rights reserved.
//

import UIKit
import Foundation
import SpriteKit

class BoardSpace: SKSpriteNode {
    var occupyingPiece: ChessPiece!
    var x: Int
    var y: Int
    var originalColor: UIColor
    
    init(squareSize: CGSize, spaceColor: UIColor, x: Int, y: Int){
        self.x = x
        self.y = y
        self.originalColor = spaceColor
        super.init(texture: nil, color: spaceColor, size: squareSize)
    }
    
    required init(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    func setPiece(piece: ChessPiece){
        self.occupyingPiece = piece
        //piece.name = "\(piece.stringRep) at \(self.name!)"
        self.addChild(piece)
    }
    
    func getPiece() ->ChessPiece!{
        if self.occupyingPiece != nil{
            return self.occupyingPiece
        }
        return nil
    }
    
    func removePiece(){
        if let piece = self.occupyingPiece{
            self.occupyingPiece = nil
            piece.removeFromParent()
        }
    }
    override func copyWithZone(zone: NSZone) -> AnyObject {
        let copy = BoardSpace(squareSize: self.size, spaceColor: self.originalColor, x: self.x, y: self.y)
        if let currentOccupyingPiece = self.occupyingPiece{
            if currentOccupyingPiece.stringRep == "K"{
                let currentPiece = currentOccupyingPiece as! King
                copy.setPiece(currentPiece.copy() as! King)
            }else if currentOccupyingPiece.stringRep == "Q"{
                let currentPiece = currentOccupyingPiece as! Queen
                copy.setPiece(currentPiece.copy() as! Queen)
            }else if currentOccupyingPiece.stringRep == "N"{
                let currentPiece = currentOccupyingPiece as! Knight
                copy.setPiece(currentPiece.copy() as! Knight)
            }else if currentOccupyingPiece.stringRep == "R"{
                let currentPiece = currentOccupyingPiece as! Rook
                copy.setPiece(currentPiece.copy() as! Rook)
            }else if currentOccupyingPiece.stringRep == "B"{
                let currentPiece = currentOccupyingPiece as! Bishop
                copy.setPiece(currentPiece.copy() as! Bishop)
            }else if currentOccupyingPiece.stringRep == "P"{
                let currentPiece = currentOccupyingPiece as! Pawn
                copy.setPiece(currentPiece.copy() as! Pawn)
            }else{
                copy.setPiece(currentOccupyingPiece.copy() as! ChessPiece)
            }
            
        }else{
            copy.occupyingPiece = nil
        }
        
        return copy
        
    }

}
