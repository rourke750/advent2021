def flash(matrix, x, y, flashed):
    matrix[y][x] = 0
    flashed['%d-%d' % (y, x)] = True
    flashes = 1
    for xx in range(x-1, x+2):
        for yy in range(y-1, y+2):
            if xx == x and yy == y:
                continue
            if xx < 0 or xx > 9 or yy < 0 or yy > 9:
                continue
            if '%d-%d' % (yy, xx) not in flashed:
                matrix[yy][xx] += 1
            if matrix[yy][xx] > 9 and '%d-%d' % (yy, xx) not in flashed:
                flashes += flash(matrix, xx, yy, flashed)
    return flashes

with open('example.txt') as f:
    lines = f.readlines()
    
matrix = []
for line in lines:
    line = line.strip()
    row = []
    for e in line:
        row.append(int(e))
    matrix.append(row)

flashes = 0
for c in range(0, 100):
    for row in matrix:
        for i in range(0, 10):
            row[i] += 1
            
    flashed = {}
    for y in range(0, len(matrix)):
        row = matrix[y]
        for x in range(0, 10):
            if row[x] > 9 and '%d-%d' % (y, x) not in flashed:
                flashes += flash(matrix, x, y, flashed)
    
print(flashes)