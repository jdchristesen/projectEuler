months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day = 1  # 1 Jan 1900 was a Monday
total_sundays = 0

for year in range(1900, 2001):
    for i, month in enumerate(months):
        if i == 1 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            day = (day + 29) % 7
        else:
            day = (day + month) % 7

        if year >= 1901 and day == 0:
            total_sundays += 1

print(total_sundays)