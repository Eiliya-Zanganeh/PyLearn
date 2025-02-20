from tictactoe import *

board = initial_state()

while True:
    is_end = terminal(board)
    if is_end is False:
        show_board(board)
        row = int(input('Please Enter Row: ').strip())
        col = int(input('Please Enter Colume: ').strip())
        move = (row, col)
        try:
            board = result(board, (row, col))
        except Exception:
            print("mese adam vared kon :| ...")
            continue
        show_board(board)
        is_end = terminal(board)
        if is_end is False:
            print("computer ....")
            ai_move = minimax(board)
            board = result(board, ai_move)
            show_board(board)
        else:
            win = winner(board)
            if win is not None:
                print(f"winner {win} ...")
            else:
                print("equal")
            exit()
    else:
        win = winner(board)
        if win is not None:
            print(f"winner {win} ...")
        else:
            print("equal")
        exit()
