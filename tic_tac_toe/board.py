from tic_tac_toe.errors import InvalidBoardIndexError, PositionAlreadyTakenError


class Board:
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.winner = None

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

    def turn(self, selection, player):
        player = self.current_player(player)

        if not self.within_bounds(selection):
            raise InvalidBoardIndexError()

        if self.position_taken(selection):
            raise PositionAlreadyTakenError()

        self.move(selection, self.board, player)

    def move(self, selection, board, player):
        index = selection - 1
        board[index] = player

    def turn_count(self, player):
        return self.board.count(player.token[0]) + self.board.count(player.token[1])

    def current_player(self, player):
        return player.token[0] if self.turn_count(player) % 2 == 0 else player.token[1]

    def position_taken(self, index):
        return self.board[index] != " "

    def within_bounds(self, index):
        return index >= 0 and index <= 8

    def win(self):
        won = False
        for combination in self.win_combinations:
            if (
                self.board[combination[0]] != " "
                and self.board[combination[0]]
                == self.board[combination[1]]
                == self.board[combination[2]]
            ):
                won = True
                break
        self.winner = self.board[combination[0]]
        return won

    def tie(self):
        return self.board.count(" ") == 0 and not self.win()

    def game_over(self):
        return self.win() or self.tie()

