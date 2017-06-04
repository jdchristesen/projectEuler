import time


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

start_time = time.clock()

# Can't be longer than 7 because 8 and 9 are divisible by 3
digits = set(['1', '2', '3', '4', '5', '6', '7'])

longest = 0
current = 7654321

while longest == 0:
    if '0' not in str(current) and len(str(current)) == len(digits) and not digits - set(str(current)):
        print(current)
        if is_prime(current):
            longest = current
    if current % 10 in [1, 7]:
        current -= 4
    elif current % 10 == 3:
        current -= 2

print('Time: {}'.format(time.clock() - start_time))
print(longest)
