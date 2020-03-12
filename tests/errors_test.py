from tic_tac_toe.errors import Errors
from tests.printer_spy import PrinterSpy


def test_errors_can_print_input_not_numeric_error_message():
    spy = PrinterSpy()
    error = Errors(spy)

    error.input_not_numeric_error_message()

    expected = "\nI didn't understand that ... trying entering a number: 1 - 9:\n"

    assert spy.printed() == expected


def test_errors_can_print_invalid_board_index_error_message():
    spy = PrinterSpy()
    error = Errors(spy)

    error.invalid_board_index_error_message()

    expected = "\nSorry, friend ... that number isn't one of the squares. Please enter 1 - 9:\n"

    assert spy.printed() == expected


def test_errors_can_print_position_already_taken_error_message():
    spy = PrinterSpy()
    error = Errors(spy)

    error.position_already_taken_error_message()

    expected = (
        "\nOops, that square already has a token on it, please choose another one:\n"
    )

    assert spy.printed() == expected

