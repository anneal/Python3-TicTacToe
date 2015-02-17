############################
#
# This is the Tic Tac Toe program
#
############################


# This line imports the class file for TicTacToe.py
import TicTacToe



# The main function is defined        
def main():

    gameOn = True
    
    while gameOn:
        game = TicTacToe.TicTacToe(3,3)  # The number of rows and columns is entered as a constant. In future revisions, this could be user input. 
        game.begin()
        gameOn = game.over()



# The main function is called
main()
