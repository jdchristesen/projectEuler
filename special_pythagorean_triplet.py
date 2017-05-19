from math import ceil

summation_target = 1000

for a in range(1, ceil(summation_target/3)):
    for b in range(a+1, summation_target):
        c = summation_target - a - b
        if a**2 + b**2 == c**2:
            print('{0}^2 + {1}^2 = {2}^2'.format(a, b, c))
            print(a * b * c)