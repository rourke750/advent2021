
with open('example1.txt') as f:
    lines = f.readlines()
    
matrix = {} # mapping of x -> y -> count
for line in lines:
    array = line.split('->')
    pre, post = array[0].split(','), array[1].split(',')
    x1, y1 = int(pre[0].strip()), int(pre[1].strip())
    x2, y2 = int(post[0].strip()), int(post[1].strip())
    if x1 == x2:
        if x1 not in matrix:
            matrix[x1] = {}
        if y1 <= y2:
            while y1 <= y2:
                if y1 not in matrix[x1]:
                    matrix[x1][y1] = 0
                matrix[x1][y1] += 1
                y1 += 1
        else:
            while y1 >= y2:
                if y1 not in matrix[x1]:
                    matrix[x1][y1] = 0
                matrix[x1][y1] += 1
                y1 -= 1
    elif y1 == y2:
        if x1 <= x2:
            while x1 <= x2:
                if x1 not in matrix:
                    matrix[x1] = {}
                if y1 not in matrix[x1]:
                    matrix[x1][y1] = 0
                matrix[x1][y1] += 1
                x1 += 1
        else:
            while x1 >= x2:
                if x1 not in matrix:
                    matrix[x1] = {}
                if y2 not in matrix[x1]:
                    matrix[x1][y2] = 0
                matrix[x1][y2] += 1
                x1 -= 1
                
for y in matrix:
    s = ''
    for x in range(0,10):
        if x in matrix[y]:
            s += str(matrix[y][x])
        else:
            s +='.'
    print(s)
count = 0
for y in matrix:
    for x in matrix[y]:
        if matrix[y][x] >= 2:
            count += 1
print(count)