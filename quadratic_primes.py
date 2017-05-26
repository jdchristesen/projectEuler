def is_prime(n):
    if n <= 1:
        return True
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

b_primes = []
for b in range(1001):
    if is_prime(b):
        b_primes.append(b)

print(b_primes)

consecutive_primes = 0
final_coeff = []
for a in range(1000):
    print(a)
    for b in b_primes:
        for sign in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            i = 0
            while is_prime(i**2 + sign[0]*a*i + sign[1]*b):
                i += 1
            if i > consecutive_primes:
                print('Primes: ', i)
                consecutive_primes = i
                final_coeff = [sign[0] * a, sign[1] * b]

print(consecutive_primes)
print(final_coeff)