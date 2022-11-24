
import math
import sys

args = sys.argv

type_ = False
principal = False
periods = False
interest = False
payment = False

for i in range(len(args)):
    if args[i].split("=")[0] == "--type":
        type_ = args[i].split("=")[1]
    elif args[i].split("=")[0] == "--principal":
        principal = int(args[i].split("=")[1])
    elif args[i].split("=")[0] == "--periods":
        periods = int(args[i].split("=")[1])
    elif args[i].split("=")[0] == "--interest":
        interest = float(args[i].split("=")[1])
    elif args[i].split("=")[0] == "--payment":
        payment = int(args[i].split("=")[1])

if type_ == "diff":
    if principal and periods and interest:
        i = interest / (12 * 100)
        total = 0
        for m in range(1, periods + 1):
            d = math.ceil(principal / periods + i * (principal - (principal * (m - 1)) / periods))
            print(f"Month {m}: payment is {d}")
            total += d
        print()
        print(f"Overpayment = {total - principal}")
    else:
        print("Incorrect parameters.")
elif type_ == "annuity":
    if principal and periods and interest:
        i = interest / (12 * 100)
        annuity = math.ceil(principal * (i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))
        print(f"Your annuity payment = {annuity}!")
        print(f"Overpayment = {annuity * periods - principal}")
    elif payment and periods and interest:
        i = interest / (12 * 100)
        principal = math.floor(payment / (i * math.pow(1 + i, periods) / (math.pow(1 + i, periods) - 1)))
        print(f"Your loan principal = {principal}!")
        print(f"Overpayment = {payment * periods - principal}")
    elif principal and payment and interest:
        i = interest / (12 * 100)
        periods = math.log(payment / (payment - i * principal), 1 + i)
        periods = math.ceil(periods)
        and_ = ""
        n_years = str(periods // 12) + " years"
        n_months = str(periods % 12) + " months"
        if periods // 12 != 0 and periods % 12 != 0:
            and_ = " and "
        elif periods // 12 == 0:
            n_years = ""
        elif periods % 12 == 0:
            n_months = ""
        print(f"It will take {n_years}{and_}{n_months} to repay this loan!")
        print(f"Overpayment = {periods * payment - principal}")
    else:
        print("Incorrect parameters.")
else:
    print("Incorrect parameters.")