with open('example.txt') as f:
    lines = f.readlines()
    
# first convert hex to binary
binary_str = ''
for c in lines[0].strip():
    v = ord(c)
    num = 0
    if v >= 48 and v <= 57:
        num =  v - 48
    if v >= 65 and v <= 70:
        num = v - 55
    binary_str += f'{num:04b}'

def process_packet(pos:int, binary_str:str):
    version_num = int(binary_str[pos:pos+3], 2)
    pos += 3
    packet_type = int(binary_str[pos:pos+3], 2)
    pos += 3
    if packet_type == 4:
        temp_bit_string = ''
        while True:
            temp_bit_string += binary_str[pos+1:pos+5]
            if binary_str[pos] == '1':
                pos += 5
            else:
                pos += 5
                break
        return int(temp_bit_string, 2), pos
    else:
        length_type_id = int(binary_str[pos], 2)
        pos += 1
        value = 0
        if packet_type == 1 or packet_type == 2 or packet_type == 5 or packet_type == 6 or packet_type == 7:
            value = -1
            
        if length_type_id == 0:
            # read L now that is 15 bits
            L = int(binary_str[pos:pos+15], 2)
            
            pos += 15
            packet_lengths = pos + L
            while pos < packet_lengths:
                temp_value, pos = process_packet(pos, binary_str)
                if packet_type == 0:
                    value += temp_value
                elif packet_type == 1:
                    if value == -1:
                        value = 1
                    value *= temp_value
                elif packet_type == 2:
                    if value == -1:
                        value = temp_value
                    else:
                        value = min(value, temp_value)
                elif packet_type == 3:
                    value = max(value, temp_value)
                elif packet_type == 5:
                    if value == -1:
                        value = temp_value
                    else:
                        value = 1 if value > temp_value else 0
                elif packet_type == 6:
                    if value == -1:
                        value = temp_value
                    else:
                        value = 1 if value < temp_value else 0
                elif packet_type == 7:
                    if value == -1:
                        value = temp_value
                    else:
                        value = 1 if value == temp_value else 0
        elif length_type_id == 1:
            amount_sub_packets = int(binary_str[pos:pos+11], 2)
            pos += 11
            for i in range(amount_sub_packets):
                temp_value, pos = process_packet(pos, binary_str)
                if packet_type == 0:
                    value += temp_value
                elif packet_type == 1:
                    if value == -1:
                        value = 1
                    value *= temp_value
                elif packet_type == 2:
                    if value == -1:
                        value = temp_value
                    else:
                        value = min(value, temp_value)
                elif packet_type == 3:
                    value = max(value, temp_value)
                elif packet_type == 5:
                    if value == -1:
                        value = temp_value
                    else:
                        value = 1 if value > temp_value else 0
                elif packet_type == 6:
                    if value == -1:
                        value = temp_value
                    else:
                        value = 1 if value < temp_value else 0
                elif packet_type == 7:
                    if value == -1:
                        value = temp_value
                    else:
                        value = 1 if value == temp_value else 0
        
        if value == -1:
            value = 0
        return value, pos
version_count, pos = process_packet(0, binary_str)
print(version_count)
print(pos)
print(len(binary_str))
# wrong 300348090223349
# wrong 252367636932048
# wrong 300349675719184
# wrong 300349646524448
# wrong 110449114800
#       110434737925      