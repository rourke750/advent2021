with open('example.txt') as f:
    lines = f.readlines()[0]
    
lines = lines.split(':')[1].strip().split(',')
x_range = lines[0][2:].split('..')
y_range = lines[1].strip()[2:].split('..')
print(y_range)

mappings = {}
min_x, max_x = int(x_range[0]), int(x_range[1]) +1
min_y, max_y = int(y_range[0]), int(y_range[1]) +1
for x in range(min_x, max_x):
    for y in range(min_y, max_y):
        key = "%d-%d" % (x, y)
        mappings[key] = True


"""
 rules we want to do 
 1. if we ever go below min y and less than min x: increase x += 1, y+=1
 2. if we ever go below min y but in between minx and max x: y-=1
 3. if we ever go past max x but have the right y: x -=1
 4. need a rule to break
 """
 
def get_y_heighest(x_velocity, y_velocity, mapping, min_y, max_x):
    x_pos, y_pos = 0,0
    while True:
        x_pos += x_velocity
        y_pos += y_velocity
        if x_velocity > 0:
            x_velocity -= 1
        y_velocity -= 1
        key = "%d-%d" % (x_pos, y_pos)
        # now apply rules
        if key in mapping:
            return True
        elif y_pos < min_y:
            return False
        elif x_pos > max_x:
            return False
        

found = {}
for x_velocity in range(1, 1000):
    for y_velocity in range(-90, 800):
        c = get_y_heighest(x_velocity, y_velocity, mappings, min_y, max_x)
        if c:
            found["%d-%d" % (x_velocity, y_velocity)] = True

print(len(found))