import time

start_time = time.clock()

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

answers = []
test = 987654321
longest = 0
while longest == 0:
    if len(set(str(test))) == 9 and '0' not in str(test):
        print(test)
        for i in range(2, 5):
            first = int(str(test)[:i])
            second = first * 2
            third = first * 3
            two_str = str(first) + str(second)
            three_str = str(first) + str(second) + str(third)
            if '0' not in two_str and len(two_str) == 9 and len(set(two_str)) == 9:
                longest = int(two_str)
                break
            elif '0' not in two_str and len(three_str) == 9 and len(set(three_str)) == 9:
                longest = int(three_str)
                break
    test -= 1

print(longest)
print(first, second, third)
print(set(str(first) + str(second)))
print('Time: {}'.format(time.clock() - start_time))