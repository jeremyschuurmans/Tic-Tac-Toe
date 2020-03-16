from tic_tac_toe.board import Board
from tic_tac_toe.player import Player
from tic_tac_toe.errors import InvalidBoardIndexError, PositionAlreadyTakenError
import pytest


def test_tic_tac_toe_initialized_with_a_3_x_3_board():
    new_board = Board()

    assert len(new_board.board) == 9


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

    player = Player(token=["X", "O"])

    assert new_board.turn_count(player) == turn_count


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

    player = Player(token=["X", "O"])

    assert new_board.current_player(player) == current_player


def test_position_taken_returns_true_if_square_is_already_occupied_and_false_if_not():
    new_board = Board()

    new_board.board = ["X", " ", " ", " ", " ", " ", " ", " ", " "]

    assert new_board.position_taken(0)
    assert not new_board.position_taken(1)


def test_within_bounds_returns_true_if_move_is_within_index_range():
    new_board = Board()

    new_board.board = ["X", " ", " ", " ", " ", " ", " ", " ", " "]

    assert not new_board.within_bounds(10)
    assert new_board.within_bounds(1)


@pytest.mark.parametrize(
    "board_state,win_status",
    [
        ([" ", " ", " ", " ", " ", " ", " ", " ", " "], False),
        (["X", "O", " ", " ", " ", " ", " ", " ", " "], False),
        (["X", "O", "X", "O", "X", "O", "X", " ", "X"], True),
        (["X", "O", " ", "X", "O", " ", "X", " ", " "], True),
    ],
)
def test_win_can_detect_a_winning_combination_present_on_the_game_board(
    board_state, win_status
):
    new_board = Board()

    new_board.board = board_state

    assert new_board.win() == win_status


@pytest.mark.parametrize(
    "board_state,winner_token",
    [
        (["X", "O", "X", "O", "X", "O", "X", " ", "X"], "X"),
        (["X", "O", " ", "X", "O", " ", "X", " ", " "], "X"),
    ],
)
def test_win_saves_the_winner(board_state, winner_token):
    new_board = Board()

    new_board.board = board_state

    assert new_board.win()
    assert new_board.winner == winner_token


def test_tie_can_detect_a_full_board_with_no_winners():
    new_board = Board()

    new_board.board = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]

    assert new_board.tie()


@pytest.mark.parametrize(
    "board_state,game_over_status",
    [
        ([" ", " ", " ", " ", " ", " ", " ", " ", " "], False),
        (["X", "O", " ", " ", " ", " ", " ", " ", " "], False),
        (["X", "O", "X", "O", "X", "O", "X", " ", "X"], True),
    ],
)
def test_game_over_returns_true_when_a_game_is_won(board_state, game_over_status):
    new_board = Board()

    new_board.board = board_state

    assert new_board.game_over() == game_over_status


def test_board_raises_error_if_index_not_on_board():
    new_board = Board()
    player = Player(token=["X", "O"])

    with pytest.raises(InvalidBoardIndexError):
        new_board.turn(9, player)


def test_board_raises_error_when_positions_are_taken():
    new_board = Board()
    player = Player(token=["X", "O"])

    new_board.board = ["X"]

    with pytest.raises(PositionAlreadyTakenError):
        new_board.turn(0, player)
