from math import factorial

largest_possible = factorial(20)

# it must be in steps of 20
for i in range(20, largest_possible, 20):
    if i % 19 == 0 and i % 18 == 0 and i % 17 == 0 and i % 16 == 0 and i % 15\
            == 0 and i % 14 == 0 and i % 13 == 0 and i % 12 == 0 and i % 11 \
            == 0:
        print(i)
        break
