var app = require('http').createServer()

app.listen(8900)

function Player(socket) {
    var self = this
    this.socket = socket
    this.name = ""
    this.game = {}

    this.socket.on("playerMove", function(fromSpace, toSpace, capturedSpace) {
        console.log("Recieved Move")
        self.game.playerMove(self, fromSpace, toSpace, capturedSpace)
    })

    this.socket.on("switchTurn", function() {
        console.log("Move Over - Changing Side")
        self.game.changeTurn(self)
    })

    this.socket.on("disconnect", function() {
        console.log(this["name"] + " has disconected")
        self.game.disconnectedPlayer()
        //self.game.changeTurn(self)
    })

    this.socket.on("endGame", function() {
        console.log(this["name"] + " has ended the game")
        self.game.gameOver()
    })

    this.socket.on("error", function() {
        console.log(this["name"] + " has created an error")
        //self.game.changeTurn(self)
    })
}

Player.prototype.joinGame = function(game) {
    this.game = game
}

function Game() {
    this.io = require('socket.io')(app)
    this.player1 = null
    this.player2 = null
    this.currentTurn = "White"
    this.started = false
    this.addHandlers()
}

Game.prototype.addHandlers = function() {
    var game = this
    console.log("Handlers added")
    console.log("Waiting for Players")
    this.io.sockets.on("connection", function(socket) {
        game.addPlayer(new Player(socket))
    })
}

Game.prototype.addPlayer = function(player) {
    console.log("adding player")
    if (this.player1 === null) {
        this.player1 = player
        this.player1["game"] = this
        this.player1["name"] = "White"
        this.player1.socket.emit("name", "White")
    } else if (this.player2 === null) {
        this.player2 = player
        this.player2["game"] = this
        this.player2["name"] = "Black"
        this.player2.socket.emit("name", "Black")
        this.startGame()  // starting the game 
    }else{
        player.socket.emit("gameFull")
        console.log("Nothing Happened")
    }
    
}

Game.prototype.announceWin = function(player, type) {
    this.player1.socket.emit("win", player["name"], type)
    this.player2.socket.emit("win", player["name"], type)
    this.resetGame()
}

Game.prototype.gameOver = function() {
    this.player1.socket.emit("gameOver")
    this.player2.socket.emit("gameOver")
    this.currentTurn = "White"
    this.started = false
}

Game.prototype.disconnectedPlayer = function(player) {
    try {
        this.player1.socket.emit("error")
        this.player2.socket.emit("error")
    }catch(err) {
        console.log("Player already disconected")
    }
    this.player1 = null
    this.player2 = null
    
}

Game.prototype.playerMove = function(player, fromSpace, toSpace, capturedSpace) {
    if (player["name"] !== this.currentTurn) {
        console.log("Throwing out Move")
        return
    }
    if (player["name"] === "White") {
        this.player2.socket.emit("playerMove", fromSpace, toSpace, capturedSpace)
    } else {
        this.player1.socket.emit("playerMove", fromSpace, toSpace, capturedSpace)
    }
}

Game.prototype.changeTurn = function(player){
    if (player["name"] === "White") {
        this.currentTurn = "Black"
        this.player1.socket.emit("currentTurn", "Black")
        this.player2.socket.emit("currentTurn", "Black")
    } else {
        this.currentTurn = "White"
        this.player1.socket.emit("currentTurn", "White")
        this.player2.socket.emit("currentTurn", "White")
    }

    console.log("CURRENT TURN")
    console.log(this.currentTurn)
}

Game.prototype.startGame = function() {
    this.player1.socket.emit("startGame")
    this.player2.socket.emit("startGame")
}

// Start the game server
var game = new Game()