class Board:
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def __getitem__(self, index):
        return self.board[index]

    def move(self, selection, token="X"):
        if self.valid_move(selection - 1):
            self.board[selection - 1] = token
        else:
            print("Oops, that selection was invalid.")

    def turn_count(self):
        return self.board.count("X") + self.board.count("O")

    def position_taken(self, index):
        if self.board[index] == "X" or self.board[index] == "O":
            return True
        else:
            return False

    def valid_move(self, index):
        if index >= 0 and index <= 8 and self.position_taken(index) == False:
            return True
        else:
            return False
