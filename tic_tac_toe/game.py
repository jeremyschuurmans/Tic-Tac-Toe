from tic_tac_toe.board import Board
from tic_tac_toe.views import CommandLineBoardPresenter
from tic_tac_toe.user_input import UserInput


def run():
    board = Board()
    view = CommandLineBoardPresenter()
    user_selection = UserInput()

    while True:
        view.display_board(board)
        try:
            selection = user_selection.process_input()
            board.turn(selection)
        except ValueError:
            print("Sorry, that input is invalid. Please enter numbers 1 - 9:\n")
        except IndexError:
            print("Sorry, that input is out of range. Please enter 1 - 9:\n")
        except KeyError:
            print(
                "Sorry, that position has already been taken, please choose another:\n"
            )

