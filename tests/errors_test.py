from tic_tac_toe.errors import Errors
from tests.printer_spy import PrinterSpy


def test_errors_can_print_input_not_numeric_error_message():
    spy = PrinterSpy()
    error = Errors(spy)

    error.input_not_numeric_error_message()

    expected = "Sorry, that input is invalid. Please enter numbers 1 - 9:\n"

    assert spy.printed() == expected


def test_errors_can_print_invalid_board_index_error_message():
    spy = PrinterSpy()
    error = Errors(spy)

    error.invalid_board_index_error_message()

    expected = "Sorry, that input is out of range. Please enter 1 - 9:\n"

    assert spy.printed() == expected


def test_errors_can_print_position_already_taken_error_message():
    spy = PrinterSpy()
    error = Errors(spy)

    error.position_already_taken_error_message()

    expected = "Sorry, that position has already been taken, please choose another:\n"

    assert spy.printed() == expected

