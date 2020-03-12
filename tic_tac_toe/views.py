class CommandLineBoardPresenter:
    def display_board(self, board, printer):
        formatted_board = f"""\
              {board[0]} | {board[1]} | {board[2]}
            --------------
              {board[3]} | {board[4]} | {board[5]}
            --------------
              {board[6]} | {board[7]} | {board[8]}
        """

        printer.print_item(formatted_board)
