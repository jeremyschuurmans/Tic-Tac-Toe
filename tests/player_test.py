from tic_tac_toe.player import Player, Human, Computer
from tic_tac_toe.board import Board
import pytest


def test_player_initializes_with_a_player_token():
    player = Player(token="X")

    assert player.token == "X"


def test_human_player_can_make_a_move():
    new_board = Board()
    player = Human(token="X")

    player.move(2, new_board.board)

    assert new_board.board[2] == "X"


def test_computer_player_can_make_a_move():
    new_board = Board()
    # new_board.board = ["X", "O", " ", "X", "O", " ", "X", " ", " "]
    computer = Computer(token="X")

    computer.move(None, new_board.board)

    assert new_board.board.index("X") != None


@pytest.mark.parametrize(
    "board_state,open_space_count",
    [
        (["X", "O", " ", "O", "X", "O", "X", " ", "X"], 2),
        (["X", "O", " ", "X", "O", " ", " ", " ", " "], 5),
    ],
)
def test_computer_player_only_places_token_on_free_spaces(
    board_state, open_space_count
):
    new_board = Board()
    new_board.board = board_state

    computer = Computer(token="X")

    computer.move(None, new_board.board)

    assert new_board.board.count(" ") == open_space_count - 1
