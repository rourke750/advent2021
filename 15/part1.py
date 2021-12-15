import math
def next(available_nodes:[]):
    if len(available_nodes) == 0:
        return None
    min_weight = 20
    temp = None
    for t in list(available_nodes):
        if t[2] < min_weight:
            temp = t
            min_weight = t[2]
        """
        elif t[2] == min_weight:
            # do the one closer to the end
            
            global END_X, END_Y
            d1 = math.sqrt(math.pow(t[0] - END_X, 2) + math.pow(t[1] - END_Y, 2))
            d2 = math.sqrt(math.pow(temp[0] - END_X, 2) + math.pow(temp[1] - END_Y, 2))
            if d1 < d2 : # d1 closer than d2 use d1
                print('eek')
                temp = t
                """
    available_nodes.remove(temp)
    return temp
    
def progress(matrix, weights, available_nodes:[]):
    global MAX_COUNT
    x_bounds = len(matrix[0])
    y_bounds = len(matrix)
    n = next(available_nodes)
    if n is None:
        return
    #print(len(available_nodes))
    # now add weight from previous to this
    weights["%d-%d" % (n[0],n[1])] = n[5] + matrix[n[1]][n[0]]
    # now add neighbors
    #for e in [(n[0]+1, n[1],), (n[0]-1, n[1],), (n[0], n[1]-1,), (n[0], n[1]+1,)]:
    for e in [(n[0]+1, n[1],), (n[0], n[1]+1,)]:
        if e[0] < 0 or e[0] >= x_bounds or e[1] < 0 or e[1] >= y_bounds:
            continue
        key = "%d-%d" % (e[0], e[1])
        if weights[key] != -1:
            # check if we need to recalculate this weight by seeing if adding the current weight to that position makes it less
            if weights["%d-%d" % (n[0],n[1])] + matrix[e[1]][e[0]] < weights[key]:
                #weights[key] = weights["%d-%d" % (n[0],n[1])] + matrix[e[1]][e[0]]
                pass
            else:
                continue
            
        available_nodes.append((e[0], e[1], matrix[e[1]][e[0]], n[0], n[1], weights["%d-%d" % (n[0],n[1])]))
    return (matrix, weights, available_nodes,)

with open('example.txt') as f:
    lines = f.readlines()
    
matrix = []
weights = {}
y = 0
for line in lines:
    x = 0
    array = []
    for e in line.strip():
        key = "%d-%d" % (x,y)
        if x == 0 and y == 0:
            n = 0
        else:
            n = int(e)
        array.append(n)
        weights[key] = -1
        x += 1
    matrix.append(array)
    y += 1

END_X = len(matrix[0])
END_Y = len(matrix)
    
# (0, 1, matrix[1][0],) x, y, its weight, other x, y, weight of the node that found it
weights['0-0'] = 0
r = progress(matrix, weights, [(0, 1, matrix[1][0], 0,0,0,), (1, 0, matrix[0][1], 0,0,0,)])
while r is not None:
    r = progress(r[0], r[1], r[2])
print(weights)
print(weights['0-2'])