//
//  ChessGame.swift
//  Chess
import SpriteKit

/**
 Completely encapsulates an instance of a chess game.
*/
class ChessGame{
    
    let socket = SocketIOClient(socketURL: "192.168.1.253:8900")
    let board : Board!
    var onlineSide: PieceColor! = PieceColor.White
    let whitePlayerName: String!, blackPlayerName: String!
    var gameStarted = false
    var onlineGame = false
    var myLabel: SKLabelNode!
    
    var playerTurn = PieceColor.White

    /**
     The ChessGame class constructor.
     
     - Parameter gameType: The `GameType` of the game.  todo
     - Parameter whitePlayerName: The name of white side's player.
     - Parameter blackPlayerName: The name of black side's player.
     */
    
    
    init(whitePlayerName: String, blackPlayerName: String, board: [[BoardSpace]], label: SKLabelNode){
        self.blackPlayerName = blackPlayerName
        self.whitePlayerName = whitePlayerName
        //gameWindow.title = whitePlayerName + " vs " + blackPlayerName + ", ft. John Cena"
        self.board = Board(boardspaces: board)
        self.board.populateBoard()
        self.myLabel = label
    }
    
    func playOnline(){
        print("Reached Playing Online")
        self.addHandlers()
        print("connecting to socket")
        self.socket.connect()
        self.onlineGame = true
        self.myLabel.text = "Waiting for other Player"
    }
    
    func addHandlers() {
        print("Adding Handlers")
        self.socket.on("startGame") {[weak self] data, ack in
            self?.handleStart()
            return
        }
        
        self.socket.on("playerMove") {
            [weak self] data, ack in
            print("Recieved a move")
            if let fromSpace = data[0] as? [Int], toSpace = data[1] as? [Int], capturedSpace = data[2] as? [Int]{
                self?.handlePlayerMove(fromSpace, toSpace: toSpace, capturedSpace: capturedSpace)
            }
        }
        
        self.socket.on("win") {
            [weak self] data, ack in
            if let name = data[0] as? String{
                print(name)
            }
        }
        
        self.socket.on("gameOver") {
            [weak self] data, ack in
            self!.myLabel.text = "Game Ended"
            self!.handleEndGame()
        }
        
        self.socket.on("name") {
            [weak self] data, ack in
            if let name = data[0] as? String{
                print("Playing as \(name)")
                if name == "Black"{
                    self?.onlineSide = PieceColor.Black
                }
            }
        }
        
        self.socket.on("currentTurn") {
            [weak self] data, ack in
            self!.newPlayerMove()
        }
        
        self.socket.on("gameReset") {
            [weak self] data, ack in
            print(data)
            
        }
        
        self.socket.on("gameOver") {
            [weak self] data, ack in
            self!.handleEndGame()
            
            
        }
        
        self.socket.onAny {print("Got event: \($0.event), with items: \($0.items)")}
    }
    
    
    func handleCurrentTurn(name:String) {
    }
    
    func handleDraw() {
    }
    
    func handleGameReset() {
    }
    
    func handleEndGame() {
        if onlineGame{
            self.socket.disconnect()
            self.onlineGame = false
        }
        self.board.unhighlightSpaces()
        self.board.emptyBoard()
        self.board.populateBoard()
        self.gameStarted = false
        self.playerTurn = PieceColor.White
        self.onlineSide = PieceColor.White
        self.myLabel.text = "Game Ended..."
    }
    
    func handlePlayerMove(fromSpace:[Int], toSpace:[Int], capturedSpace: [Int]) {
        let thisBoard = self.board
        var capturedPiece: ChessPiece! = nil
        let thisBoardSpaces = thisBoard.boardSpaces
        let thisBoardFrom = thisBoardSpaces[fromSpace[1]][fromSpace[0]]
        var thisBoardTo: BoardSpace! = nil
        let thisBoardPiece = thisBoardFrom.childNodeWithName("Piece") as! ChessPiece
        if capturedSpace[0] != 10{
            capturedPiece = thisBoardSpaces[capturedSpace[1]][capturedSpace[0]].childNodeWithName("Piece") as! ChessPiece
        }
        if toSpace[0] != 10{
            thisBoardTo = thisBoardSpaces[toSpace[1]][toSpace[0]]
        }
        thisBoard.move(thisBoardPiece, space: thisBoardTo, piecetotake: capturedPiece)
    }
    
    func handleStart() {
        self.gameStarted = true
        self.myLabel.text = "Game Started!"
        
    }
    
    
    func sendMove(fromSpace: BoardSpace, var toSpace: BoardSpace!, var capturedSpace: BoardSpace!){
        if capturedSpace == nil{
            capturedSpace = BoardSpace(squareSize: nil, spaceColor: nil, x: 10, y: 10) //fake space
        }
        if toSpace == nil{
            toSpace = BoardSpace(squareSize: nil, spaceColor: nil, x: 10, y: 10) //fake space
        }
        print("SENDING MOVE!!!!!")
        self.socket.emit("playerMove", [fromSpace.x, fromSpace.y], [toSpace.x, toSpace.y], [capturedSpace.x, capturedSpace.y])
    }
    
    
    
    func resetGame(){
        if self.onlineGame{
            self.socket.emit("endGame")
        }else{
            handleEndGame()
        }
    }
    
    func switchOnlineSide(){
        self.socket.emit("switchTurn")
    }
    /**
     Changes which player's turn it is.
     */
    func newPlayerMove(){
        if(playerTurn == .White){
            playerTurn = .Black
            board.newMoveReset(PieceColor.Black)
            board.boardInCheck(.Black)
            if board.blackInCheck{
                if board.boardInCheckMate(.Black){
                    print("White WINS")
                }
            }
            //chessBoard.currentPlayerTurnLabel.stringValue = blackPlayerName + "'s"
        }
        else{
            playerTurn = .White
            board.newMoveReset(PieceColor.White)
            board.boardInCheck(.White )
            if board.whiteInCheck{
                if board.boardInCheckMate(.White){
                    print("Black WINS")
                }
            }
            //chessBoard.currentPlayerTurnLabel.stringValue = whitePlayerName + "'s"
        }
        self.myLabel.text = "\(self.playerTurn)'s Move"
        print("Black in check: \(board.blackInCheck)")
        print("White in check: \(board.whiteInCheck)")
        if self.onlineGame && self.playerTurn == self.onlineSide{
            self.myLabel.text = "Your Move!"
        }
        
    }

}