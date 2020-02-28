from tic_tac_toe.board import Board
from tic_tac_toe.views import BoardDisplay


def run():
    board = Board()
    view = BoardDisplay()
    view.display_board(board)
