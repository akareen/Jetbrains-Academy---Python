import requests

def create_currency_cache():
    user_choice = input()
    json_dic = requests.get(f"http://www.floatrates.com/daily/{user_choice}.json").json()

    cache = {}
    for key, value in json_dic.items():
        cache[key] = value["rate"]

    return cache

def convert_currency(cache, amount, currency_to_convert):
    return amount * cache[currency_to_convert.lower()]

def print_result(in_cache,cache, amount, currency_to_convert):
    print("Checking the cache...")
    if in_cache:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
    print(f"You received {round(convert_currency(cache, amount, currency_to_convert), 2)} {currency_to_convert.upper()}.")


def loop():
    cache = create_currency_cache()
    currencies_in_cache = ["USD", "EUR"]
    while True:
        currency_to_convert = input()
        if currency_to_convert == "":
            break
        amount = float(input())
        if currency_to_convert.upper() in currencies_in_cache:
            print_result(True, cache, amount, currency_to_convert)
        else:
            print_result(False, cache, amount, currency_to_convert)
            currencies_in_cache.append(currency_to_convert.upper())

loop()