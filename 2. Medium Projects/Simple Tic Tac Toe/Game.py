from Board import Board

def take_turn_input():
    while True:
        try:
            row, col = input().split()
            row = int(row)
            col = int(col)
            if (row > 3 or row < 1 or col > 3 or col < 1):
                print("Coordinates should be from 1 to 3!")
                continue
            return row - 1, col - 1
        except ValueError:
            print("You should enter numbers!")


def check_winner(board):
    if (board.check_winner("X")):
        board.print_board()
        print("X wins")
    elif (board.check_winner("O")):
        board.print_board()
        print("O wins")
    elif (board.empty_cells() == False):
        board.print_board()
        print("Draw")
    else:
        return False
    return True


def execution():
    board = Board()
    player = "X"

    while True:
        board.print_board()
        user_input = take_turn_input()
        while (board.cell_is_occuiped(user_input[0], user_input[1])):
            print("This cell is occupied! Choose another one!")
            user_input = take_turn_input()
        board.set_board(player, user_input[0], user_input[1])
        if (check_winner(board)):
            break
        if (player == "X"):
            player = "O"
        else:
            player = "X"



if __name__ == '__main__':
    execution()