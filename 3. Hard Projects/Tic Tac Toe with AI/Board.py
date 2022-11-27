class Board:
    board_cells = [[" ", " ", " "], 
                   [" ", " ", " "],
                   [" ", " ", " "]]

    def set_cell(self, row, column, symbol):
        self.board_cells[row][column] = symbol

    def get_cell(self, row, column):
        return self.board_cells[row][column]

    def get_empty_coords(self):
        ls = []
        for i in range(3):
            for j in range(3):
                if self.board_cells[i][j] == " ":
                    coord = [i, j]
                    ls.append(coord)
        return ls

    def print_board(self):
        print("---------")
        for i in range(3):
            print("| " + self.board_cells[i][0] + " " + self.board_cells[i][1] +
                  " " + self.board_cells[i][2] + " |")
        print("---------")


    def is_occupied(self, row, column):
        return self.board_cells[row][column] != " "

    def is_extra_x(self):
        x_count = 0
        o_count = 0
        for i in range(3):
            for j in range(3):
                if self.board_cells[i][j] == "X":
                    x_count += 1
                elif self.board_cells[i][j] == "O":
                    o_count += 1
        return x_count > o_count


    def win_check(self, symbol):
        return self.win_row(symbol) or self.win_column(symbol) or self.win_diagonal(symbol)


    def winnable(self, symbol, coord):
        self.set_cell(coord[0], coord[1], symbol)
        win = self.win_check(symbol)
        self.set_cell(coord[0], coord[1], " ")
        return win


    def draw_check(self):
        for i in range(3):
            for j in range(3):
                if self.board_cells[i][j] == " ":
                    return False
        return True
    

    def win_row(self, symbol):
        for i in range(3):
            if self.board_cells[i][0] == symbol and self.board_cells[i][1] == symbol and self.board_cells[i][2] == symbol:
                return True
        return False


    def win_column(self, symbol):
        for i in range(3):
            if self.board_cells[0][i] == symbol and self.board_cells[1][i] == symbol and self.board_cells[2][i] == symbol:
                return True
        return False

    
    def win_diagonal(self, symbol):
        if self.board_cells[0][0] == symbol and self.board_cells[1][1] == symbol and self.board_cells[2][2] == symbol:
            return True
        if self.board_cells[0][2] == symbol and self.board_cells[1][1] == symbol and self.board_cells[2][0] == symbol:
            return True
        return False