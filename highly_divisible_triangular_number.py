def num_of_divisors(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        divisor_count = 2
    i = 2
    while i * i <= n:
        if n % i == 0:
            divisor_count += 2
        i += 1
    return divisor_count

count = 0
natural_numbers = [1]
while count < 500:
    # print('Sum ', sum(natural_numbers))
    count = num_of_divisors(sum(natural_numbers))
    # print('Count ', count)
    natural_numbers.append(natural_numbers[-1]+1)

print(sum(natural_numbers[:-1]))