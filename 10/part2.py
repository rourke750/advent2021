from collections import deque

with open('example.txt') as f:
    lines = f.readlines()

valid_opening = {
    '(': ')', 
    '[': ']',
    '{': '}',
    '<': '>'
    }
valid_closing = [')', ']', '}', '>']
points = {'(': 1, '[': 2, '{': 3, '<': 4}
    
counts = []
for line in lines:
    stack = deque()
    bad = False
    for c in line:
        if c in valid_opening:
            stack.append(c)
        elif c in valid_closing:
            v = stack.pop()
            if valid_opening[v] != c:
                bad = True
                break
    if bad:
        continue
    num = 0
    while len(stack) != 0:
        v = stack.pop()
        num *= 5
        num += points[v]
    counts.append(num)
counts.sort()
print(counts[int(len(counts) /2)])