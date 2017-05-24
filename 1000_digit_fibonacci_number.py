fib_seq = [1, 1]
i = 2
while len(str(fib_seq[i-1] + fib_seq[i-2])) < 1000:
    fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    i += 1

print(i+1)