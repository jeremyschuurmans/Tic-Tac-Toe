import pytest
from tic_tac_toe.tic_tac_toe import TicTacToe


def test_tic_tac_toe_initialized_with_a_3_x_3_board():
    ttt = TicTacToe(board=[" ", " ", " ", " ", " ", " ", " ", " ", " "])

    assert len(ttt.board) == 9


def test_tic_tac_toe_display_board(capfd):
    ttt = TicTacToe(board=[" ", " ", " ", " ", " ", " ", " ", " ", " "])

    ttt.display_board()

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
    ttt = TicTacToe(board=[" ", " ", " ", " ", " ", " ", " ", " ", " "])

    ttt.board = ["X", " ", " ", " ", "X", " ", " ", " ", "X"]

    ttt.display_board()

    mock_output_with_plays = capfd.readouterr()
    expected = """\
  X |   |  
--------------
    | X |  
--------------
    |   | X
"""
    assert mock_output_with_plays.out == expected


def test_tic_tac_toe_move():
    ttt = TicTacToe(board=[" ", " ", " ", " ", " ", " ", " ", " ", " "])

    ttt.move(selection=3)

    assert ttt.board[2] == "X"
