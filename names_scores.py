alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

names = ''
with open('p022_names.txt') as fp:
    for line in fp:
        names += line

names = names.split(',')
names = sorted(names)

total = 0
for i, name in enumerate(names):
    name = name.strip('"')
    temp = 0
    for letter in name:
        temp += alpha.index(letter) + 1
    total += i * temp

print(total)