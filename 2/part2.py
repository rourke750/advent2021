"""
[0,0,0,1  | 
 0,0,0,0  V down
 0,0,0,0
 0,0,0,0

            ]
"""
pos = 0
depth = 0
aim = 0
with open('example_2.txt') as f:
    lines = f.readlines()
for line in lines:
    arr = line.split(' ')
    operation = arr[0]
    amount = int(arr[1])
    if operation == 'forward':
        pos += amount
        depth += amount * aim
    elif operation == 'down':
        aim += amount
    else:
        aim -= amount
print (pos * depth)