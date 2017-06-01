def is_prime(n):
    if n <= 1:
        return False
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

circular_primes = []
not_circular = set()
for x in range(500000):
    if ('8' or '6' or '5' or '4' or '2' or '0') in str(x):
        pass
    elif x not in circular_primes and is_prime(x):
        circular_bool = True
        circular = x
        for i in range(len(str(circular))):
            circular = int(str(circular)[-1] + str(circular)[:-1])
            if not is_prime(circular):
                circular_bool = False

        if circular_bool:
            circular = x
            for i in range(len(str(circular))):
                circular = int(str(circular)[-1] + str(circular)[:-1])
                circular_primes.append(circular)
        else:
            not_circular.add(''.join(sorted(str(x))))

print(len(sorted(set(circular_primes))))
