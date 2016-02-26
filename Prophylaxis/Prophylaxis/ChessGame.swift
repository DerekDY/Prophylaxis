//
//  ChessGame.swift
//  Chess
//
//  Created by Jack Cousineau on 10/14/15.
//




/**
 Holds a captured `ChessPiece` and the `NSImageView` that it's being displayed in.
*/
//struct CapturedPieceImageView{
//    var piece: ChessPiece!
//    var imageView: NSImageView!
//}

/**
 Completely encapsulates an instance of a chess game.
*/
class ChessGame{
    
    let board : Board!
    let whitePlayerName: String!, blackPlayerName: String!
    
    var playerTurn = PieceColor.White
    
    //var whiteCapturedPieces = [CapturedPieceImageView](), blackCapturedPieces = [CapturedPieceImageView]()
    
    /**
     Displays the captured piece in the game's interface.
     
     - Parameter piece: The ChessPiece to display.
     */
//    func displayCapturedPiece(piece: ChessPiece){
//        
//        var pieceArray : [CapturedPieceImageView]!
//        
//        // We decide which array to insert the piece into, based on the piece's color.
//        if(piece.pieceColor == PieceColor.Black){
//            pieceArray = whiteCapturedPieces
//        }
//        else{
//            pieceArray = blackCapturedPieces
//        }
//        
//        for i in 0...15{
//            if(pieceArray[i].piece == nil){
//                // Once we find the first available slot in pieceArray, we store the piece in that slot, and display the piece's icon.
//                pieceArray[i].piece = piece
//                pieceArray[i].imageView.image = piece.pieceImage
//                return
//            }
//        }
//    }

    /**
     The ChessGame class constructor.
     
     - Parameter gameType: The `GameType` of the game.  todo
     - Parameter whitePlayerName: The name of white side's player.
     - Parameter blackPlayerName: The name of black side's player.
     */
    
    
    init(whitePlayerName: String, blackPlayerName: String, board: [[BoardSpace]]){
        self.blackPlayerName = blackPlayerName
        self.whitePlayerName = whitePlayerName
        
        //gameWindow.title = whitePlayerName + " vs " + blackPlayerName + ", ft. John Cena"
        self.board = Board(boardspaces: board)
        self.board.populateBoard()
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
        print("Black in check: \(board.blackInCheck)")
        print("White in check: \(board.whiteInCheck)")
        
    }

}