numbers_dict = {0: '',
                1: 'one',
                2: 'two',
                3: 'three',
                4: 'four',
                5: 'five',
                6: 'six',
                7: 'seven',
                8: 'eight',
                9: 'nine',
                10: 'ten',
                11: 'eleven',
                12: 'twelve',
                13: 'thirteen',
                14: 'fourteen',
                15: 'fifteen',
                16: 'sixteen',
                17: 'seventeen',
                18: 'eighteen',
                19: 'nineteen',
                20: 'twenty',
                30: 'thirty',
                40: 'forty',
                50: 'fifty',
                60: 'sixty',
                70: 'seventy',
                80: 'eighty',
                90: 'ninety',
                100: 'hundred',
                1000: 'thousand'}

complete_str = ''
for i in range(1, 1001):
    if i <= 20:
        complete_str += numbers_dict[i]
    elif i < 100:
        complete_str += numbers_dict[i - i % 10] + numbers_dict[i % 10]
    elif i < 1000:
        complete_str += numbers_dict[int(i / 100)] + numbers_dict[100]
        if 0 < i % 100 <= 20:
            complete_str += 'and' + numbers_dict[i % 100]
        elif i % 100 > 20:
            complete_str += 'and' + numbers_dict[i % 100 - i % 10] + numbers_dict[i % 10]

    elif i == 1000:
        complete_str += numbers_dict[i / 1000] + numbers_dict[i]

print(complete_str)
print(len(complete_str))
