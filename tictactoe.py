"""
Tic Tac Toe Player
"""

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
    # using the no of empty state in th table and the first turn is always given to x and also a player doesn't have the liberty to not play one chance
    no_of_emptystates = 0

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == EMPTY:
                no_of_emptystates += 1

    if no_of_emptystates % 2 == 0:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                action.add((i, j))

    return (action)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    player1 = player(new_board)

    if new_board[action[0]][action[1]] != EMPTY:
        raise NameError('Action is invalid')

    new_board[action[0]][action[1]] = player1

    return (new_board)


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # checking if x or o won vertically
    if board[0][0] == X and board[1][0] == X and board[2][0] == X:
        return (X)
    elif board[0][1] == X and board[1][1] == X and board[2][1] == X:
        return (X)
    elif board[0][2] == X and board[1][2] == X and board[2][2] == X:
        return (X)

    elif board[0][0] == O and board[1][0] == O and board[2][0] == O:
        return (O)
    elif board[0][1] == O and board[1][1] == O and board[2][1] == O:
        return (O)
    elif board[0][2] == O and board[1][2] == O and board[2][2] == O:
        return (O)


    # checking if x or o won horizontally
    elif board[0][0] == X and board[0][1] == X and board[0][2] == X:
        return (X)
    elif board[1][0] == X and board[1][1] == X and board[1][2] == X:
        return (X)
    elif board[2][0] == X and board[2][1] == X and board[2][2] == X:
        return (X)

    elif board[0][0] == O and board[0][1] == O and board[0][2] == O:
        return (O)
    elif board[1][0] == O and board[1][1] == O and board[1][2] == O:
        return (O)
    elif board[2][0] == O and board[2][1] == O and board[2][2] == O:
        return (O)


    # checking if x or o won diagonally
    elif board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return (X)
    elif board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return (X)

    elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return (O)
    elif board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return (O)


    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_state = 0
    winning_player = winner(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                empty_state += 1

    if empty_state == 0:
        return True

    elif winning_player == X or winning_player == O:
        return True

    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board) == True:
        winning_player = winner(board)
        if winning_player == X:
            return 1
        elif winning_player == O:
            return -1
        else:
            return 0


def min_value(board):
    if terminal(board) == True:
        return utility(board)
    v = 100
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def max_value(board):
    if terminal(board) == True:
        return utility(board)
    v1 = -100
    for action in actions(board):
        v1 = max(v1, min_value(result(board, action)))
    return v1


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None

    playing_player = player(board)
    if playing_player == X:
        maximum_list = []
        for action in actions(board):
            maximum = min_value(result(board, action))
            maximum_list.append([action, maximum])

        for i in range(len(maximum_list)):
            for j in range(len(maximum_list[i]) - 1):
                if maximum_list[i][j + 1] == 1:
                    return maximum_list[i][j]

        for i in range(len(maximum_list)):
            for j in range(len(maximum_list[i]) - 1):
                if maximum_list[i][j + 1] == 0:
                    return maximum_list[i][j]

        for i in range(len(maximum_list)):
            for j in range(len(maximum_list[i]) - 1):
                if maximum_list[i][j + 1] == -1:
                    return maximum_list[i][j]

    if playing_player == O:
        minimum_list = []
        for action in actions(board):
            minimum = max_value(result(board, action))
            minimum_list.append([action, minimum])

        for i in range(len(minimum_list)):
            for j in range(len(minimum_list[i]) - 1):
                if minimum_list[i][j + 1] == -1:
                    return minimum_list[i][j]

        for i in range(len(minimum_list)):
            for j in range(len(minimum_list[i]) - 1):
                if minimum_list[i][j + 1] == 0:
                    return minimum_list[i][j]

        for i in range(len(minimum_list)):
            for j in range(len(minimum_list[i]) - 1):
                if minimum_list[i][j + 1] == 1:
                    return minimum_list[i][j]
