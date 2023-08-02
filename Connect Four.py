# Command line Connect Four implementation 

import numpy as np 

# This defines the attributes and methods required to conduct a game of connect four
class play: 
    
    # Creates game board, instantiates variables to keep track of turn and win status.
    def __init__(self):
        self.game_board = np.zeros((6, 7))   
        self.Turn = 1
        self.compare = lambda x, y: True if x == y else False
        self.Winner = 0
        self.Connect_Four = False
        
    # Static method to take user input and constrains inputs to integers between 1 and 7 corresponding to columns.
    @staticmethod
    def validate_user_input(turn):
        while True:
            player_input = input('This is player {}\'s turn. Please Enter a number between 1 and 7 \
                                 inclusive to indicate where you want to place your token. '.format(turn))
            if player_input.isnumeric():
                input_column = int(player_input)
                if input_column > 0 and input_column < 8:
                    break
                else:
                    print('Invalid Input. Please Enter number between 1 and 7 inclusive. ')
            else:
                print('Invalid Input. Please enter a valid number between 1 and 7 inclusive. ')
        return input_column
                
    # Simple function to flip turns
    def change_turn(self):
        if self.Turn == 1:
            self.Turn = 2
        else:
            self.Turn = 1
    
    # This calls function to get user input, then modifies game board as long as it is modifiable, then switches turns
    def play_round(self):
        move_not_made = True
        while move_not_made:
            print('\n')
            input_value = self.validate_user_input(self.Turn)
            for row in range(1, 7):
                if self.game_board[-row, input_value - 1] == 0:
                    self.game_board[-row, input_value - 1] = self.Turn
                    move_not_made = False
                    break
            if move_not_made:
                print('Sorry. While you gave a valid entry. There aren\'t available slots in that column. ')
        self.change_turn()            
    
    #Simple function to display the np array used to represent the connect four board
    def display_game_board(self):
        print('\n')
        print(self.game_board)
    
    # Checks for connect four on a left diagonal axis. Restrains to check cells only in the top right corner  as it 
    # is sufficient to check 12 cells to determine presence of left diagonal connect four.
    def check_left_diagonal(self):
        for row in range(0, 3):
            if self.Connect_Four == True: 
                break
            for column in range(3, 7):
                if self.game_board[row][column] != 0:
                    compare_list = []
                    compare_list.append(self.compare(self.game_board[row][column], self.game_board[row+1][column-1]))
                    compare_list.append(self.compare(self.game_board[row][column], self.game_board[row+2][column-2]))
                    compare_list.append(self.compare(self.game_board[row][column], self.game_board[row+3][column-3]))
                    if all(compare_list): 
                        self.Connect_Four = True
                        self.Winner = self.game_board[row][column]
                        break
    
    # Checks for connect four on a right diagonal axis. Restrains to check cells only in the top left corner as it 
    # is sufficient to check 12 cells to determine presence of right diagonal connect four.
    def check_right_diagonal(self):
        for row in range(0, 3):
            if self.Connect_Four == True: 
                break
            for column in range(0, 4):
                if self.game_board[row][column] != 0:
                    compare_list = []
                    compare_list.append(self.compare(self.game_board[row][column], self.game_board[row+1][column+1]))
                    compare_list.append(self.compare(self.game_board[row][column], self.game_board[row+2][column+2]))
                    compare_list.append(self.compare(self.game_board[row][column], self.game_board[row+3][column+3]))
                    if all(compare_list): 
                        self.Connect_Four = True
                        self.Winner = self.game_board[row][column]
                        break
    
    # Checks for connect four on horizontal axis. Restrains to check cells only in the left half as it 
    # is sufficient to determine presence of horizontal connect four.
    def check_horizontal(self):
        for row in range(0, 6):
            if self.Connect_Four == True: 
                break
            for column in range(0, 4):
                if self.game_board[row][column] != 0:
                    compare_list = []
                    compare_list.append(self.compare(self.game_board[row][column], self.game_board[row][column+1]))
                    compare_list.append(self.compare(self.game_board[row][column], self.game_board[row][column+2]))
                    compare_list.append(self.compare(self.game_board[row][column], self.game_board[row][column+3]))
                    if all(compare_list): 
                        self.Connect_Four = True
                        self.Winner = self.game_board[row][column]
                        break
    
    # Checks for connect four on vertical axis. Restrains to check cells only in the left half as it 
    # is sufficient to determine presence of horizontal connect four.
    def check_vertical(self):
        for row in range(0, 3):
            if self.Connect_Four == True: 
                break
            for column in range(0, 7):
                if self.game_board[row][column] != 0:
                    compare_list = []
                    compare_list.append(self.compare(self.game_board[row][column], self.game_board[row+1][column]))
                    compare_list.append(self.compare(self.game_board[row][column], self.game_board[row+2][column]))
                    compare_list.append(self.compare(self.game_board[row][column], self.game_board[row+3][column]))
                    if all(compare_list): 
                        self.Connect_Four = True
                        self.Winner = self.game_board[row][column]
                        break
    
    #Function that calls on all possible win conditions. Can be refracted to quit early when win is found.
    def check_win_condition(self):
        self.check_left_diagonal()
        self.check_right_diagonal()
        self.check_vertical()
        self.check_horizontal()

# Instantiate game play
current_game = play()
current_game.display_game_board()


# This is the main game loop, consisting of player move, game display and checking if there is a winner
while True:    
    current_game.play_round()
    current_game.display_game_board()
    current_game.check_win_condition()
    if current_game.Connect_Four == True:
        print('We have a Winner. It is player {}.'.format(current_game.Winner))
        break