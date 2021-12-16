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
    
print(binary_str)

def process_packet(pos:int, binary_str:str):
    version_num = int(binary_str[pos:pos+3], 2)
    print('version', version_num)
    version_count = version_num
    pos += 3
    packet_type = int(binary_str[pos:pos+3], 2)
    print('packet_type', packet_type)
    pos += 3
    if packet_type == 4:
        while True:
            if binary_str[pos] == '1': # last packet:
                pos += 5
            else:
                pos += 5
                break
        #pos += (4 - pos) % 4
        return version_count, pos
    else:
        length_type_id = int(binary_str[pos], 2)
        print("length_type_id", length_type_id)
        pos += 1
        if length_type_id == 0:
            # read L now that is 15 bits
            L = int(binary_str[pos:pos+15], 2)
            # dont do anything with the data yet so just skip ahead
            pos += 15
            packet_lengths = pos + L
            while pos < packet_lengths:
                temp_version_count, pos = process_packet(pos, binary_str)
                version_count += temp_version_count
        elif length_type_id == 1:
            print("binary length", len(binary_str[pos:pos+11]))
            print("binary", binary_str[pos:pos+11])
            amount_sub_packets = int(binary_str[pos:pos+11], 2)
            print("amount subpackets", amount_sub_packets)
            pos += 11 
            for i in range(amount_sub_packets):
                temp_version_count, pos = process_packet(pos, binary_str)
                version_count += temp_version_count
        
        return version_count, pos

version_count, pos = process_packet(0, binary_str)
print("pos", pos)
print(version_count)
                
        