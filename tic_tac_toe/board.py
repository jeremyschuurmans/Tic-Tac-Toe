class Board:
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def __getitem__(self, index):
        return self.board[index]

    def move(self, selection, token="X"):
        self.board[selection - 1] = token
