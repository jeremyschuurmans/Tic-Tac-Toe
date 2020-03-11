from tic_tac_toe.errors import InputNotNumericError


class UserInput:
    def process_input(self):

        user_entry = input()

        try:
            return int(user_entry) - 1
        except ValueError:
            raise InputNotNumericError()
