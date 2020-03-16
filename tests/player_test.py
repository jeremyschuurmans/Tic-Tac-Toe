from tic_tac_toe.player import Player
from tic_tac_toe.board import Board
import pytest


def test_player_initializes_with_a_player_token():
    player = Player(token="X")

    assert player.token == "X"


def test_human_player_can_make_a_move():
    new_board = Board()
    player = Player(token=["X", "O"])

    new_board.move(2, new_board.board, player.token[0])

    assert new_board.board[1] == "X"
