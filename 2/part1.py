"""
[0,0,0,1  | 
 0,0,0,0  V down
 0,0,0,0
 0,0,0,0

            ]
"""
pos = 0
depth = 0
with open('example.txt') as f:
    lines = f.readlines()
for line in lines:
    arr = line.split(' ')
    operation = arr[0]
    amount = int(arr[1])
    if operation == 'forward':
        pos += amount
    elif operation == 'down':
        depth += amount
    else:
        depth -= amount
print (pos * depth)