import math
import copy

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
    if any(None in row for row in board):
        Xcount = sum(row.count("X") for row in board)
        Ocount = sum(row.count("O") for row in board)

        if Xcount == Ocount:
            return "X"
        else:
            return "O"
    else:
        return


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    options = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                options.add((i,j))
    return options


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if i < 3 and j < 3 and board[i][j] is EMPTY:
        name = player(board)
        new_board = copy.deepcopy(board)
        new_board[i][j] = name
        return new_board
    else:
        raise Exception('Invalid move')


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == "X":
            return "X"
        elif board[i][0] == board[i][1] == board[i][2] == "O":
            return "O"
    # Check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == "X":
            return "X"
        elif board[0][i] == board[1][i] == board[2][i] == "O":
            return "O"
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == "X":
        return "X"
    if board[0][0] == board[1][1] == board[2][2] == "O":
        return "O"
    if board[0][2] == board[1][1] == board[0][2] == "X":
        return "X"
    if board[0][2] == board[1][1] == board[0][2] == "O":
        return "O"
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    if any(None in row for row in board):
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return -1
    else:
        return 0


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -1
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
        if v == 1:
            break
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = 1
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
        if v == -1:
            break
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == "X":
        v = -1
        best = (1, 1)
        count = sum(row.count(EMPTY) for row in board)
        if count == 9:
            return best
        for action in actions(board):
            move_value = min_value(result(board, action))
            if move_value == 1:
                best = action
            if move_value > v:
                best = action
        return best
    if player(board) == "O":
        v = 1
        best = (1, 1)
        for action in actions(board):
            move_value = max_value(result(board, action))
            if move_value == -1:
                best = action
            if move_value < v:
                best = action
        return best

