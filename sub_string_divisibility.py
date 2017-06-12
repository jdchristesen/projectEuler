from itertools import permutations
import time

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
divisors = [2, 3, 5, 7, 11, 13, 17]
answer = 0
start_time = time.clock()

for test_case in permutations(digits):
    for i, div in enumerate(divisors):
        if int(test_case[i+1] + test_case[i+2] + test_case[i+3]) % div != 0:
            test_case = None
            break

    if test_case is not None:
        answer += int(''.join(test_case))

print(answer)
print(time.clock() - start_time)