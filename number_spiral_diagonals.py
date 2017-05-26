from math import sqrt
spiral = 1001

upper_right = [n**2 for n in range(1, spiral+1, 2)]
upper_left = [n - (sqrt(n) - 1) for n in upper_right[1:]]
lower_left = [n - 2*(sqrt(n) - 1) for n in upper_right[1:]]
lower_right = [n - 3*(sqrt(n) - 1) for n in upper_right[1:]]
print(lower_right)
print(lower_left)
print(upper_left)
print(upper_right)

print((sum(upper_right) + sum(lower_left) + sum(upper_left) + sum(lower_right)))
