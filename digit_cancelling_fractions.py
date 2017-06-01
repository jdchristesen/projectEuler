from fractions import Fraction

answer = 1

for numerator in range(10, 100):
    if numerator % 10 == int(numerator / 10):
        continue
    for denominator in range(numerator + 1, 100):
        if denominator % 10 == int(denominator / 10):
            continue
        frac = [0]
        for num in str(numerator):
            if num in str(denominator) and num != '0':
                numerator_new = int(str(numerator).replace(num, ''))
                denominator_new = int(str(denominator).replace(num, ''))
                if denominator_new == 0:
                    break
                frac = [numerator_new / denominator_new, numerator_new,
                        denominator_new]
        if frac[0] == 0:
            continue
        if numerator/denominator == frac[0]:
            answer *= (numerator_new/denominator_new)
            print('{} / {}'.format(numerator, denominator))

print(Fraction(answer).limit_denominator(1000))
