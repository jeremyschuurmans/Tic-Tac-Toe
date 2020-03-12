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

    instructions = {
        "great": "\nOkay great!",
        "intro": "\nHere's how to play:",
        "player tokens": "\nPlayer 1 will be X, and Player 2 will be O.",
        "game play": "\nPlayers will take turns placing tokens on the board.",
        "selection": """\
        \nTo place your token on a square, type that square's number:\n
              1 | 2 | 3
            --------------
              4 | 5 | 6 
            --------------
              7 | 8 | 9 
        """,
        "show": "\nI'll show you really quick.\n",
        "demo board": """\
                |   |  
            --------------
                |   |  
            --------------
                |   |  
        """,
        "demo": "\nLet's say I'm Player 1, and I choose",
        "square": "\n5",
        "play": """\
                |   |  
            --------------
                | X |  
            --------------
                |   |  
        """,
        "completed move": "\nMy token gets put on square 5.",
        "easy right?": "\nEasy, right?",
        "objective": "\nYour objective is to place three tokens in a row",
        "horizontally": """\
        \neither horizontally\n
              X | X | X
            --------------
                |   |  
            --------------
                |   |  
        """,
        "vertically": """\
            \nvertically\n
                | X |  
            --------------
                | X |  
            --------------
                | X |  
        """,
        "diagonally": """\
            \nor diagonally\n
                |   | X
            --------------
                | X |  
            --------------
              X |   |  
        """,
        "winner": "\nThe first player to get three in a row wins.",
        "first move": "\nPlayer 1, the first move is yours. Please choose 1 - 9:\n",
    }

    def instructions_option(self):
        option = "\nBefore we get started, should I tell you how to play the game? Type 1 for 'yes', and 2 for 'no'."

        self.printer.print_item(option)

    def display_instructions(self):
        for instruction in self.instructions.values():
            self.printer.print_item(instruction)
            time.sleep(2.5)

    def whos_turn(self):
        turn = f"It's {self.board.current_player()}'s turn"

        self.printer.print_item(turn)

    def who_won(self):
        winner = f"{self.board.winner}, you're the winner!"

        self.printer.print_item(winner)

    def its_a_tie(self):
        tie_game = "Looks like it's a tie! You're both winners in my book!"

        self.printer.print_item(tie_game)

