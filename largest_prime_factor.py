from math import sqrt

number_to_factor = 600851475143
largest_prime = 1
prime = False

for i in range(2, int(sqrt(number_to_factor))):
    if number_to_factor % i == 0:
        for j in range(2, int(sqrt(i))):
            if i % j == 0:
                prime = False
                break
            else:
                prime = True
        if prime:
            largest_prime = i
            prime = False

print(largest_prime)