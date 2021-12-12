def traverse(start, nodes, cant_visit:{}):
    next_nodes = nodes[start][1]
    c = cant_visit.copy()
    count = 0
    if start.islower():
        c[start] = True
    if start == 'end':
        return 1
    for node in next_nodes:
        if node in c:
            continue
        count += traverse(node, nodes, c)
    return count
    
    
with open('example.txt') as f:
    lines = f.readlines()
    
nodes = {}
    
for line in lines:
    array = line.split('-')
    node = array[0]
    pointer = array[1].strip()
    
    if node not in nodes:
        nodes[node] = (node, [],)
    if pointer not in nodes:
        nodes[pointer] = (pointer, [],)
    nodes[node][1].append(pointer)
    nodes[pointer][1].append(node)
print(nodes)
count = traverse('start', nodes, {})
print(count)