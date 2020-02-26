class TicTacToe:
    def __init__(self):
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display_board(self, board):
        print(f'  {self.board[0]} | {self.board[1]} | {self.board[2]}')
        print('--------------')
        print(f'  {self.board[3]} | {self.board[4]} | {self.board[5]}')
        print('--------------')
        print(f'  {self.board[6]} | {self.board[7]} | {self.board[8]}')

        # print(f'Hello {name}! This is {program}')
