def find_basin(dict, matrix, pos):
    y = int(pos / len(matrix[0]))
    x = pos % len(matrix[0])
    
    left_pos = x - 1
    right_pos = x + 1
    up_pos = y - 1
    down_pos = y + 1
    
    row = matrix[y]
    
    actual_left = left_pos + len(row) * y
    actual_right = right_pos + len(row) * y
    actual_up = x + len(matrix[0]) * up_pos
    actual_down = x + len(matrix[0]) * down_pos
    
    
    number = 1
    dict[pos] = True
    found = False
    if left_pos >= 0 and row[left_pos] < 9 and actual_left not in dict:
        number += find_basin(dict, matrix, actual_left)
    if right_pos < len(row) and row[right_pos] < 9 and actual_right not in dict:
        number += find_basin(dict, matrix, actual_right)
    if up_pos >= 0 and matrix[up_pos][x] < 9 and actual_up not in dict:
        number += find_basin(dict, matrix, actual_up)
    if down_pos < height and matrix[down_pos][x] < 9 and actual_down not in dict:
        number += find_basin(dict, matrix, actual_down)
    return number
    

with open('example.txt') as f:
    lines = f.readlines()

matrix = []
for line in lines:
    line = line.strip()
    row = []
    for e in line:
        row.append(int(e))
    matrix.append(row)

low_points = []
    
height = len(matrix)
for z in range(0, height):
    row = matrix[z]
    for i in range(0, len(row)):
        left_pos = i - 1
        right_pos = i + 1
        up_pos = z - 1
        down_pos = z + 1
        
        actual_pos = i + len(row) * z 
        
        number = row[i]
        low_point = True
        if left_pos >= 0 and row[left_pos] <= number:
            low_point = False
        if right_pos < len(row) and row[right_pos] <= number:
            low_point = False
        if up_pos >= 0 and matrix[up_pos][i] <= number:
            low_point = False
        if down_pos < height and matrix[down_pos][i] <= number:
            low_point = False
        if low_point:
            low_points.append(actual_pos)
            
            
# now we have the low points find the basins

nums = []
for point in low_points:
    size = find_basin({}, matrix, point)
    print(size)
    nums.append(size)
    
nums.sort()

c = 1
for n in nums[-3:]:
    c *= n
print(c)
