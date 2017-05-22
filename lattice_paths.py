import math

def pascal_row_sum(n):
    if n == 0:
        return 1

    prev_row = [1, 1]
    for i in range(1, n):
        next_row = [0 for x in range(len(prev_row)+1)]
        next_row[0] = 1
        next_row[len(prev_row)] = 1
        for j in range(0, len(prev_row)-1):
            next_row[j+1] = prev_row[j] + prev_row[j+1]
        print(next_row)
        prev_row = next_row

    for i in range(n, 0, -1):
        next_row = [0 for x in range(len(prev_row)-1)]
        for j in range(1, len(prev_row)):
            next_row[j-1] = prev_row[j-1] + prev_row[j]
        print(next_row)
        prev_row = next_row

    return next_row

cube_size = 20
print(pascal_row_sum(cube_size))

# This is 2*cube_size choose cube_size
print(math.factorial(2*cube_size) / (math.factorial(cube_size) ** 2))
