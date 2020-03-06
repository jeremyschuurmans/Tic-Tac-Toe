from tic_tac_toe.board import Board
from tic_tac_toe.views import CommandLineBoardPresenter
from tic_tac_toe.user_input import UserInput


def run():
    board = Board()
    view = CommandLineBoardPresenter
    user_selection = UserInput

    while True:
        board.turn(view, user_selection)

