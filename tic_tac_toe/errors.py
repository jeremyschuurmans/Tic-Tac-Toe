class Errors:
    def __init__(self, printer):
        self.printer = printer

    def input_not_numeric_error_message(self):
        self.message = (
            "\nI didn't understand that ... trying entering a number: 1 - 9:\n"
        )
        self.printer.print_item(self.message)

    def invalid_board_index_error_message(self):
        self.message = "\nSorry, friend ... that number isn't one of the squares. Please enter 1 - 9:\n"
        self.printer.print_item(self.message)

    def position_already_taken_error_message(self):
        self.message = "\nOops, that square already has a token on it, please choose another one:\n"
        self.printer.print_item(self.message)


class InputNotNumericError(Exception):
    pass


class InvalidBoardIndexError(Exception):
    pass


class PositionAlreadyTakenError(Exception):
    pass
