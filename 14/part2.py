from collections import deque 
from datetime import datetime

with open('example.txt') as f:
    lines = f.readlines()
    
pairs = {}
polymer = lines[0].strip()
for line in lines[2:]:
    array = line.split('->')
    key = array[0].strip()
    value = array[1].strip()
    pairs[key] = value


for z in range(0, 1):
    print(z)
    new_poly = [polymer[0]]
    i = 0
    while i < len(polymer) - 1:
        f, s = polymer[i], polymer[i+1]
        key = "%s%s" % (f, s)
        print(key)
        if key in pairs:
            v = f + pairs[key] + s
            new_poly.append(f + pairs[key])
            pairs[v] = key
        else:
            new_poly.append(polymer[i])
        i += 1
    polymer = new_poly
    print(pairs)

print(polymer)
s = ''
for i in range(0, len(polymer)):
    v = polymer[i]
    if v in pairs:
        s += pairs[v]
    else:
        s += v
#print(s)
