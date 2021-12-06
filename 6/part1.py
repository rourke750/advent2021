with open('example.txt') as f:
    lines = f.readlines()
    
    
days_to_count = {} # mapping of how many days left to the amount of fish
# now populate
for k in range(0,9):
    days_to_count[k] = 0
    
# populate the days_to_count from lines
for line in lines[0].split(','):
    n = int(line.strip())
    days_to_count[n] += 1
# count next 18 days
for i in range(0, 80):
    temp = days_to_count[0]
    for num in range(0,8):
        # shift everything down
        days_to_count[num] = days_to_count[num + 1]
    days_to_count[6] += temp
    days_to_count[8] = temp

count = 0
for k in days_to_count:
    count += days_to_count[k]
print(count)