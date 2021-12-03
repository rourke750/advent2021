def find_numbers(lines:[], pos:int, direction:bool):
    key = 0
    for line in lines:
        if line[pos] == '0':
            key -= 1
        else:
            key += 1
            
    print(key)
    if direction:
        if key >= 0:
            key = '1'
        else:
            key = '0'
    else:
        if key < 0:
            key = '1'
        else:
            key = '0'
    
    new_array = []

    for line in lines:
        if line[pos] == key:
            new_array.append(line)
            
    print(new_array)
            
    if len(new_array) == 1:
        return new_array
    return find_numbers(new_array, pos + 1, direction)
    
def convert_binary_dec(array):
    pos = pow(2, len(array) - 1)
    num = 0
    for x in array:
        if int(x) > 0:
            num += pos
        pos = pos / 2
    return num
    

with open('example2.txt') as f:
    lines = f.readlines()
    
lines = [x.strip() for x in lines]
l = len(lines[0])
array = [0 for x in range(0, l)]

    
v = find_numbers(lines, 0, True)
oxygen = v[0]
oxygen_v = convert_binary_dec(oxygen)
print(oxygen_v)


v = find_numbers(lines, 0, False)
scrub = v[0]
scrub_v = convert_binary_dec(scrub)
print(scrub_v)

print(oxygen_v * scrub_v)