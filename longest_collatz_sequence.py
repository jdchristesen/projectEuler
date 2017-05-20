def collatz_chain(n):
    if n <= 1:
        return 1
    elif n % 2 == 0:
        return collatz_chain(n/2) + 1
    else:
        return collatz_chain(3 * n + 1) + 1

largest_chain = 0

for i in range(1000001):
    chain = collatz_chain(i)
    if chain > largest_chain:
        starting_number_for_longest_chain = i
        largest_chain = chain

print(starting_number_for_longest_chain)