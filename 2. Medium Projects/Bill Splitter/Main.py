from SplitBill import SplitBill
import random

def number_joining_input():
    try:
        number_joining = int(input("Enter the number of friends joining (including you):\n"))
        return number_joining
    except ValueError:
        return -1

def friends_joining_input(num_joining):
    ls = []
    print("\nEnter the name of every friend (including you), each on a new line:")
    for i in range(num_joining):
        ls.append(input())
    return ls


def bill_amount_input():
    try:
        bill_amount = float(input("\nEnter the total bill value:\n"))
        return bill_amount
    except ValueError:
        return -1


def get_lucky_input():
    lucky_input = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:")
    return lucky_input == "Yes"


def get_lucky_friend(friends):
    lucky_friend = random.choice(friends)
    return lucky_friend


def execution():
    num_joining = number_joining_input()
    if num_joining <= 0:
        print("\nNo one is joining for the party")
        return
    friends_joining = friends_joining_input(num_joining)
    bill_amount = bill_amount_input()
    bill_class = SplitBill(friends_joining, bill_amount)

    lucky_input = get_lucky_input()
    if lucky_input:
        lucky_friend = get_lucky_friend(friends_joining)
        bill_class.update_lucky_friend(lucky_friend)
        print(f"\n{lucky_friend} is the lucky one!\n")
    else:
        print("\nNo one is going to be lucky\n")

    print()
    print(bill_class.bill_dictionary)

if __name__ == "__main__":
    execution()