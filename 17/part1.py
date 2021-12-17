with open('example.txt') as f:
    lines = f.readlines()[0]
    
lines = lines.split(':')[1].strip().split(',')
x_range = lines[0][2:].split('..')
y_range = lines[1].strip()[2:].split('..')
print(y_range)

mappings = {}
min_x, max_x = int(x_range[0]), int(x_range[1]) + 1
min_y, max_y = int(y_range[0]), int(y_range[1]) + 1
for x in range(min_x, max_x):
    for y in range(min_y, max_y):
        key = "%d-%d" % (x, y)
        mappings[key] = True
 
def get_y_heighest(x_velocity, y_velocity, mapping, min_y, max_x):
    max_height = 0
    x_pos, y_pos = 0,0
    while True:
        x_pos += x_velocity
        y_pos += y_velocity
        max_height = max(max_height, y_pos)
        if x_velocity > 0:
            x_velocity -= 1
        y_velocity -= 1
        key = "%d-%d" % (x_pos, y_pos)
        # now apply rules
        if key in mapping:
            return max_height
        elif y_pos < min_y:
            return -1
        elif x_pos > max_x:
            return -1
        

max_height = 0
for x_velocity in range(1, 100):
    for y_velocity in range(1, 100):
        max_height = max(get_y_heighest(x_velocity, y_velocity, mappings, min_y, max_x), max_height)

print(max_height)