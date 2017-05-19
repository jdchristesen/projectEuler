def num_of_divisors(n):
    i = 1
    divisor_count = 0
    while i * i <= n:
        if n % i == 0:
            divisor_count += 1
        i += 1
    return divisor_count

count = 0
natural_numbers = [1]
while count <= 500:
    count = num_of_divisors(sum(natural_numbers))
    print(count)
    natural_numbers.append(natural_numbers[-1]+1)