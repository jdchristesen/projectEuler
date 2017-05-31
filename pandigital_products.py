import time

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

answers = []

start_time = time.clock()
for a in range(2, 100):
    if len(set(str(a))) != len(str(a)):
        continue

    start = 123 if a > 9 else 1234
    end = int((10000 / a) + 1)
    for b in range(start, end):
        if len(set(str(b))) != len(str(b)):
            continue
        c = a * b
        if len(str(a)) + len(str(b)) + len(str(c)) > len(digits):
            continue

        for dig in digits:
            pandigital = True
            if dig not in str(a) and dig not in str(b) and dig not in str(c):
                pandigital = False
                break
        if pandigital:
            answers.append([a, b, c])

print(sum(set([x[2] for x in answers])))
print('Time = ', time.clock() - start_time)

