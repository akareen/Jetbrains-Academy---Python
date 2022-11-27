import random

class User:
    def __init__(self, board, symbol):
        self.board = board
        self.symbol = symbol


    def make_move(self):
        while True:
            try:
                coordinates = input("Enter the coordinates: ").split()
                if len(coordinates) != 2:
                    raise ValueError
                row = int(coordinates[0])
                column = int(coordinates[1])
                if row < 1 or row > 3 or column < 1 or column > 3:
                    print("Coordinates should be from 1 to 3!")
                if self.board.is_occupied(row - 1, column - 1):
                    print("This cell is occupied! Choose another one!")
                else:
                    self.board.set_cell(row - 1, column - 1, self.symbol)
                    break
            except ValueError:
                print("You should enter numbers!")