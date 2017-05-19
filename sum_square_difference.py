first_hundred = [x for x in range(101)]

summation = sum(first_hundred)
square_of_sum = summation ** 2

squares = [x ** 2 for x in first_hundred]
sum_of_squares = sum(squares)

print(square_of_sum - sum_of_squares)
