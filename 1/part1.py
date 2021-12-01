with open('example1.txt') as f:
    lines = f.readlines()
previous = 0
count = -1
for line in lines:
    num = int(line)
    if num > previous:
        count += 1
    previous = num
print(count)