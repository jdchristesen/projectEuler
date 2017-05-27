def find_combinations(amount, values):
    if amount == 0:
        return 1
    elif len(values) < 1 or amount < 1:
        return 0
    else:
        return find_combinations(amount, values[:-1]) + find_combinations(amount - values[-1], values)


coins = [1, 2, 5, 10, 20, 50, 100, 200]

print(find_combinations(200, coins))
