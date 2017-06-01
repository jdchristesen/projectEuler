from math import factorial
import time

digits = [factorial(x) for x in range(10)]
answers = []

start_time = time.clock()

for i in range(3, 10**6):
    summation = 0
    for digit in str(i):
        summation += digits[int(digit)]

    if summation == i:
        answers.append(i)

print(answers)
print(sum(answers))
print(time.clock() - start_time)
