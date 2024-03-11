from copy import deepcopy
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

app = QApplication([])
loader = QUiLoader()
window = loader.load("main.ui")
window.setFixedSize(250, 318)

X = "X"
O = "O"
EMPTY = None

buttons = [
    [window.btn_1, window.btn_2, window.btn_3],
    [window.btn_4, window.btn_5, window.btn_6],
    [window.btn_7, window.btn_8, window.btn_9]
]


def convert_buttons_to_board(buttons):
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    for i in range(3):
        for j in range(3):
            board[i][j] = buttons[i][j].text() or None
    return board


def player(board):
    Xcount = 0
    Ocount = 0

    for row in board:
        Xcount += row.count(X)
        Ocount += row.count(O)

    if Xcount <= Ocount:
        return X
    else:
        return O


def actions(board):
    possible_moves = set()

    for row_index, row in enumerate(board):
        for column_index, item in enumerate(row):
            if item == None:
                possible_moves.add((row_index, column_index))

    return possible_moves


def result(board, action):
    player_move = player(board)

    new_board = deepcopy(board)
    i, j = action

    if board[i][j] != None:
        raise Exception
    else:
        new_board[i][j] = player_move

    return new_board


def winner(board):
    for player in (X, O):

        for row in board:
            if row == [player] * 3:
                return player

        for i in range(3):
            column = [board[x][i] for x in range(3)]
            if column == [player] * 3:
                return player

        if [board[i][i] for i in range(0, 3)] == [player] * 3:
            return player

        elif [board[i][~i] for i in range(0, 3)] == [player] * 3:
            return player
    return None


def terminal(board):
    if winner(board) != None:
        return True

    for row in board:
        if EMPTY in row:
            return False

    return True


def utility(board):
    win_player = winner(board)

    if win_player == X:
        return 1
    elif win_player == O:
        return -1
    else:
        return 0


def minimax(board):
    def max_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = -5
            for action in actions(board):
                minval = min_value(result(board, action))[0]
                if minval > v:
                    v = minval
                    optimal_move = action
            return v, optimal_move

    def min_value(board):
        optimal_move = ()
        if terminal(board):
            return utility(board), optimal_move
        else:
            v = 5
            for action in actions(board):
                maxval = max_value(result(board, action))[0]
                if maxval < v:
                    v = maxval
                    optimal_move = action
            return v, optimal_move

    curr_player = player(board)

    if terminal(board):
        return None

    if curr_player == X:
        return max_value(board)[1]

    else:
        return min_value(board)[1]
