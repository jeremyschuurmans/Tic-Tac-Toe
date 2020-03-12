class Player:
    def __init__(self, token):
        self.token = token


class Human(Player):
    def move(self, selection, board):
        board[selection] = self.token

