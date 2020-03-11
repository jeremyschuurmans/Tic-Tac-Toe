from tic_tac_toe.board import Board
from tic_tac_toe.views import CommandLineBoardPresenter
from tic_tac_toe.printer import Printer
from tic_tac_toe.user_input import UserInput
from tic_tac_toe.errors import (
    Errors,
    InvalidBoardIndexError,
    InputNotNumericError,
    PositionAlreadyTakenError,
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
            errors.input_not_numeric_error_message()
        except InvalidBoardIndexError:
            errors.invalid_board_index_error_message()
        except PositionAlreadyTakenError:
            errors.position_already_taken_error_message()
