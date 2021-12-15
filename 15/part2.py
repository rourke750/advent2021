def progress(matrix, weights, x, y, visited:{}):
    #weights["%d-%d" % (n[0],n[1])] = n[5] + matrix[n[1]][n[0]]
    x_bounds = len(matrix[0])
    y_bounds = len(matrix)
        
    # now add neighbors
    for e in [(x+1, y,), (x-1, y,), (x, y-1,), (x, y+1,)]:
        if e[0] < 0 or e[0] >= x_bounds or e[1] < 0 or e[1] >= y_bounds:
            continue
        key = "%d-%d" % (e[0], e[1])
        if key in visited:
            continue
        temp_weight = weights["%d-%d" % (x, y)] + matrix[e[1]][e[0]]
        weights["%d-%d" % (e[0], e[1])] = min(weights["%d-%d" % (x, y)] + matrix[e[1]][e[0]], weights["%d-%d" % (e[0], e[1])])
    visited["%d-%d" % (x, y)] = True
    
    smallest_key = None
    smallest_value = 9999999999
    for k in weights:
        v = weights[k]
        if k not in visited and (smallest_key is None or v < smallest_value):
            smallest_key = k
            smallest_value = v
        
    if smallest_key is None:
        return None
        
    array = smallest_key.split('-')
    return (matrix, weights, int(array[0]), int(array[1]), visited)

with open('example.txt') as f:
    lines = f.readlines()
    
temp_matrix = []
weights = {}
y = 0
for line in lines:
    x = 0
    array = []
    for e in line.strip():
        if x == 0 and y == 0:
            n = 0
        else:
            n = int(e)
        array.append(n)
        x += 1
    temp_matrix.append(array)
    y += 1

matrix = []
for y in range(5):
    for row in temp_matrix:
        array = []
        for x in range(5):
            #[[(x + y + z) % 10 +1 if (x + y + z) >= 10 else (x + y + z) for z in row] for row in temp_matrix[r_pos]]
            #print(row)
            array.extend([(x + y + z) % 10 +1 if (x + y + z) >= 10 else (x + y + z) for z in row])
        matrix.append(array)

for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        key = "%d-%d" % (x,y)
        weights[key] = 9999999999
        

    
# (0, 1, matrix[1][0],) x, y, its weight, other x, y, weight of the node that found it
weights['0-0'] = 0
r = progress(matrix, weights, 0, 0, {})
c = 0
while r is not None:
    r = progress(r[0], r[1], r[2], r[3], r[4])
print(weights)
print(matrix[49][49])