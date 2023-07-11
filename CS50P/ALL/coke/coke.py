coin_values = [25, 10, 5, 1]  # acceptable denominations
total_coin_value = 0  # initialize total coin value to zero

while total_coin_value < 50:
    coin = input("Insert a coin: ")
    if coin.isdigit() and int(coin) in coin_values and 50 - total_coin_value:
        total_coin_value += int(coin)
        print("Amount due:", 50 - total_coin_value, )
    else:
        print("Invalid coin, try again.")

print("Change owed:", abs(total_coin_value - 50))
