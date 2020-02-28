from tic_tac_toe.board import Board
from tic_tac_toe.views import BoardDisplay


def test_tic_tac_toe_display_board(capfd):

    view = BoardDisplay()
    board = Board()
    view.display_board(board)

    mock_output = capfd.readouterr()
    expected = """\
    |   |  
--------------
    |   |  
--------------
    |   |  
"""
    assert mock_output.out == expected


# def test_tic_tac_toe_display_board_with_user_token(capfd):
#     board_with_plays = Board()

#     board_with_plays.board = ["X", " ", " ", " ", "X", " ", " ", " ", "X"]

#     board = BoardDisplay()

#     board.display_board(board_with_plays)

#     mock_output_with_plays = capfd.readouterr()
#     expected = """\
#   X |   |
# --------------
#     | X |
# --------------
#     |   | X
# """
#     assert mock_output_with_plays.out == expected
