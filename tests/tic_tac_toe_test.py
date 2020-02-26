import pytest
from tic_tac_toe.tic_tac_toe import TicTacToe

def test_tic_tac_toe_board():
    ttt = TicTacToe()
    
    assert isinstance(ttt.board, list)  # board is a list
    assert (len(ttt.board)) == 9        # board length is 9
    assert ttt.board[0] == " "          # board contains empty strings

def test_tic_tac_toe_display_board(capfd):
    ttt = TicTacToe()

    ttt.display_board(ttt.board)

    mock_output = capfd.readouterr()
    assert mock_output.out == '    |   |  \n' '--------------\n''    |   |  \n' '--------------\n' '    |   |  \n'
        # this confusing-looking output of strings looks like this in the console:
        #
        #      |   |     
        # ---------------
        #      |   |     
        # ---------------
        #      |   |     