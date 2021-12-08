from collections import defaultdict 

def r():
    return 0
    
def remove_missing(common, diff):
    for d in diff:
        pass
        
    

with open('example.txt') as f:
    lines = f.readlines()    

global_mappings = {
    '012456': 0,
    '25': 1,
    '02346': 2,
    '02356': 3,
    '1235': 4,
    '01356': 5,
    '013456': 6,
    '025': 7,
    '0123456': 8,
    '012356': 9
}

""" 1 -> 2
    4 -> 4
    7 ->3
    8 -> 7
"""
c = 0

for line in lines:
    row = line.split('|')
    elements = [r.strip() for r in row[0].split(' ')][:-1]
    
    # build letters to numbers
    letter_mappings = {}
    unfound_letters = []
    for e in elements:
        l = len(e)
        s = ''.join(sorted(e))
        if l == 2:
            letter_mappings[1] = s
        elif l == 4:
            letter_mappings[4] = s
        elif l == 3:
            letter_mappings[7] = s
        elif l == 7:
            letter_mappings[8] = s
        else:
            unfound_letters.append(s)
            
    mappings = defaultdict(r) # mapping to letters to the amount of times they appear
    for e in elements:
        for l in e:
            mappings[l] += 1
    # find the mappings that have 4, 9, or 6
    lost_mappings = {}
    for k in mappings:
        v = mappings[k]
        if v == 4 or v == 9 or v == 6:
            lost_mappings[v] = k
    #print(lost_mappings)
    #print(letter_mappings)
    #print('a')
    
    matrix = {} # mapping of letters to positions
    
    # now build missing numbers
    # missing 2,3,5,6,9
    
    # 0 is 7 + missing 3 - common 8
    #letters_0 = letter_mappings[7] + ''.join([lost_mappings[x] for x in lost_mappings])
    
    # find position 5
    for l in lost_mappings:
        v = lost_mappings[l]
        if v in letter_mappings[7]:
            # the letter in fifth position
            del lost_mappings[l]
            matrix[v] = 5
            break
    # find position 1
    for l in letter_mappings[7]:
        if l not in letter_mappings[1]:
            matrix[l] = 0
            break
    # find position 2
    for l in letter_mappings[1]:
        if l not in matrix:
            matrix[l] = 2
            
    # we can use 4 to eliminate 2 more positions
    del_key = None
    for l in lost_mappings:
        v = lost_mappings[l]
        if v in letter_mappings[4]:
            matrix[v] = 1
            del_key = l
    
    del lost_mappings[del_key]
    # last lost mapping is the position 4
    for l in lost_mappings:
        v = lost_mappings[l]
        matrix[v] = 4
        break
    
    # last letter not in 4 is position 3
    for l in letter_mappings[4]:
        if l not in matrix:
            matrix[l] = 3
            break
    
    #last letter is position 6
    for l in letter_mappings[8]:
        if l not in matrix:
            matrix[l] = 6
            break
    print(matrix)
    out_elements = [r.strip() for r in row[1].split(' ')][1:]
    num_val_out = ''
    for e in out_elements:
        num = ''
        for v in e:
            num += str(matrix[v])
        m = ''.join(sorted(num))
        print(m)
        num_val_out += str(global_mappings[m])
        
    c += int(num_val_out)
print(c)
    
