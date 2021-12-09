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
            low_points.append(number + 1)
c = 0
for n in low_points:
    c += n
print(c)