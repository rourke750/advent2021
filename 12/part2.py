def traverse(start, nodes, cant_visit:{}, visited:[], path=''):
    if start == 'end':
        #print(path)
        return [path]
    next_nodes = nodes[start][1]
    c = cant_visit.copy()
    paths = []
    if start.islower():
        c[start] = True
        if len(visited) == 0 and start != 'start':
            for node in next_nodes:
                if node in c:
                    continue
                paths.extend(traverse(node, nodes, c, [start, True], '%s,%s' % (path, node)))
                
            
            
    for node in next_nodes:
        if len(visited) > 0 and node == visited[0] and visited[1]:
            #print(node)
            paths.extend(traverse(node, nodes, c, [node, False], '%s,%s' % (path, node)))
        elif node in c:
            continue
        else:
            paths.extend(traverse(node, nodes, c, visited, '%s,%s' % (path, node)))
    return paths
    
    
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
#print(nodes)
count = traverse('start', nodes, {}, [], 'start')
paths = {}
for c in count:
    paths[c] = True
print(len(paths))