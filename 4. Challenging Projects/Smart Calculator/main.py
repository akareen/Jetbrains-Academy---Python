def main():
    while True:
        input_string = input()
        if input_string == "":
            continue
        if input_string[0] == "/":
            if input_string == "/exit":
                print("Bye!")
                break
            elif input_string == "/help":
                print("The program calculates the sum of numbers")
                continue
            else:
                print("Unknown command")
                continue
        if input_string == "":
            continue
        if input_string == "/exit":
            print("Bye!")
            break
        if input_string == "/help":
            print("The program calculates the sum of numbers")
            continue
        calculation = line_calculation(input_string)
        print(calculation)
    

def isNumber(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def symbol_calculation(item):
    total_neg = 0
    total_pos = 0
    cur_str = [*item]
    for symb in cur_str:
        if symb == "-":
            total_neg += 1
        elif symb == "+":
            total_pos += 1
        else:
            return -1
    if total_neg > 0 and total_pos > 0:
        if total_neg > total_pos:
            return 0
        else:
            return 1
    if total_neg > 0:
        if (total_neg % 2) == 0:
            return 1
        else:
            return 0
    return 1

def line_calculation(line_input):
    line_split = line_input.split()
    total = 0
    addition_mode = True
    operator_mode = False
    for item in line_split:
        if (not isNumber(item) and (item[0] == "-" or item[0] == "+")):
            flag = symbol_calculation(item)
            if flag == -1:
                return "Invalid expression"
            elif flag == 0:
                addition_mode = False
            else:
                addition_mode = True
            operator_mode = False
        elif(not isNumber(item)):
            return "Invalid expression"
        else:
            if operator_mode:
                return "Invalid expression"
            if addition_mode:
                total += int(item)
            else:
                total -= int(item)
            operator_mode = True
    return total


if __name__ == "__main__":
    main()