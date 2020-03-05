from tic_tac_toe.views import BoardDisplay


class Board:
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def __getitem__(self, index):
        return self.board[index]

    def turn(self):
        view = BoardDisplay()
        token = self.current_player()

        print("Please enter 1-9.")

        view.display_board(self.board)

        selected_space = int(input()) - 1

        if self.valid_move(selected_space):
            self.move(selected_space, token)
        else:
            self.turn()

    def move(self, selection, token):
        self.board[selection] = token

    def turn_count(self):
        return self.board.count("X") + self.board.count("O")

    def current_player(self):
        if self.turn_count() % 2 == 0:
            return "X"
        else:
            return "O"

    def position_taken(self, index):
        return self.board[index] == "X" or self.board[index] == "O"

    def valid_move(self, index):
        return index >= 0 and index <= 8 and self.position_taken(index) == False
