from tic_tac_toe.board import Board


def test_tic_tac_toe_initialized_with_a_3_x_3_board():
    new_board = Board()

    assert len(new_board.board) == 9


def test_tic_tac_toe_move():
    new_board = Board()

    new_board.move(selection=2)

    assert new_board.board[2] == "X"


def test_turn_count_keeps_track_of_number_of_turns():
    new_board = Board()

    new_board.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    assert new_board.turn_count() == 0

    new_board.board = ["X", " ", " ", " ", " ", " ", " ", " ", " "]

    assert new_board.turn_count() == 1

    new_board.board = ["X", "O", " ", " ", " ", " ", " ", " ", " "]

    assert new_board.turn_count() == 2


def test_current_player_returns_current_player_token():
    new_board = Board()

    new_board.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    assert new_board.current_player() == "X"

    new_board.board = ["X", " ", " ", " ", " ", " ", " ", " ", " "]

    assert new_board.current_player() == "O"

    new_board.board = ["X", "O", " ", " ", " ", " ", " ", " ", " "]

    assert new_board.current_player() == "X"


def test_position_taken_returns_true_if_square_is_already_occupied_and_false_if_not():
    new_board = Board()

    new_board.board = ["X", " ", " ", " ", " ", " ", " ", " ", " "]

    assert new_board.position_taken(0) == True
    assert new_board.position_taken(1) == False


def test_valid_move_returns_true_if_move_is_within_index_range_and_square_is_not_occupied():
    new_board = Board()

    new_board.board = ["X", " ", " ", " ", " ", " ", " ", " ", " "]

    assert new_board.valid_move(10) == False
    assert new_board.valid_move(0) == False
    assert new_board.valid_move(1) == True
