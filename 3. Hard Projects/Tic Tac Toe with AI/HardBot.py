from MediumBot import MediumBot
from Bot import Bot
import math

class HardBot(MediumBot):
    def __init__(self, board, symbol):
        super().__init__(board, symbol)
        if self.symbol == "X":
            self.opponent = "O"
        else:
            self.opponent = "X"

    def make_move(self):
        print("Making move level \"hard\"")

        best_score = -math.inf
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board.get_cell(i, j) == " ":
                    self.board.set_cell(i, j, self.symbol)
                    score = self.minimax(self.board, 0, False)
                    self.board.set_cell(i, j, " ")
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        self.board.set_cell(best_move[0], best_move[1], self.symbol)

    def minimax(self, board, depth, is_maximizing):
        if board.win_check(self.symbol):
            return 1
        elif board.win_check(self.opponent):
            return -1
        elif board.draw_check():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for i in range(3):
                for j in range(3):
                    if board.get_cell(i, j) == " ":
                        board.set_cell(i, j, self.symbol)
                        score = self.minimax(board, depth + 1, False)
                        board.set_cell(i, j, " ")
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(3):
                for j in range(3):
                    if board.get_cell(i, j) == " ":
                        board.set_cell(i, j, self.opponent)
                        score = self.minimax(board, depth + 1, True)
                        board.set_cell(i, j, " ")
                        best_score = min(score, best_score)
            return best_score
