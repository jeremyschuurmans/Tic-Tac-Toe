class Errors:
    def __init__(self, printer):
        self.printer = printer

    def invalid_input_error(self):
        self.message = "Sorry, that input is invalid. Please enter numbers 1 - 9:\n"
        self.printer.print_item(self.message)

    def index_out_of_range_error(self):
        self.message = "Sorry, that input is out of range. Please enter 1 - 9:\n"
        self.printer.print_item(self.message)

    def position_already_taken_error(self):
        self.message = (
            "Sorry, that position has already been taken, please choose another:\n"
        )
        self.printer.print_item(self.message)


class InputNotNumericError(Exception):
    pass


class InvalidBoardIndexError(Exception):
    pass


class PositionAlreadyTakenError(Exception):
    pass
