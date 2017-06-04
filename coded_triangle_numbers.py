import time

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

start_time = time.clock()

with open('p042_words.txt') as fp:
    words = fp.read().split(',')
    words = [x.replace('"', '') for x in words]

word_sum = []
for word in words:
    word_sum.append(sum([alpha.index(x)+1 for x in word]))

total = 0
triangles = []
i = 0
while i <= max(word_sum):
    triangles.append(int(0.5*i*(i+1)))
    i += 1

for tri in triangles:
    total += word_sum.count(tri)

print(total)
print('Time = ', time.clock() - start_time)