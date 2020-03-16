from tic_tac_toe.errors import InputNotNumericError
import random


class Player:
    def __init__(self, token):
        self.token = token


class Human(Player):
    def __init__(self, token):
        super().__init__(token)

    def get_input(self):
        user_entry = input()

        try:
            return int(user_entry)
        except ValueError:
            raise InputNotNumericError()

    def move(self, selection, board):
        index = selection - 1
        board[index] = self.token


class Computer(Player):
    def __init__(self, token):
        super().__init__(token)

    def get_available_space(self, selection, board):
        available_spaces = [index for index, space in enumerate(board) if space == " "]

        selection = random.choice(available_spaces)

        return selection

    def move(self, selection, board):
        board[selection] = self.token

