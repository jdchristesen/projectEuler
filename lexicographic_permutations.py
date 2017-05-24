from math import factorial

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lexi_permutation = 1000000
permutation_list = []
summation = []

for i in range(len(digits)-1, 0, -1):
    prefactor = 0
    while prefactor * factorial(i) + sum(summation) < lexi_permutation:
        prefactor += 1

    permutation_list.append(prefactor-1)
    summation.append((prefactor-1) * factorial(i))

permutation_list.append(0)
print([digits.pop(x) for x in permutation_list])
