def find_combinations(amount, values):
    if amount == 0:
        return 1
    elif len(values) < 1 or amount < 1:
        return 0
    else:
        return find_combinations(amount, values[:-1]) \
               + find_combinations(amount - values[-1], values)


def coin_dp(amount, values):
    ways = [0 for x in range(amount+1)]
    ways[0] = 1
    for coin in values:
        for j in range(coin, amount+1):
            ways[j] = ways[j] + ways[j - coin]

    return ways[-1]

coins = [1, 2, 5, 10, 20, 50, 100, 200]

print(find_combinations(200, coins))
print(coin_dp(200, coins))
