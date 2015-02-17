############################
#
# The class TicTacToe is defined in this file
#
############################



class TicTacToe():



    # When an instance of the class is created, an empty game board and a populated selection board are created
    def __init__(self, NUM_ROWS, NUM_COLS):
        
        self.board = [[0 for i in range(NUM_COLS)] for j in range(NUM_ROWS)]
        self.coords = [[str(chr(97 + i) + str(j + 1)) for i in range(NUM_COLS)] for j in range(NUM_ROWS)]
        self.replay = False



    # This returns the value of the replay variable. If the game is over, the value will be False
    def over(self):
        return self.replay


    
    # The game board is displayed
    def displayBoard(self):

        #print('\n'*100)
        print('\nThe game board is:  (You are \'O\'.)')

        num_rows = len(self.board)
        num_cols = len(self.board[0])
        
        for rows in range(num_rows):
            print('\n' + '------'*num_rows + '-\t\t' + '------'*num_rows + '-')
            for cols in range(num_cols):
                print('|',end='')
                if self.board[rows][cols] == 0:
                    print('     ',end='')
                elif self.board[rows][cols] == -1:
                    print('  X  ',end='')
                else:
                    print('  O  ',end='')
            print('|' + '\t\t' + '|  ',end='')
            for cols in range(num_cols):
                print(self.coords[rows][cols] + ' |  ',end='')
        print('\n' + '------'*num_rows + '-\t\t' + '------'*num_rows + '-')



    # The user's move is requested
    def getUserMove(self):
        
        move = input('\nWhere would you like to play?\t')
        move = move.lower()

        num_rows = len(self.board)
        num_cols = len(self.board[0])

        valid_input = False

        # Test that the input is a valid move. If so, make the move.
        for r in range(num_rows):
            for c in range(num_cols):
                if move == self.coords[r][c]:
                    valid_input = True
                    self.board[r][c] = 2
                    self.coords[r][c] = '  '
                    break

        if not valid_input:
            print('\nThat move is not valid. Please enter another move.')
            self.getUserMove()
        else:
            self.turn = False
            self.checkTie()



    # The game begins by asking the user if they would like to play first or second
    def begin(self):

        first_turn = input('\nWelcome to a game of tic-tac-toe. Would you like to go first? (y/n)\t')
        
        if first_turn.upper() == 'Y':
            self.turn = True
            self.displayBoard()
            self.getUserMove()
        else:
            self.turn = False
            self.move()



    # The game board is checked for a tie, then calls to check for a winner
    def checkTie(self):
        
        taken_spaces = [1 for row in self.coords for value in row if value.isspace()]

        if sum(taken_spaces) == len(self.coords) * len(self.coords[0]):
            if not self.turn:
                self.displayBoard()
            print('\nTie Game.')
            play_again = input('\nWould you like to play again? (y/n)\t')
            if play_again.upper() == 'Y':
                self.replay = True
            else:
                self.replay = False
        else:
            self.findWinner()



    # The game board is checked for a winner
    def findWinner(self):
        
        user_won = computer_won = False

        num_rows = len(self.board)
        num_cols = len(self.board[0])
            
        # Check each row for a win
        for row in self.board:
            if sum(row) == 2 * (num_cols):
                user_won = True
            elif sum(row) == -1 * (num_cols):
                computer_won = True

        # Check each column for a win
        transposed_board = [[row[j] for row in self.board] for j in range(num_cols)]
        for row in transposed_board:
            if sum(row) == 2 * (num_cols):
                user_won = True
            elif sum(row) == -1 * (num_cols):
                computer_won = True

        # Check each diagonal for a win
        diags = []
        diags.append([self.board[j][k] for j in range(num_cols) \
                 for k in range(num_rows) \
                 if (j == k)])
        diags.append([self.board[j][k] for j in range(num_cols) \
                 for k in range(num_rows) \
                 if (j + k) == (num_cols- 1)])

        for row in diags:
            if sum(row) == (2 * num_cols):
                user_won = True
            elif sum(row) == (-1 * num_cols):
                computer_won = True

        if not user_won and not computer_won:
            if self.turn:
                self.getUserMove()
            else:
                self.move()
        elif user_won:
            print('\nYOU WON!!!!')
            play_again = input('\nWould you like to play again? (y/n)\t')
            if play_again.upper() == 'Y':
                self.replay = True
            else:
                self.replay = False
        else:
            print('\nWhomp whomp. You lost.')
            play_again = input('\nWould you like to play again? (y/n)\t')
            if play_again.upper() == 'Y':
                self.replay = True
            else:
                self.replay = False



    # Determine the computer's move
    def move(self):

        move_found = False

        num_rows = len(self.board)
        num_cols = len(self.board[0])

        # Check each row for a win
        row_count = 0
        for row in self.board:
            if sum(row) == -1 * (num_cols - 1) and not move_found:
                for j in range(num_cols):
                    if self.board[row_count][j] == 0:
                        self.board[row_count][j] = -1
                        self.coords[row_count][j] = '  '
                        move_found = True
                        break
            row_count += 1

        # Check each column for a win
        if not move_found:
            transposed_board = [[row[j] for row in self.board] for j in range(num_cols)]
            row_count = 0
            for row in transposed_board:
                if (sum(row) == -1 * (num_cols - 1)) and not move_found:
                    for j in range(num_cols):
                        if transposed_board[row_count][j] == 0:
                            self.board[j][row_count] = -1
                            self.coords[j][row_count] = '  '
                            move_found = True
                row_count += 1

        # Check each diagonal for a win
        if not move_found:
            diags = []
            diags.append([self.board[j][k] for j in range(num_cols) \
                     for k in range(num_rows) \
                     if (j == k)])
            diags.append([self.board[j][k] for j in range(num_cols) \
                     for k in range(num_rows) \
                     if (j + k) == (num_cols - 1)])

            row_count = 0
            for row in diags:
                if (sum(row) == -1 * (num_cols - 1)) and not move_found:
                    for j in range(num_cols):
                        if diags[row_count][j] == 0 and row_count == 0:
                            self.board[j][j] = -1
                            self.coords[j][j] = '  '
                            move_found = True
                        elif diags[row_count][j] == 0:
                            self.board[j][num_cols - 1 - j] = -1
                            self.coords[j][num_cols - 1 - j] = '  '
                            move_found = True
                row_count += 1

        # Check each row for a block
        if not move_found:
            row_count = 0
            for row in self.board:
                if sum(row) == 2 * (num_cols - 1) and not move_found:
                    for j in range(num_cols):
                        if self.board[row_count][j] == 0:
                            self.board[row_count][j] = -1
                            self.coords[row_count][j] = '  '
                            move_found = True
                            break
                row_count += 1

        # Check each column for a block
        if not move_found:
            transposed_board = [[row[j] for row in self.board] for j in range(num_cols)]
            row_count = 0
            for row in transposed_board:
                if (sum(row) == 2 * (num_cols - 1)) and not move_found:
                    for j in range(num_cols):
                        if transposed_board[row_count][j] == 0:
                            self.board[j][row_count] = -1
                            self.coords[j][row_count] = '  '
                            move_found = True
                row_count += 1

        # Check each diagonal for a block
        if not move_found:
            diags = []
            diags.append([self.board[j][k] for j in range(num_cols) \
                     for k in range(num_rows) \
                     if (j == k)])
            diags.append([self.board[j][k] for j in range(num_cols) \
                     for k in range(num_rows) \
                     if (j + k) == (num_cols - 1)])

            row_count = 0
            for row in diags:
                if (sum(row) == 2 * (num_cols - 1)) and not move_found:
                    for j in range(num_cols):
                        if diags[row_count][j] == 0 and row_count == 0:
                            self.board[j][j] = -1
                            move_found = True
                        elif diags[row_count][j] == 0:
                            self.board[j][num_cols - 1 - j] = -1
                            self.coords[j][num_cols - 1 - j] = '  '
                            move_found = True
                row_count += 1


        # Make a strategic play along the diagonal
        if not move_found:
            r = num_rows - 2
            c = num_cols - 2
            within_board = True
            
            while not move_found and within_board:
                if self.board[r][c] == 0:
                    move_found = True
                    self.board[r][c] = -1
                    self.coords[r][c] = '  '
                r -= 1
                c -= 1
                if r == -1 and c == -1:
                    within_board = False
                elif r == -1:
                    r = 0
                elif c == -1:
                    c = 0
    
        # Make a play anywhere
        if not move_found:
            for r in range(num_rows):
                for c in range(num_cols):
                    if self.board[r][c] == 0 and not move_found:
                        move_found = True
                        self.board[r][c] = -1
                        self.coords[r][c] = '  '
                
        if move_found:
            self.turn = True
            self.displayBoard()
            self.checkTie()
        else:
            print('UHOH')

