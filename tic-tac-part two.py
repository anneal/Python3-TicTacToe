import TicTacToe

        
def main():

    gameOn = True
    
    while gameOn:
        game = TicTacToe.TicTacToe(3,3)  # The number of rows and columns is entered as a constant
        game.begin()
        gameOn = game.over()

main()
