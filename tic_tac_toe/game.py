from tic_tac_toe.board import Board
from tic_tac_toe.views import BoardDisplay


def run():
    board = Board()
    view = BoardDisplay()
    view.display_board(board)
    turn_count = 0
    while True:
        print("Please select an open square by entering 1-9.")
        if turn_count % 2 == 0:
            board.move(selection=int(input()), token="X")
            turn_count += 1
            view.display_board(board)
            print(f"Turn: {turn_count}")
        else:
            board.move(selection=int(input()), token="0")
            turn_count += 1
            view.display_board(board)
            print(f"Turn: {turn_count}")

