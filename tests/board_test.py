from tic_tac_toe.board import Board


def test_tic_tac_toe_initialized_with_a_3_x_3_board():
    new_board = Board()

    assert len(new_board.board) == 9


def test_tic_tac_toe_move():
    new_board = Board()

    new_board.move(selection=3)

    assert new_board.board[2] == "X"


def test_player_cannot_place_token_on_square_already_occupied():
    new_board = Board()

    new_board.move(selection=5)

    assert new_board.board[4] == "X"

    new_board.move(selection=5, token="O")

    assert new_board.board[4] == "X"


def test_turn_count_keeps_track_of_number_of_turns():
    new_board = Board()

    new_board.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    assert new_board.turn_count() == 0

    new_board.board = ["X", " ", " ", " ", " ", " ", " ", " ", " "]

    assert new_board.turn_count() == 1

    new_board.board = ["X", "O", " ", " ", " ", " ", " ", " ", " "]

    assert new_board.turn_count() == 2


def current_player_returns_current_player_token():
    new_board = Board()

    new_board.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    assert new_board.current_player == "X"

    new_board.board = ["X", " ", " ", " ", " ", " ", " ", " ", " "]

    assert new_board.current_player == "O"

    new_board.board = ["X", "O", " ", " ", " ", " ", " ", " ", " "]

    assert new_board.current_player == "X"

