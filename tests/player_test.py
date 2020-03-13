from tic_tac_toe.player import Player, Human, Computer
from tic_tac_toe.board import Board


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
