def is_abundant(n):
    if n <= 0:
        return False

    divisors = [1]
    i = 2
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            divisors.append(int(n / i))
        i += 1

    if sum(set(divisors)) > n:
        return True
    else:
        return False

abundant_numbers = set()

total_sum = 0

for target in range(28124):
    if is_abundant(target):
        abundant_numbers.add(target)
    if not any((target - j in abundant_numbers) for j in abundant_numbers):
        total_sum += target

print(total_sum)
