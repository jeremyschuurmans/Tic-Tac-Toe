from tic_tac_toe.board import Board
from tic_tac_toe.views import CommandLineBoardPresenter
from tic_tac_toe.printer import Printer
from tic_tac_toe.user_input import UserInput
from tic_tac_toe.errors import (
    Errors,
    InvalidBoardIndexError,
    InputNotNumericError,
    PositionAlreadyTaken,
)


def run():
    board = Board()
    view = CommandLineBoardPresenter()
    printer = Printer()
    user_selection = UserInput()
    errors = Errors(printer)

    while True:
        view.display_board(board, printer)
        try:
            selection = user_selection.process_input()
            board.turn(selection)
        except InputNotNumericError:
            errors.invalid_input_error()
        except InvalidBoardIndexError:
            errors.index_out_of_range_error()
        except PositionAlreadyTaken:
            errors.position_already_taken_error()
