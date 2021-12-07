with open('example.txt') as f:
    lines = f.readlines()

line = lines[0].split(',')
max = 0
for l in line:
    i = int(l)
    if i > max:
        max = i

array_pos = [0] * (max + 1)
for l in line:
    i = int(l)
    for j in range(0, max + 1):
        array_pos[j] += abs(i - j)
        
min = -1
for a in array_pos:
    if min == -1:
        min = a
    elif min > a:
        min = a
print(min)