digits_to_sum = str(2 ** 1000)
sum_of_digits = 0

for digit in digits_to_sum:
    sum_of_digits += int(digit)

print(sum_of_digits)