from Board import Board
from EasyBot import EasyBot
from MediumBot import MediumBot
from HardBot import HardBot
from User import User

def take_input_command():
    valid_input = ["user", "easy", "medium", "hard"]
    while True:
        commands = input("Input command: ").split()
        if commands[0] == "exit":
            return "", "";
        elif commands[0] == "start":
            if len(commands) != 3:
                print("Bad parameters!")
            elif commands[1] not in valid_input or commands[2] not in valid_input:
                print("Bad parameters!")
            else:
                return commands[1], commands[2]
        else:
            print("Bad parameters!")


def evaluate_game_state(board):
    if board.win_check("X"):
        print("X wins\n")
    elif board.win_check("O"):
        print("O wins\n")
    elif board.draw_check():
        print("Draw\n")
    else:
        return False
    return True


def create_players(commands, board):
    ls = ["X", "O"]
    player_list = []
    for i in range(2):
        if commands[i] == "easy":
            player_list.append(EasyBot(board, ls[i]))
        elif commands[i] == "user":
            player_list.append(User(board, ls[i]))
        elif commands[i] == "medium":
            player_list.append(MediumBot(board, ls[i]))
        elif commands[i] == "hard":
            player_list.append(HardBot(board, ls[i]))
    return player_list


def main_execution():
    while True:
        commands = take_input_command()
        if commands[0] == "":
            break
        turn_execution(commands)
    

def turn_execution(commands):
    board = Board()
    player_list = create_players(commands, board)
    board.print_board()
    while True:
        for player in player_list:
            player.make_move()
            board.print_board()
            if evaluate_game_state(board):
                return


if __name__ == "__main__":
    main_execution()
    
    