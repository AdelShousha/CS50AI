"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

BOARD_LEN = 3
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # counting the number of X and O
    x_num = 0
    o_num = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_num +=1
            elif cell == O:
                o_num +=1
    # the X player playes when the two option are equal because he is the first to play
    if x_num <= o_num:
        return X
    else:
        return O        


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # loop throw each square and add its index to action set if square is empty
    action_set = set()
    for i in range(BOARD_LEN):
        for j in range(BOARD_LEN):
            if board[i][j] == EMPTY:
                action_set.add((i,j))
    return action_set            
      

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # check if the square corresponding to action is empty
    new_board = deepcopy(board)
    i = action[0]
    j = action[1]
    if board[i][j] != EMPTY:
        raise ValueError("Invalid Action")

    # Add the action to the new board and return the new board
    new_board[i][j] = player(new_board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # for each row check if all element of a row are the same then return the first element of the row (X or O)
    for i in range(BOARD_LEN):
         if len(set(board[i])) == 1:
            return board[i][0]
    # check if all element of the diagonal(top right to bottom left) are the same then return the middle element of the diagonal (X or O)
    if board[1][1] == board[0][0] == board[2][2] == O or board[1][1] == board[0][0] == board[2][2] == X:
        return board [0][0]
   
    # rotate the board then repeat the previous proccess
    board = list(zip(*reversed(board)))

    for i in range(BOARD_LEN):
         if len(set(board[i])) == 1:
            return board[i][0]
    if board[1][1] == board[0][0] == board[2][2] == O or board[1][1] == board[0][0] == board[2][2] == X:
        return board [0][0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # return true if there is a winner 
    if winner(board):
        return True
    # return true if all squares are filled
    counter = 0
    for i in range(BOARD_LEN):
        for j in range(BOARD_LEN):
            if board[i][j] == EMPTY:
                counter += 1
    return True if counter == 0 else False   
       
        
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    my_player = player(board)
    
    if my_player == X:
        # getting the first action that corresponds with the current board value 
        v = max_value(board) 
        for action in actions(board):
            if v == min_value(result(board, action)):
                return action

    elif my_player == O:
        # getting the first action that corresponds with the current board value
        v = min_value(board) 
        for action in actions(board):
            if v == max_value(result(board, action)):
                return action    

# find max value of board
def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
         v = max(v, min_value(result(board, action)))
    return v

# find min value of board
def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
         v = min(v, max_value(result(board, action)))
    return v


