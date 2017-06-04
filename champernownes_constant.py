import time

start_time = time.clock()

exponent = 0
answer = []
constant = '1'
i = 1

while len(answer) != 7:
    if i == 10**exponent:
        answer.append(int(constant[i-1]))
        exponent += 1
    i += 1
    constant += str(i)

print('Time: {}'.format(time.clock() - start_time))
final_answer = 1
for x in answer:
    final_answer *= x

print(final_answer)