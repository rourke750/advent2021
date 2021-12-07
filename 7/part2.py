def add(num):
    count = 0
    for n in range(1, num+1):
        count += n
    return count

with open('example.txt') as f:
    lines = f.readlines()

line = lines[0].split(',')
max = 0
count_look_up = {}

for l in line:
    i = int(l)
    if i > max:
        max = i
count = 0
print(max)
for n in range(0, max + 1):
    count += n
    count_look_up[n] = count

array_pos = [0] * (max + 1)
for l in line:
    i = int(l)
    for j in range(0, max + 1):
        array_pos[j] += count_look_up[abs(i - j)]
        
min = -1
for a in array_pos:
    if min == -1:
        min = a
    elif min > a:
        min = a
print(min)