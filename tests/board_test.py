from tic_tac_toe.board import Board
import pytest


def test_tic_tac_toe_initialized_with_a_3_x_3_board():
    new_board = Board()

    assert len(new_board.board) == 9


def test_tic_tac_toe_move():
    new_board = Board()

    new_board.move(selection=2, token="X")

    assert new_board.board[2] == "X"


@pytest.mark.parametrize(
    "board_state,turn_count",
    [
        ([" ", " ", " ", " ", " ", " ", " ", " ", " "], 0),
        (["X", " ", " ", " ", " ", " ", " ", " ", " "], 1),
        (["X", "O", " ", " ", " ", " ", " ", " ", " "], 2),
    ],
)
def test_turn_count_keeps_track_of_number_of_turns(board_state, turn_count):
    new_board = Board()

    new_board.board = board_state

    assert new_board.turn_count() == turn_count


@pytest.mark.parametrize(
    "board_state,current_player",
    [
        ([" ", " ", " ", " ", " ", " ", " ", " ", " "], "X"),
        (["X", " ", " ", " ", " ", " ", " ", " ", " "], "O"),
        (["X", "O", " ", " ", " ", " ", " ", " ", " "], "X"),
    ],
)
def test_current_player_returns_current_player_token(board_state, current_player):
    new_board = Board()

    new_board.board = board_state

    assert new_board.current_player() == current_player


def test_position_taken_returns_true_if_square_is_already_occupied_and_false_if_not():
    new_board = Board()

    new_board.board = ["X", " ", " ", " ", " ", " ", " ", " ", " "]

    assert new_board.position_taken(0)
    assert not new_board.position_taken(1)


def test_valid_move_returns_true_if_move_is_within_index_range_and_square_is_not_occupied():
    new_board = Board()

    new_board.board = ["X", " ", " ", " ", " ", " ", " ", " ", " "]

    assert not new_board.valid_move(10)
    assert not new_board.valid_move(0)
    assert new_board.valid_move(1)
