//
//  GameScene.swift
//  Prophylaxis
//
//  Created by Derek De Young on 1/16/16.
//  Copyright (c) 2016 Prophylaxis. All rights reserved.
//
import Foundation
import SpriteKit

class GameScene: SKScene {
    

    var myLabel = SKLabelNode(fontNamed: "Arial")
    var boardSpaces = [[BoardSpace]]()
    var board: Board!
    var game: ChessGame!
    
    
    override func didMoveToView(view: SKView) {
        self.backgroundColor = SKColor.whiteColor()
        /* Setup your scene here */
        self.scaleMode = .ResizeFill
        
        // Draw the board
        drawMenu()
        //drawBack()
        //drawSettings()
        drawBoard()
        setupLabel()
        self.game = ChessGame(whitePlayerName: "Derek", blackPlayerName: "Nick", board: boardSpaces)
//        self.board = Board(boardspaces: boardSpaces)
//        self.board.populateBoard()
        

        
        
        
    }
    
    override func touchesBegan(touches: Set<UITouch>, withEvent event: UIEvent?) {
        /* Called when a touch begins */
        
        for touch in touches {
            let positionInScene = touch.locationInNode(self)
            let touched = self.nodeAtPoint(positionInScene)
            if let name = touched.name
            {
                let touchedNode = touched as! SKSpriteNode
                if let previouslyTouchedPiece = self.game.board.selectedPiece{
                    //print("\(previouslyTouchedPiece.stringRep) is selected")
                    if name == "Piece"{
                        let touchedPiece = touchedNode as! ChessPiece
                        if touchedPiece.pieceColor  == game.playerTurn{
                            game.board.selectPiece(touchedPiece)
                        }else{//check if legal move to capture
                            let fromSpace = previouslyTouchedPiece.parent as! BoardSpace
                            let toSpace = touchedPiece.parent as! BoardSpace
                            //print(fromSpace)
                            if previouslyTouchedPiece.isValidMove(fromSpace, target: toSpace, board: self.game.board){
                                game.board.move(previouslyTouchedPiece, space: nil, piecetotake: touchedPiece)
                                game.newPlayerMove()
                            }
                        }
                    }else if name == "Space"{
                        let space = touchedNode as! BoardSpace
                        //check if legal move
                        let fromSpace = previouslyTouchedPiece.parent as! BoardSpace
                        if previouslyTouchedPiece.isValidMove(fromSpace, target: space, board: self.game.board){
                            if previouslyTouchedPiece.stringRep == "K"{
                                if abs(fromSpace.x - space.x) == 2{
                                    game.board.move(previouslyTouchedPiece, space: space, piecetotake: nil)
                                    let dx = space.x - fromSpace.x
                                    let side = previouslyTouchedPiece.pieceColor
                                    var rook = game.board.boardSpaces[0][7].getPiece()
                                    if(dx > 0){
                                        if side == PieceColor.White{
                                            rook = game.board.boardSpaces[0][7].getPiece()
                                        }else{
                                            rook = game.board.boardSpaces[7][7].getPiece()
                                        }
                                        game.board.move(rook, space: game.board.boardSpaces[space.y][space.x - 1], piecetotake: nil)
                                    }else{
                                        if side == PieceColor.White{
                                            rook = game.board.boardSpaces[0][0].getPiece()
                                        }else{
                                            rook = game.board.boardSpaces[7][0].getPiece()
                                        }
                                        game.board.move(rook, space: game.board.boardSpaces[space.y][space.x + 1], piecetotake: nil)
                                    }
                                    
                                }else{
                                    game.board.move(previouslyTouchedPiece, space: space, piecetotake: nil)
                                }
                            }
                            //Put code here to check if en pessant
                            if previouslyTouchedPiece.stringRep == "P"{
                                let pawn = previouslyTouchedPiece as! Pawn
                                let isWhite = pawn.pieceColor == PieceColor.White
                                let currentSpace = pawn.parent as! BoardSpace
                                //piece moved diagonaly without capturing piece
                                if(space.x != currentSpace.x){
                                    if isWhite && currentSpace.y == 4{
                                        //print("Checking:\(currentSpace.y),\(space.x)")
                                        let spaceToCheck = boardSpaces[currentSpace.y][space.x] as BoardSpace
                                        if let pawnToTake = spaceToCheck.occupyingPiece{
                                            game.board.move(previouslyTouchedPiece, space: space, piecetotake: pawnToTake)
                                        }
                                    }else if !isWhite && currentSpace.y == 3{
                                        let spaceToCheck = boardSpaces[currentSpace.y][space.x]
                                        if let pawnToTake = spaceToCheck.occupyingPiece{
                                            game.board.move(previouslyTouchedPiece, space: space, piecetotake: pawnToTake)
                                        }
                                    }
                                }
                                //Pawn moves again to the final destination 
                                game.board.move(previouslyTouchedPiece, space: space, piecetotake: nil)
                                }else{
                                    game.board.move(previouslyTouchedPiece, space: space, piecetotake: nil)
                                }
                                game.newPlayerMove()
                            }
                            
                        }
                    
                }else{
                    if name == "Piece"{
                        let touchedPiece = touchedNode as! ChessPiece
                        //only alow a player to select a their  pieces
                        if touchedPiece.pieceColor  == game.playerTurn{
                            game.board.selectPiece(touchedPiece)
                        }
                    }
                    
                    
                }
                self.myLabel.text = "Touched Space: \(name)"
                //touchedNode.color = UIColor.yellowColor()
                
                
            }
        }
    }
   
    override func update(currentTime: CFTimeInterval) {
        /* Called before each frame is rendered */
    }
    
    func setupLabel() {
        self.myLabel.text = "Touch A Piece"
        self.myLabel.fontColor = UIColor.blackColor()
        self.myLabel.fontSize = 20
        self.myLabel.position = CGPointMake(200, 580)
        
        self.addChild(myLabel)
        
    }
    
    func drawMenu() {
        //let screenSize: CGRect = UIScreen.mainScreen().bounds
        //let screenWidth = screenSize.width
        //let screenHeight = screenSize.height
        
        
        
        
    }
    func drawBoard() {
        let screenSize: CGRect = UIScreen.mainScreen().bounds
        let screenWidth = screenSize.width
        let screenHeight = screenSize.height
        let lightColor = UIColor(red: 67/255, green: 179/255, blue: 255/255, alpha: 1)
        let darkColor = UIColor(red: 47/255, green: 129/255, blue: 183/255, alpha: 1)
        let alphas = ["A","B","C","D","E","F","G","H"]
        let numRows = 8
        let numCols = 8
        let squareSize = CGSizeMake(round(screenWidth/8), round(screenHeight/10))
        let xOffset:CGFloat = round(screenWidth/16)
        let yOffset:CGFloat = round(screenHeight/20)
        // Used to alternate between white and black squares
        var toggle:Bool = false
        for row in 0...numRows-1 {
            var columnSection = [BoardSpace]()
            for col in 0...numCols-1 {
                // Letter for this column
                let colChar = alphas[col]
                // Determine the color of square
                let color = toggle ? lightColor : darkColor
                let square = BoardSpace(squareSize: squareSize, spaceColor: color, x: col, y: row)
                square.position = CGPointMake(CGFloat(col) * squareSize.width + xOffset,
                    CGFloat(row) * squareSize.height + yOffset)
                // Set sprite's name (e.g., a8, c5, d1)
                square.name = "\(colChar)\(8-row)"
                square.name = "Space"
                self.addChild(square)
                columnSection.append(square)
                toggle = !toggle
            }
            toggle = !toggle
            boardSpaces.append(columnSection)
        }
    }
}
