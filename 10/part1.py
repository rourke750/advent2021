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
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    
stack = deque()
count = 0
for line in lines:
    for c in line:
        if c in valid_opening:
            stack.append(c)
        elif c in valid_closing:
            v = stack.pop()
            if valid_opening[v] != c:
                count += points[c]
                break
print(count)