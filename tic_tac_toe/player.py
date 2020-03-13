from tic_tac_toe.errors import InputNotNumericError


class Player:
    def __init__(self, token):
        self.token = token


class Human(Player):
    def __init__(self, token):
        super().__init__(token)

    def get_input(self):
        user_entry = input()

        try:
            return int(user_entry) - 1
        except ValueError:
            raise InputNotNumericError()

    def move(self, selection, board):
        board[selection] = self.token

