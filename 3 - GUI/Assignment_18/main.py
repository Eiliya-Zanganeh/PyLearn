from functools import partial

from PySide6.QtWidgets import QWidget, QMessageBox

from tictactoe import *

window.show()

AI = True


def button_clicked(button):
    if button.text() == "":
        if player(convert_buttons_to_board(buttons)) == "X":
            button.setStyleSheet("background-color: #27496D; border-radius: 10px;color: #00A8CC;")
            button.setText(X)
        elif player(convert_buttons_to_board(buttons)) == "O":
            button.setStyleSheet("background-color: #27496D; border-radius: 10px;color: rgb(255, 255, 0);")
            button.setText(O)
        if terminal(convert_buttons_to_board(buttons)):
            game_over(buttons)
        else:
            if AI:
                move = minimax(convert_buttons_to_board(buttons))
                buttons[move[0]][move[1]].setStyleSheet(
                    "background-color: #27496D; border-radius: 10px;color: rgb(255, 255, 0);")
                buttons[move[0]][move[1]].setText(O)
                if terminal(convert_buttons_to_board(buttons)):
                    game_over(buttons)


def game_over(buttons):
    widget = QWidget()
    widget.resize(250, 150)
    win = winner(convert_buttons_to_board(buttons))
    if win is None:
        msg = "Equal 😐"
        window.score_equal.setText(
            str(
                int((window.score_equal.text())) + 1
            )
        )
    else:
        msg = f"Player {win} Win 😐"
        if win == "X":
            window.score_X.setText(
                str(
                    int((window.score_X.text())) + 1
                )
            )
        elif win == "O":
            window.score_O.setText(
                str(
                    int((window.score_O.text())) + 1
                )
            )
    QMessageBox.information(widget, 'Game Over', msg)
    widget.show()
    new_game()


def new_game():
    for row in buttons:
        for button in row:
            button.setText("")


def change_player_2(is_ai):
    global AI
    if AI != is_ai:
        AI = is_ai
        window.score_equal.setText("0")
        window.score_X.setText("0")
        window.score_O.setText("0")
        new_game()


for row in buttons:
    for button in row:
        button.clicked.connect(partial(button_clicked, button))

window.new_game.clicked.connect(new_game)
window.ai.clicked.connect(partial(change_player_2, True))
window.player_2.clicked.connect(partial(change_player_2, False))

app.exec()
