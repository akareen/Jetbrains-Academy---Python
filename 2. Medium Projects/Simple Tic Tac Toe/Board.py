class Board:
    def __init__(self):
        self.board = [[' ', ' ', ' '], 
                      [' ', ' ', ' '], 
                      [' ', ' ', ' ']]

    def set_board(self, item, row, col):
        self.board[row][col] = item

    def cell_is_occuiped(self, row, col):
        if (self.board[row][col] != ' '):
            return True
        return False

    def make_board(self, line):
        for i in range(3):
            for j in range(3):
                item = line[i * 3 + j]
                if (item != "_"):
                    self.board[i][j] = item
    
    def print_board(self):
        print("---------")
        for i in range(3):
            print("|", end=" ")
            for j in range(3):
                print(self.board[i][j], end=" ")
            print("|")
        print("---------")


    def row_checker(self, item):
        for i in range(3):
            for j in range(3):
                if (self.board[i][j] != item):
                    break
                if (j == 2):
                    return True
    


    def col_checker(self, item):
        for i in range(3):
            for j in range(3):
                if (self.board[j][i] != item):
                    break
                if (j == 2):
                    return True
    


    def diag_checker(self, item):
        for i in range(3):
            if (self.board[i][i] != item):
                break
            if (i == 2):
                return True
        for i in range(3):
            if (self.board[i][2 - i] != item):
                break
            if (i == 2):
                return True


    def check_winner(self, item):
        if (self.row_checker(item) or self.col_checker(item) or self.diag_checker(item)):
            return True
        return False


    def empty_cells(self):
        for i in range(3):
            for j in range(3):
                if (self.board[i][j] == ' '):
                    return True
        return False


    def too_large_difference(self):
        x_count = 0
        o_count = 0
        for i in range(3):
            for j in range(3):
                if (self.board[i][j] == 'X'):
                    x_count += 1
                elif (self.board[i][j] == 'O'):
                    o_count += 1
        if (abs(x_count - o_count) > 1):
            return True
        return False

    def is_impossible(self):
        if (self.too_large_difference()):
            return True
        if (self.check_winner('X') and self.check_winner('O')):
            return True
        return False
    