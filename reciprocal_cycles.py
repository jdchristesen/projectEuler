def get_reciprocal_length(n):
    remainders = []
    current = 10
    while current > 0:
        current = current % n
        if current in remainders:
            return len(remainders) - remainders.index(current)
        remainders.append(current)
        current *= 10
    return 0

longest = 0
for i in range(2, 1000):
    length = get_reciprocal_length(i)
    longest = i if length > longest else longest

print(longest)
