from tic_tac_toe.errors import Errors
from tests.printer_spy import PrinterSpy


def test_errors_can_print_invalid_input_error():
    spy = PrinterSpy()
    error = Errors(spy)

    error.invalid_input_error()

    expected = "Sorry, that input is invalid. Please enter numbers 1 - 9:\n"

    assert spy.printed() == expected


def test_errors_can_print_index_out_of_range_error():
    spy = PrinterSpy()
    error = Errors(spy)

    error.index_out_of_range_error()

    expected = "Sorry, that input is out of range. Please enter 1 - 9:\n"

    assert spy.printed() == expected


def test_errors_can_print_position_already_taken_error():
    spy = PrinterSpy()
    error = Errors(spy)

    error.position_already_taken_error()

    expected = "Sorry, that position has already been taken, please choose another:\n"

    assert spy.printed() == expected

