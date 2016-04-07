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
    
    var viewController: GameViewController!
    var myLabel = SKLabelNode(fontNamed: "Arial")
    var boardSpaces = [[BoardSpace]]()
    var board: Board!
    var game: ChessGame!
    var menuParent: SKSpriteNode!
    var blurFilter: CIFilter!
    var online = false
    var bluetooth: Bool = false
    
    
    override func didMoveToView(view: SKView) {
        self.backgroundColor = SKColor.whiteColor()
        /* Setup your scene here */
        self.scaleMode = .ResizeFill
        // Draw the board
        drawBoard()
        setupLabel()
        self.game = ChessGame(whitePlayerName: "WHITE", blackPlayerName: "BLACK", board: boardSpaces, label: myLabel, scene: self)
        drawMenuBar()
        drawMenu()
        
        //while true
        

        
        
        
    }
    //GAME LOGIC
    override func touchesBegan(touches: Set<UITouch>, withEvent event: UIEvent?) {
//        /* Called when a touch begins */
//        if self.myLabel.text == "Game Ended..."{
//            self.myLabel.text = ""
//            showMenu()
//            return
//        }
        
        
        for touch in touches {
            let positionInScene = touch.locationInNode(self)
            let touched = self.nodeAtPoint(positionInScene)
            if let name = touched.name
            {
                if name == "offline"{
                    print("Playing Offline")
                    online = false
                    clearMenu()
                    return
                }else if name == "online"{
                    print("Playing Online")
                    online = true
                    game.playOnline()  //start the socket connection
                    clearMenu()
                    return
                }
                if name == "bluetooth"{
                    if (bluetooth){
                        print("Turning Off bluetooth")
                        game.nrfManager.disconnect()
                        bluetooth = false
                    }else{
                        print("Starting bluetooth")
                        bluetooth = true
                        self.game.connectBluetooth()
                    }
                                        
                }
                
                if name == "close"{
                    game.resetGame()
                    return
                }
                if online == true{
                    if game.gameStarted != true{
                        return
                    }
                    if game.onlineSide != game.playerTurn{
                        self.myLabel.text = "\(game.playerTurn)'s Move"
                        return
                    }
                    if bluetooth{
                        return
                    }
                    //self.myLabel.text = "Your Move!"
                }
                
                let touchedNode = touched 
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
                                if (online){
                                    game.sendMove(fromSpace, toSpace: nil, capturedSpace: toSpace)
                                    game.switchOnlineSide()
                                }
                                if !online{
                                    game.newPlayerMove()
                                }
                            }
                        }
                    }else if name == "Space"{
                        let space = touchedNode as! BoardSpace
                        //check if legal move
                        var fromSpace = previouslyTouchedPiece.parent as! BoardSpace
                        if previouslyTouchedPiece.isValidMove(fromSpace, target: space, board: self.game.board){
                            //check to see if casteling
                            if previouslyTouchedPiece.stringRep == "K"{
                                if abs(fromSpace.x - space.x) == 2{
                                    game.board.move(previouslyTouchedPiece, space: space, piecetotake: nil)
                                    if (online){
                                        game.sendMove(fromSpace, toSpace: space, capturedSpace: nil)
                                    }
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
                                        if (online){
                                            game.sendMove(rook.parent as! BoardSpace, toSpace: game.board.boardSpaces[space.y][space.x - 1], capturedSpace: nil)
                                        }
                                    }else{
                                        if side == PieceColor.White{
                                            rook = game.board.boardSpaces[0][0].getPiece()
                                        }else{
                                            rook = game.board.boardSpaces[7][0].getPiece()
                                        }
                                        game.board.move(rook, space: game.board.boardSpaces[space.y][space.x + 1], piecetotake: nil)
                                        if (online){
                                            game.sendMove(rook.parent as! BoardSpace, toSpace: game.board.boardSpaces[space.y][space.x + 1], capturedSpace: nil)
                                        }
                                    }
                                    
                                }else{
                                    game.board.move(previouslyTouchedPiece, space: space, piecetotake: nil)
                                    if (online){
                                        game.sendMove(fromSpace, toSpace: space, capturedSpace: nil)
                                    }
                                }
                            }
                            //Put code here to check if en pessant
                            else if previouslyTouchedPiece.stringRep == "P"{
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
                                            if (online){
                                                game.sendMove(fromSpace, toSpace: space, capturedSpace: spaceToCheck)
                                                fromSpace = spaceToCheck
                                                
                                            }
                                        }
                                    }else if !isWhite && currentSpace.y == 3{
                                        let spaceToCheck = boardSpaces[currentSpace.y][space.x]
                                        if let pawnToTake = spaceToCheck.occupyingPiece{
                                            game.board.move(previouslyTouchedPiece, space: space, piecetotake: pawnToTake)
                                            if (online){
                                                game.sendMove(fromSpace, toSpace: space, capturedSpace: spaceToCheck)
                                                fromSpace = spaceToCheck
                                            }
                                        }
                                    }
                                }
                                //Pawn moves again to the final destination 
                                game.board.move(previouslyTouchedPiece, space: space, piecetotake: nil)
                                if (online){
                                    game.sendMove(fromSpace, toSpace: space, capturedSpace: nil)
                                }
                                }else{
                                    game.board.move(previouslyTouchedPiece, space: space, piecetotake: nil)
                                if (online){
                                    game.sendMove(fromSpace, toSpace: space, capturedSpace: nil)
                                }
                                }
                            if !online{
                                game.newPlayerMove()
                            }else{
                                game.switchOnlineSide()
                            }
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
                //self.myLabel.text = "Touched Space: \(name)"
                //touchedNode.color = UIColor.yellowColor()
                
                
            }
        }
    }
   
    override func update(currentTime: CFTimeInterval) {
        /* Called before each frame is rendered */
    }
    
    func setupLabel() {
        self.myLabel.text = ""
        self.myLabel.fontColor = UIColor.blackColor()
        self.myLabel.fontSize = 20
        self.myLabel.position = CGPointMake(200, 625)
        
        self.addChild(myLabel)
        
    }
    
    func drawMenuBar(){
        let screenSize: CGRect = UIScreen.mainScreen().bounds
        let screenWidth = screenSize.width
        let screenHeight = screenSize.height
        let menuBar = SKSpriteNode()
        menuBar.name = "menuBar"
        menuBar.position = CGPoint(x: round(0), y: round(screenHeight*(8/9))+round(screenHeight*(1/18)))
        menuBar.size = CGSizeMake(screenWidth*2, screenHeight/9 + 10)
        menuBar.color = UIColor(red: 0.925, green: 0.941, blue: 0.945, alpha: 1)
        let board = self.childNodeWithName("blureffect") as! SKEffectNode
        board.addChild(menuBar)
        
        let buttoncolor = UIColor(red: 189/255, green: 195/255, blue: 199/255, alpha: 1)
        let buttonSize = CGSizeMake(50, 50)
        let buttonFont = "Helvetica"
        let buttonFontSize: CGFloat = 30
        let button = makeButton("close", position: CGPoint(x: screenSize.width*(9.2/10), y: -10), size: buttonSize, color: buttoncolor, label: "X", font: buttonFont, labelID: "close", fontSize: buttonFontSize, parent: menuBar)
        let label = button.childNodeWithName("close") as! SKLabelNode
        label.fontColor = UIColor.whiteColor()
        label.position = CGPoint(x: 1,y: -12)
    }
    
    func showMenu(){
        if (self.childNodeWithName("blur") != nil){
            return
        }
        self.addChild(self.menuParent)
        let board = self.childNodeWithName("blureffect") as! SKEffectNode
        board.filter = self.blurFilter
    }
    
    func clearMenu(){
        self.menuParent.removeFromParent()
        let board = self.childNodeWithName("blureffect") as! SKEffectNode
        board.filter = nil
    }
    
    func drawMenu() {
        let screenSize: CGRect = UIScreen.mainScreen().bounds
        let screenWidth = screenSize.width
        let screenHeight = screenSize.height
        
        self.blurFilter = CIFilter(name: "CIGaussianBlur")
        // Set the blur amount. Adjust this to achieve the desired effect
        let blurAmount = 20.0
        self.blurFilter!.setValue(blurAmount, forKey: kCIInputRadiusKey)
        let board = self.childNodeWithName("blureffect") as! SKEffectNode
        board.filter = self.blurFilter
        
        self.menuParent = SKSpriteNode()
        self.menuParent.name = "blur"
        self.menuParent.position = CGPoint(x: 0, y: 0)
        self.menuParent.size = CGSizeMake(screenWidth*2, screenHeight*2)
        self.menuParent.color = UIColor(red: 0, green: 0, blue: 0, alpha: 0.30)
        self.addChild(self.menuParent)
        self.menuParent.zPosition = 100
        let menu = SKSpriteNode()
        menu.name = "menu"
        menu.position = CGPoint(x: round(screenWidth/2), y: round(screenHeight/2))
        menu.size = CGSizeMake(screenWidth/2, screenHeight/2)
        menu.color = UIColor(red: 0.925, green: 0.941, blue: 0.945, alpha: 1)
        self.menuParent.addChild(menu)
        menu.zPosition = +1
        
        let buttoncolor = UIColor(red: 47/255, green: 129/255, blue: 183/255, alpha: 1)
        let buttonSize = CGSizeMake(200, 50)
        let buttonFont = "Helvetica"
        let buttonFontSize: CGFloat = 20
        let _ = makeButton("online", position: CGPoint(x: 0, y: 0), size: buttonSize, color: buttoncolor, label: "Play Online", font: buttonFont, labelID: "online", fontSize: buttonFontSize, parent: menu)
        let _ = makeButton("offline", position: CGPoint(x: 0, y: -65), size: buttonSize, color: buttoncolor, label: "Play Offline", font: buttonFont, labelID: "offline", fontSize: buttonFontSize, parent: menu)
        let _ = makeButton("bluetooth", position: CGPoint(x: 0, y: -130), size: buttonSize, color: buttoncolor, label: "Connect Bluetooth", font: buttonFont, labelID: "bluetooth", fontSize: buttonFontSize, parent: menu)
    }
    
    func makeButton(name: String, position: CGPoint, size: CGSize, color: UIColor, label: String, font: String, labelID: String, fontSize: CGFloat, parent: SKSpriteNode) -> SKSpriteNode{
        let button = SKSpriteNode()
        button.name = name
        button.position = position
        button.size = size
        button.color = color
        parent.addChild(button)
        button.zPosition = +1
        let buttonLabel = SKLabelNode(fontNamed: font)
        button.addChild(buttonLabel)
        buttonLabel.text = label
        buttonLabel.fontSize = fontSize
        buttonLabel.name = labelID
        buttonLabel.position = CGPointMake(CGRectGetMidX(button.frame), (CGRectGetMidY(button.frame)-8) - position.y)
        
        return button
    }
    
    
    func drawBoard() {
        let board = SKEffectNode()
        board.name = "blureffect"
        self.addChild(board)
        let screenSize: CGRect = UIScreen.mainScreen().bounds
        let screenWidth = screenSize.width
        let screenHeight = screenSize.height
        let lightColor = UIColor(red: 67/255, green: 179/255, blue: 255/255, alpha: 1)
        let darkColor = UIColor(red: 47/255, green: 129/255, blue: 183/255, alpha: 1)
        let alphas = ["A","B","C","D","E","F","G","H"]
        let numRows = 8
        let numCols = 8
        let squareSize = CGSizeMake(round(screenWidth/8), round(screenHeight/9))
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
                board.addChild(square)
                columnSection.append(square)
                toggle = !toggle
            }
            toggle = !toggle
            boardSpaces.append(columnSection)
        }
    }
}
