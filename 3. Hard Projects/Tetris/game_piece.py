#this if for a 10x20 game grid

class GamePiece:
    tile_roots = {"I": (0, 0), "O": (1, 1), "S": (1, 0), "Z": (-1, -1), "L": (0, 0), "J": (0, 1), "T": (0, 0)}
    
    tiles = {"O": [[4, 14, 15, 5]], 
             "I": [[4, 14, 24, 34], [3, 4, 5, 6]],
             "S": [[5, 4, 14, 13], [4, 14, 15, 25]], 
             "Z": [[4, 5, 15, 16], [5, 15, 14, 24]], 
             "L": [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]], 
             "J": [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]], 
             "T": [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]}
    valid_tiles = ["O", "I", "S", "Z", "L", "J", "T"]


    def __init__(self, tile_name, board_y, board_x):
        self.positions = []
        self.size = 0
        self.index = 0
        self.create_piece(tile_name, board_y, board_x)

    
    def get_root_tuple(self, tile_name, board_y, board_x):
        if tile_name not in GamePiece.valid_tiles:
            raise ValueError("Invalid tile name")
        return GamePiece.tiles[tile_name][0][0] + (board_y * 10) + board_x


    def create_piece(self, tile_name, board_y, board_x):
        if tile_name not in GamePiece.valid_tiles:
            raise ValueError("Invalid tile name")        
        self.positions = self.modify_positions(GamePiece.tiles[tile_name], board_y - 20, board_x - 10)
        self.size = len(self.positions)
        self.index = 0


    def modify_positions(self, positions, board_y, board_x):
        for i in range(len(positions)):
            positions[i] += (board_y * 10) + board_x
        return positions


    def get_current_position(self):
        return self.positions[self.index]


    def rotate(self):
        self.index += 1
        if self.index == self.size:
            self.index = 0
    

    def move_position(self, movecode):
        if movecode == "left":
            self.move_left()
        elif movecode == "right":
            self.move_right()
        elif movecode == "down":
            self.move_down()
        else:
            raise ValueError("Invalid move code")


    def move_left(self):
        for i in range(len(self.positions)):
            for j in range(len(self.positions[i])):
                #move to other side if it goes off the board
                if self.positions[i][j] % 10 == 0:
                    self.positions[i][j] += 9
                else:
                    self.positions[i][j] -= 1
    
    
    def move_right(self):
        for i in range(len(self.positions)):
            for j in range(len(self.positions[i])):
                #move to other side if it goes off the board
                if self.positions[i][j] % 10 == 9:
                    self.positions[i][j] -= 9
                else:
                    self.positions[i][j] += 1


    def move_down(self):
        for i in range(len(self.positions)):
            for j in range(len(self.positions[i])):
                #return to top if it goes off the board
                if self.positions[i][j] >= 190:
                    self.positions[i][j] -= 190
                else:
                    self.positions[i][j] += 10




