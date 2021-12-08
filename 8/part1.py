from collections import defaultdict

def r():
    return False

with open('example.txt') as f:
    lines = f.readlines()    

""" 1 -> 2
    4 -> 4
    7 ->3
    8 -> 7
"""
c = 0
for line in lines:
    row = line.split('|')
    elements = [r.strip() for r in row[0].split(' ')][:-1]
    mapping = defaultdict(r)
    for e in elements:
        l = len(e)
        if not (l == 2 or l == 4 or l == 3 or l == 7):
            continue
        s = ''.join(sorted(e))
        mapping[s] = True
    out_elements = [r.strip() for r in row[1].split(' ')][1:]
    print(mapping)
    for e in out_elements:
        s = ''.join(sorted(e))
        print(s)
        if mapping[s]:
            c += 1
print(c)