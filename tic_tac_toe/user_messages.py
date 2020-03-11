import time


class UserMessages:
    def __init__(self, printer, board):
        self.printer = printer
        self.board = board

    def logo(self):
        logo = """
    ________________   _________   ______   __________  ______
   /_  __/  _/ ____/  /_  __/   | / ____/  /_  __/ __ \\/ ____/
    / /  / // /        / / / /| |/ /        / / / / / / __/   
   / / _/ // /___     / / / ___ / /___     / / / /_/ / /___   
  /_/ /___/\\____/    /_/ /_/  |_\\____/    /_/  \\____/_____/"""

        self.printer.print_item(logo)

    def countdown(self):
        seconds = 3

        starter_message = "\nStarting in:"

        self.printer.print_item(starter_message)

        while seconds:
            countdown = f"\n{seconds}"
            self.printer.print_item(countdown)
            time.sleep(1)
            seconds -= 1

    def instructions(self):
        intro = "\nHere are your instructions:"

        self.printer.print_item(intro)

        time.sleep(3)

        player_tokens = "\nPlayer 1 will be X, and Player 2 will be O."

        self.printer.print_item(player_tokens)

        time.sleep(3)

        game_play = "\nPlayers will take turns placing tokens on the board."

        self.printer.print_item(game_play)

        time.sleep(3)

        objective = "\nYour objective is to place three tokens in a row"

        self.printer.print_item(objective)
        time.sleep(2)

        horizontally = "\neither horizontally\n"

        self.printer.print_item(horizontally)
        self.example_horizontal_win()

        time.sleep(3)

        vertically = "\nvertically\n"

        self.printer.print_item(vertically)
        self.example_vertical_win()
        time.sleep(3)

        diagonally = "\nor diagonally\n"

        self.printer.print_item(diagonally)
        self.example_diagonal_win()
        time.sleep(3)

        winner = "\nThe first player to get three in a row wins.\n"

        self.printer.print_item(winner)
        time.sleep(4)

        first_move = "\nPlayer 1, the first move is yours. Please choose 1 - 9:\n"

        self.printer.print_item(first_move)

    def example_horizontal_win(self):
        win = """\
              X | X | X
            --------------
                |   |  
            --------------
                |   |  
        """

        self.printer.print_item(win)

    def example_vertical_win(self):
        win = """\
                | X |  
            --------------
                | X |  
            --------------
                | X |  
        """

        self.printer.print_item(win)

    def example_diagonal_win(self):
        win = """\
                |   | X
            --------------
                | X |  
            --------------
              X |   |  
        """

        self.printer.print_item(win)

    def whos_turn(self):
        turn = f"{self.board.current_player()}'s turn"

        self.printer.print_item(turn)

    def who_won(self):
        winner = f"{self.board.winner} wins!"

        self.printer.print_item(winner)

    def its_a_tie(self):
        tie_game = "Tie game!"

        self.printer.print_item(tie_game)

