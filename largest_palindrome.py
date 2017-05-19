from math import ceil, floor
largest_palindrome = 0

for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        product = i * j
        product_str = str(product)
        first_half = product_str[:floor(len(product_str)/2)]
        second_half = product_str[ceil(len(product_str)/2):]
        second_half_reverse = second_half[::-1]
        if i * j > largest_palindrome and first_half == second_half_reverse:
            largest_palindrome = i * j

print(largest_palindrome)