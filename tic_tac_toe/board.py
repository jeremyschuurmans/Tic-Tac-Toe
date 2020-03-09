class Board:
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def __getitem__(self, index):
        return self.board[index]

    def turn(self, selection):
        token = self.current_player()

        if self.within_bounds(selection):
            if self.position_taken(selection) == False:
                self.move(selection, token)
            else:
                raise KeyError
        else:
            raise IndexError

    def move(self, selection, token):
        self.board[selection] = token

    def turn_count(self):
        return self.board.count("X") + self.board.count("O")

    def current_player(self):
        return "X" if self.turn_count() % 2 == 0 else "O"

    def position_taken(self, index):
        return self.board[index] == "X" or self.board[index] == "O"

    def within_bounds(self, index):
        return index >= 0 and index <= 8

