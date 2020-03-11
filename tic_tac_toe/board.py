from tic_tac_toe.errors import InvalidBoardIndexError, PositionAlreadyTakenError


class Board:
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    win_combinations = (
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    )

    def __getitem__(self, index):
        return self.board[index]

    def turn(self, selection):
        token = self.current_player()

        if not self.within_bounds(selection):
            raise InvalidBoardIndexError()

        if self.position_taken(selection):
            raise PositionAlreadyTakenError()

        self.move(selection, token)

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

    def win(self):
        won = False
        for combination in self.win_combinations:
            if (
                self.board[combination[0]]
                == self.board[combination[1]]
                == self.board[combination[2]]
            ):
                won = True
        return won

