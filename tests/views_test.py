from tic_tac_toe.board import Board
from tic_tac_toe.views import CommandLineBoardPresenter
from tests.printer_spy import PrinterSpy


def test_tic_tac_toe_display_board():
    new_board = Board()
    view = CommandLineBoardPresenter()
    spy = PrinterSpy()

    view.display_board(new_board, spy, current_player="X")

    expected = """\
                |   |  
            --------------
                |   |  
            --------------
                |   |  
        """
    assert spy.printed() == expected


def test_tic_tac_toe_display_board_with_user_token():

    new_board = Board()
    view = CommandLineBoardPresenter()
    spy = PrinterSpy()

    new_board.board = ["X", " ", " ", " ", "X", " ", " ", " ", "X"]

    view.display_board(new_board, spy, current_player=None)

    expected = """\
              X |   |  
            --------------
                | X |  
            --------------
                |   | X
        """
    assert spy.printed() == expected
