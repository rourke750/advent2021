from collections import defaultdict
import math

def r():
    return 0

with open('example.txt') as f:
    lines = f.readlines()
    
pairs = {}
polymer_init = lines[0].strip()
for line in lines[2:]:
    array = line.split('->')
    key = array[0].strip()
    value = array[1].strip()
    pairs[key] = value

polymer = defaultdict(r)
for i in range(0, len(polymer_init) - 1):
        key = "%s%s" % (polymer_init[i], polymer_init[i+1])
        polymer[key] += 1
        
count = defaultdict(r)
for z in range(0, 40):
    new_poly = defaultdict(r)
    for k in polymer:
        #if k not in new_poly:
            #new_poly[k] = polymer[k]
        l = pairs[k]
        k1 = "%s%s" % (k[0], l)
        k2 = "%s%s" % (l, k[1])
        
        new_poly[k1] += polymer[k]
        new_poly[k2] += polymer[k]
    polymer = new_poly

print(polymer)
for e in polymer:
    print(e)
    count[e[0]] += polymer[e]
    count[e[1]] += polymer[e]
max = -1
min = -1
for c in count:
    v = math.ceil(count[c]/2)
    if v > max:
        max = v
    if min == -1 or v < min:
        min = v
print(max - min)
