import string

def take_pencil_input():
    print("How many pencils would you like to use:")
    while True:
        try:
            num_pencils = int(input())
            if num_pencils > 0:
                return num_pencils
            else:
                print("The number of pencils should be positive")
        except ValueError:
            print("The number of pencils should be numeric")


def take_name_input():
    names = ["John", "Jack"]
    print("Who will be the first (John, Jack):")
    while True:
        person_name = input()
        if person_name in names:
            return person_name
        else:
            print("Choose between 'John' and 'Jack'")


def pencils_taken_input():
    valid_choices = [1, 2, 3]
    while True:
        try:
            num_pencils_taken = int(input())
            if num_pencils_taken in valid_choices:
                return num_pencils_taken
            else:
                print("Possible values: '1', '2' or '3'")
        except ValueError:
            print("Possible values: '1', '2' or '3'")


def check_correct_taken_loop(num_pencils):
    while True:
        num_pencils_taken = pencils_taken_input()
        if num_pencils_taken <= num_pencils:
            return num_pencils_taken
        else:
            print("Too many pencils were taken")

def start_of_move(person_name, num_pencils):
    print("|" * num_pencils)
    print(f"{person_name}'s turn!")


def human_move(num_pencils):
    start_of_move("John", num_pencils)
    num_pencils -= check_correct_taken_loop(num_pencils)
    return num_pencils


def robot_move(num_pencils):
    start_of_move("Jack", num_pencils)
    if num_pencils % 4 == 1:
        print(1)
        num_pencils -=  1
    elif num_pencils % 4 == 0 and num_pencils >= 4:
        print(3)
        num_pencils -= 3
    else:
        print(num_pencils % 4 - 1)
        num_pencils -= num_pencils % 4 - 1
    return num_pencils


def game_execution():
    num_pencils = take_pencil_input()
    person_name = take_name_input()

    while num_pencils > 0:
        if person_name == "John":
            num_pencils = human_move(num_pencils)
            person_name = "Jack"
        else:
            num_pencils = robot_move(num_pencils)
            person_name = "John"

        if num_pencils == 0:
            print(f"{person_name} won!")
            break
        

if __name__ == "__main__":
    game_execution()

