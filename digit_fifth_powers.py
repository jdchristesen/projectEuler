def sum_digits_to_power(number, power):
    number_str = str(number)
    summation = 0
    for digit in number_str:
       summation += int(digit) ** power
    return summation

total = 0
power = 5

counter = 1
upper_limit = 9
while upper_limit <= counter*9**power:
    upper_limit += 9 * (10 ** counter)
    counter += 1

print(upper_limit)

for i in range(2, upper_limit):
    if i == sum_digits_to_power(i, 5):
        total += i

print(total)