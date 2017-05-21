def pascal_row_sum(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    prev_row = [1, 1]
    total_sum = sum(prev_row)
    for i in range(2,n+1):
        next_row = [0 for x in range(len(prev_row)+1)]
        next_row[0] = 1
        next_row[len(prev_row)] = 1
        for j in range(0, len(prev_row)-1):
            next_row[j+1] = prev_row[j] + prev_row[j+1]
        print(next_row)
        prev_row = next_row
        total_sum += sum(next_row)

    return total_sum

print(pascal_row_sum(21))
