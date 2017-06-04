import time
from math import ceil

start_time = time.clock()

summation_target = 1000
answer = [0 for x in range(summation_target + 1)]


for a in range(1, summation_target):
    for b in range(a+1, summation_target):
        c = (a**2 + b**2)**0.5
        if c % 1 == 0 and a+b+c <= 1000:
            answer[int(a+b+c)] += 1

print('Time: {}'.format(time.clock() - start_time))
print(answer.index(max(answer)))
