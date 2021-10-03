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
    board = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]
    return board


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    rows = 3
    columns = 3
    for i in range(rows):
        for j in range(columns):
            if board[i][j] != EMPTY:
                count += 1
    if count % 2 == 0:
        player = X
    else:
        player = O
    return player

    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionset = set()
    rows = 3
    columns = 3
    for i in range(rows):
        for j in range(columns):
            if board[i][j] == EMPTY:
                actionset.add((i,j))
    return actionset

    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newstate = [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]
    rows = 3
    columns = 3
    for i in range(rows):
        for j in range(columns):
            newstate[i][j] = board[i][j]
#    print(newstate)
#    print(action)
    ival = action[0]
    jval = action[1]
    if ival > 2:
        raise Exception("invalid i action")
    if jval > 2:
        raise Exception("invalid j action")
    if board[ival][jval] != EMPTY:
        raise Exception("invalid action")
    else:
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
    if board[0][0] == board[0][1] == board[0][2] != EMPTY:
        if board[0][0] == X:
            return X
        else:
            return O

    elif board[1][0] == board[1][1] == board[1][2] != EMPTY:
        if board[1][0] == X:
            return X
        else:
            return O

    elif board[2][0] == board[2][1] == board[2][2] != EMPTY:
        if board[2][0] == X:
            return X
        else:
            return O

    elif board[0][0] == board[1][0] == board[2][0] != EMPTY:
        if board[0][0] == X:
            return X
        else:
            return O

    elif board[0][1] == board[1][1] == board[2][1] != EMPTY:
        if board[0][1] == X:
            return X
        else:
            return O

    elif board[0][2] == board[1][2] == board[2][2] != EMPTY:
        if board[0][2] == X:
            return X
        else:
            return O

    elif board[0][0] == board[1][1] == board[2][2] != EMPTY:
        if board[0][0] == X:
            return X
        else:
            return O

    elif board[0][2] == board[1][1] == board[2][0] != EMPTY:
        if board[0][2] == X:
            return X
        else:
            return O
    else:
        return None

    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    var = winner(board)
    count = 0
    rows = 3
    columns = 3
    for i in range(rows):
        for j in range(columns):
            if board[i][j] != EMPTY:
                count += 1
    if count == 9 or var is not None:
        return True
    else:
        return False

    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    value = 0
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
    actionset = actions(board)
    retaction = []
    if player(board) == X:
        v = -10
    else:
        v = 10
    for action in actionset:
        if player(board) == X:
            retvalue = minvalue(result(board, action))
            if retvalue > v:
                v = retvalue
                retaction.clear()
                retaction.extend(list(action))
        else:
            retvalue = maxvalue(result(board, action))
            if retvalue < v:
                v = retvalue
                retaction.clear()
                retaction.extend(list(action))

    return tuple(retaction)

def minvalue(board):
    if terminal(board):
        return utility(board)
    v = 10
    actionset = actions(board)
    for action in actionset:
        retvalue = maxvalue(result(board, action))
        if retvalue < v:
            v = retvalue
    return v


def maxvalue(board):
    if terminal(board):
        return utility(board)
    v = -10
    actionset = actions(board)
    for action in actionset:
        retvalue = minvalue(result(board, action))
        if retvalue > v:
            v = retvalue
    return v

  #raise NotImplementedError