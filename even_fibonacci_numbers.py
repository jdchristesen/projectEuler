previous_first = 1
previous_second = 2
even_sum = 2

while previous_second < 4000000:
    temp_sum = previous_first + previous_second

    if temp_sum % 2 == 0:
        even_sum += temp_sum

    previous_first = previous_second
    previous_second = temp_sum

print(even_sum)
