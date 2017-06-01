def is_palindrome(n):
    n = [int(x) for x in str(n)]
    if len(n) == 1:
        return True
    while len(n) >= 2:
        if n[0] == n[-1]:
            n.pop(-1)
            n.pop(0)
        else:
            return False
    return True

running_sum = 0
for x in range(10**6 + 1):
    if is_palindrome(x) and is_palindrome(bin(x)[2:]):
        running_sum += x

print(running_sum)