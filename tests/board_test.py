from tic_tac_toe.board import Board


def test_tic_tac_toe_initialized_with_a_3_x_3_board():
    new_board = Board()

    assert len(new_board.board) == 9


def test_tic_tac_toe_move():
    fresh_board = Board()

    fresh_board.move(selection=3)

    assert fresh_board.board[2] == "X"
