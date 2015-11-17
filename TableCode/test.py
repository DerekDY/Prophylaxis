from chessTable import *




def main():
    table = ChessTable()
    table.drawMotors()  
    table.initialize_Coord()  
    table.goto("E4")
    table.move("A2A4")
    table.win.getMouse()
    table.win.close() 
    
    
    
main()
