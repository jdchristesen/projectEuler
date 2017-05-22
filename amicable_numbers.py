def proper_divisors(n):
    if n <= 0:
        return []

    divisors = [1]
    i = 2
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            divisors.append(int(n / i))
        i += 1

    return sorted(divisors)

amicable_dict = {}
total = 0
print(proper_divisors(220))
print(proper_divisors(284))
for i in range(10001):
    summation = sum(proper_divisors(i))
    if summation in amicable_dict and amicable_dict[summation] == i:
        total += summation + i
    elif i in amicable_dict and amicable_dict[i] == summation:
        total += summation + i

    amicable_dict[i] = summation

print(total)

