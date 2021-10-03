"""
Tic Tac Toe Player
"""

import math

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
    count = 0
    for i in board:
        for j in board[i]:
            if board[i, j] != EMPTY:
                count += 1
    if count % 2 == 0:
        return X
    else:
        return O
    
    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionset = set()
    for i in board:
        for j in board[i]:
            if board[i][j] == Empty:
                actionset.add([i, j])
        return actionset

    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newstate = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]
    for i in board:
        for j in board[i]:
            newstate[i][j] = board[i,j]
    if action[0] > 2:
        raise Exception("invalid i action")
    if action[1] > 2:
        raise Exception("invalid j action")
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("invalid action")
    else:
        ival = action[0]
        jval = action[1]
        if player(board) == X:
            newstate[ival][jval] = X
        else:
            newstate[ival][jval] = O
    return newstate


    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0, 0] == board[0, 1] == board[0, 2]:
        if board[0, 0] == X:
            return X
        else:
            return O

    elif board[1, 0] == board[1, 1] == board[1, 2]:
        if board[1, 0] == X:
            return X
        else:
            return O

    elif board[2, 0] == board[2, 1] == board[2, 2]:
        if board[2, 0] == X:
            return X
        else:
            return O

    elif board[0, 0] == board[1, 0] == board[2, 0]:
        if board[0, 0] == X:
            return X
        else:
            return O

    elif board[0, 1] == board[1, 1] == board[2, 1]:
        if board[0, 1] == X:
            return X
        else:
            return O

    elif board[0, 2] == board[1, 2] == board[2, 2]:
        if board[0, 2] == X:
            return X
        else:
            return O

    elif board[0, 0] == board[1, 1] == board[2, 2]:
        if board[0, 0] == X:
            return X
        else:
            return O

    elif board[0, 2] == board[1, 1] == board[2, 0]:
        if board[0, 2] == X:
            return X
        else:
            return O

    #raise NotImplementedError

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    count = 0
    for i in board:
        if i != EMPTY:
            count += 1
    if count == 9:
        return True
    elif winner(board) == X or O:
        return True
    else:
        return False
    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    value = Empty
    if winner(board) == X:
        value = 1
    elif winner(board) == O:
        value = -1
    else:
        value = 0
    return value

   # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    player(board)
    actions(board)
    for i in actionset:
        result(board, i)
        minimax(newstate)



  #raise NotImplementedError
