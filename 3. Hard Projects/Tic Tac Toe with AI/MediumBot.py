from EasyBot import EasyBot

class MediumBot(EasyBot):
    def __init__(self, board, symbol):
        super().__init__(board, symbol)
        if self.symbol == "X":
            self.opponent = "O"
        else:
            self.opponent = "X"

    def make_move(self):
        print("Making move level \"medium\"")
        self.movement()

    def movement(self):
        empty_coords = self.board.get_empty_coords()
        for coord in empty_coords: #if a winning move make it
            if self.board.winnable(self.symbol, coord):
                self.board.set_cell(coord[0], coord[1], self.symbol)
                return
        for coord in empty_coords: #if opponent has a winning move block it
            if self.board.winnable(self.opponent, coord):
                self.board.set_cell(coord[0], coord[1], self.symbol)
                return
        super().movement()