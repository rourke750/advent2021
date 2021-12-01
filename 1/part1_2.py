with open('example1_2.txt') as f:
    lines = f.readlines()
pos = 0
bucket = []
for line in lines:
    num = int(line)
    #index = pos % 3
    bucket.append([num])
    if pos >= 1:
        bucket[pos - 1].append(num)
    if pos >= 2:
        bucket[pos - 2].append(num)
    pos += 1

window = []
for b in bucket:
    if len(b) < 3:
        continue
    sum = 0
    for v in b:
        sum += v
    window.append(sum)
    
previous = 0
count = -1
for line in window:
    num = int(line)
    if num > previous:
        count += 1
    previous = num
print(count)