with open('example.txt') as f:
    lines = f.readlines()
    
fold = False
max_x = 0
max_y = 0
mappings = []
for line in lines:
    if line == '\n':
        fold = True
        continue
    
    if fold:
        l = line.split('=')
        letter = l[0][-1]
        pos = int(l[1])
        if letter == 'y':
            for m in list(mappings):
                y_pos = m[1]
                x_pos = m[0]
                if y_pos <= pos:
                    continue
                diff = pos - (y_pos - pos)
                mappings.remove(m)
                mappings.append((x_pos, diff,))
            max_y = pos
        elif letter == 'x':
            for m in list(mappings):
                y_pos = m[1]
                x_pos = m[0]
                if x_pos <= pos:
                    continue
                diff = pos - (x_pos - pos)
                mappings.remove(m)
                mappings.append((diff, y_pos,))
            max_x = pos
        break
    else:
        l = line.split(',')
        x = int(l[0])
        y = int(l[1].strip())
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        mappings.append((x,y,))
        

done = {}
count = 0
for e in mappings:
    key = '%d-%d' % (e[0], e[1])
    if key in done:
        continue
    done[key] = True
    count += 1
print(count)