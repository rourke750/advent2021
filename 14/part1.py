with open('example.txt') as f:
    lines = f.readlines()
    
pairs = {}
polymer = lines[0].strip()
for line in lines[2:]:
    array = line.split('->')
    key = array[0].strip()
    value = array[1].strip()
    pairs[key] = value

for z in range(0, 10):
    new_poly = polymer
    middle_pos = 1
    for i in range(0, len(polymer) - 1):
        key = "%s%s" % (polymer[i], polymer[i+1])
        if key in pairs:
            new_poly = "%s%s%s" % (new_poly[0:middle_pos], pairs[key], new_poly[middle_pos:])
            middle_pos += 1
        middle_pos += 1
    polymer = new_poly

count = {}
for l in polymer:
    if l not in count:
        count[l] = 0
    count[l] += 1

max = -1
min = -1
print(count)
for key in count:
    c = count[key]
    if max < c:
        max = c
    elif min == -1 or c < min:
        min = c
print(max-min)