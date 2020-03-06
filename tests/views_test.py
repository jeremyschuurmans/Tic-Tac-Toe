from tic_tac_toe.board import Board
from tic_tac_toe.views import CommandLineBoardPresenter


def test_tic_tac_toe_display_board(capfd):
    new_board = Board()
    view = CommandLineBoardPresenter()

    view.display_board(new_board)

    mock_output = capfd.readouterr()

    expected = """\
    |   |  
--------------
    |   |  
--------------
    |   |  
"""
    assert mock_output.out == expected


def test_tic_tac_toe_display_board_with_user_token(capfd):

    new_board = Board()
    new_board.board = ["X", " ", " ", " ", "X", " ", " ", " ", "X"]
    view = CommandLineBoardPresenter()

    view.display_board(new_board)

    mock_output_with_plays = capfd.readouterr()

    expected = """\
  X |   |  
--------------
    | X |  
--------------
    |   | X
"""
    assert mock_output_with_plays.out == expected
