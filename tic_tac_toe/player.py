from tic_tac_toe.errors import InputNotNumericError
import random


class Player:
    def __init__(self, token):
        self.token = token

    def get_input(self):
        user_entry = input()

        try:
            return int(user_entry) - 1
        except ValueError:
            raise InputNotNumericError()

