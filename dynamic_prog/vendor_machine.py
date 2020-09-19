"""The program simulates a vendor machine handling the dispensing of change.
Using dynamic programming to solve the task"""


def vend_make_change(coin_value_list, change, min_coins, coins_used):
    # coin_value_list takes in a list with the denomination of coin to be used.
    # change takes the amount of change to be dispensed
    # The minimum amount of coins to be used to dispense that change
    # contains a list of the coins used to dispense the change
    for pennies in range(change + 1):
        coin_count = pennies
        new_coin = 1
        for coin in [quid for quid in coin_value_list if quid <= pennies]:
            if min_coins[pennies - coin] + 1 < coin_count:
                coin_count = min_coins[pennies-coin]+1
                new_coin = coin
        min_coins[pennies] = coin_count
        coins_used[pennies] = new_coin
    return min_coins[change]


def dispense_coins(coins_used, change):
    coin = change
    while coin > 0:
        coined = coins_used[coin]
        print(coined)
        coin = coin - coined  # Subtracts the coin/change from the coin
        # dispensed
