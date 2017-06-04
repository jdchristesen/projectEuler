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

truncatable_primes = []
current = 11

while len(truncatable_primes) < 11:
    if is_prime(current):
        truncatable_primes.append(current)
        current_list = [int(x) for x in str(current)]
        for i in range(1, len(str(current))):
            left = str(current)[:i]
            right = str(current)[i:]
            print('Current: {} Left: {} Right: {}'.format(current, left, right))
            if not is_prime(int(left)) or not is_prime(int(right)):
                truncatable_primes.remove(current)
                break

    if current >= 1e6:
        break
    current += 1

print(truncatable_primes)
print(sum(truncatable_primes))