import pytest
from tic_tac_toe.tic_tac_toe import TicTacToe

def test_tic_tac_toe_board():
    ttt = TicTacToe()
    assert isinstance(ttt.board, list)  # board is a list
    assert (len(ttt.board)) == 9        # board length is 9