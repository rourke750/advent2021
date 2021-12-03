with open('example1.txt') as f:
    lines = f.readlines()
    
array = [0 for x in range(0, 12)]
for line in lines:
    pos = 0
    for x in line:
        if pos == 12:
            break
        elif x == '0':
            array[pos] -= 1
        else:
            array[pos] += 1
        pos += 1
gamma = 0
epis = 0
pos = pow(2, 11)
print(epis)
for x in array:
    if x > 0:
        gamma += pos
    else:
        epis += pos
    pos = pos / 2
    
print(gamma)
print(epis)
print(int(gamma)* int(epis))
