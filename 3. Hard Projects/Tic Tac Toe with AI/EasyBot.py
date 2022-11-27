from Bot import Bot
import random

class EasyBot(Bot):
    def __init__(self, board, player):
        super().__init__(board, player)

    def make_move(self):
        print("Making move level \"easy\"")
        self.movement()

    def movement(self):
        empty_coords = self.board.get_empty_coords()
        random_coord = random.choice(empty_coords)
        self.board.set_cell(random_coord[0], random_coord[1], self.player)