class Board:
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def __getitem__(self, index):
        return self.board[index]

    def turn(self, view, selection):
        token = self.current_player()

        view.display_board(self, self.board)

        selected_space = selection.input_validator(self)

        if self.valid_move(selected_space):
            self.move(selected_space, token)
        else:
            print("Sorry, that's not a valid move.\n")
            self.turn(view, selection)

    def move(self, selection, token):
        self.board[selection] = token

    def turn_count(self):
        return self.board.count("X") + self.board.count("O")

    def current_player(self):
        return "X" if self.turn_count() % 2 == 0 else "O"

    def position_taken(self, index):
        return self.board[index] == "X" or self.board[index] == "O"

    def valid_move(self, index):
        return index >= 0 and index <= 8 and self.position_taken(index) == False
