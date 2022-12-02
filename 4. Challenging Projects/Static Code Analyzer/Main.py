
def tooLong(line):
    return len(line) > 80 #includes the newline PEP 8 of 79 characters

def errorMessage(line_number):
    print(f"Line {line_number}: S001 Too long")

def read_file(filename):
    with open(filename) as f:
        i = 0
        for line in f:
            i += 1
            if tooLong(line):
                errorMessage(i)

def main(filename):
    read_file(filename)

if __name__ == "__main__":
    main(input())