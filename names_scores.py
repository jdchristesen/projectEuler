alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

names = ''
with open('p022_names.txt') as fp:
    for line in fp:
        names += line

names = names.split(',')
names = [x.strip('"') for x in names]
names = sorted(names)

total = 0
for i, name in enumerate(names):
    temp = 0
    for letter in name:
        temp += alpha.index(letter) + 1
    total += (i + 1) * temp

print(total)