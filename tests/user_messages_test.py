from tic_tac_toe.user_messages import UserMessages
from tic_tac_toe.board import Board
from tests.printer_spy import PrinterSpy
import pytest

UserMessages.SLEEP_DURATION = 0


def test_user_interface_prints_logo_to_user():
    spy = PrinterSpy()
    user_message = UserMessages(spy)

    user_message.logo()

    expected = """
    ________________   _________   ______   __________  ______
   /_  __/  _/ ____/  /_  __/   | / ____/  /_  __/ __ \\/ ____/
    / /  / // /        / / / /| |/ /        / / / / / / __/   
   / / _/ // /___     / / / ___ / /___     / / / /_/ / /___   
  /_/ /___/\\____/    /_/ /_/  |_\\____/    /_/  \\____/_____/"""

    assert spy.printed() == expected


def test_user_interface_prints_example_horizontal_win():
    spy = PrinterSpy()
    user_message = UserMessages(spy)

    spy.print_item(user_message.instructions["horizontally"])

    expected = """\
        \neither horizontally\n
              X | X | X
            --------------
                |   |  
            --------------
                |   |  
        """

    assert spy.printed() == expected


def test_user_interface_prints_example_vertical_win():
    spy = PrinterSpy()
    user_message = UserMessages(spy)

    spy.print_item(user_message.instructions["vertically"])

    expected = """\
            \nvertically\n
                | X |  
            --------------
                | X |  
            --------------
                | X |  
        """

    assert spy.printed() == expected


def test_user_interface_prints_example_diagonal_win():
    spy = PrinterSpy()
    user_message = UserMessages(spy)

    user_message.display_instructions()

    expected = user_message.instructions.values()

    for actual, expected in zip(spy.printed_items, expected):
        assert actual == expected


def test_user_interface_congratulates_winner():
    spy = PrinterSpy()
    user_message = UserMessages(spy)
    board = Board()

    board.board = ["X", "O", " ", "X", "O", " ", "X", " ", " "]
    board.win()

    user_message.who_won(board)

    assert spy.printed_item == "X, you're the winner!"

