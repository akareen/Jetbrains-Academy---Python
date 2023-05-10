import numpy as np
from game_piece import GamePiece


def main():
    letter_input = input()
    piece = GamePiece(letter_input)
    print()
    print_array(positions([]))
    for i in range(5):
        print_array(positions(piece.get_current_position()))
        piece.rotate()


def positions(position_array):
    blank_array = np.zeros(shape=(20, 10))
    if len(position_array) == 0:
        return blank_array
    if len(position_array) != 4:
        raise ValueError("Invalid position array")
    for i in range(4):
        element = position_array[i]
        #put the 1d position array into the 2d array
        blank_array[element // 10][element % 10] = 1
    return blank_array


def print_array(array):
    for i in range(20):
        for j in range(10):
            element = array[i][j]
            if j > 0:
                print(" ", end="")
            if element == 0:
                print("-", end="")
            else:
                print(0, end="")
        print()
    print()


if __name__ == "__main__":
    main()
