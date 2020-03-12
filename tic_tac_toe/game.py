from tic_tac_toe.board import Board
from tic_tac_toe.views import CommandLineBoardPresenter
from tic_tac_toe.user_messages import UserMessages
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
    user_messages = UserMessages(printer, board)
    user_selection = UserInput()
    errors = Errors(printer)

    user_messages.logo()

    user_messages.countdown()

    user_messages.display_instructions()

    view.display_board(board, printer)

    while not board.game_over():
        try:
            selection = user_selection.process_input()
            board.turn(selection)
        except InputNotNumericError:
            errors.input_not_numeric_error_message()
        except InvalidBoardIndexError:
            errors.invalid_board_index_error_message()
        except PositionAlreadyTakenError:
            errors.position_already_taken_error_message()
        finally:
            view.display_board(board, printer)
            if not board.win() and not board.tie():
                user_messages.whos_turn()

    if board.win():
        user_messages.who_won()

    if board.tie():
        user_messages.its_a_tie()
