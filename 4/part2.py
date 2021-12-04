with open('example2.txt') as f:
    lines = f.readlines()
    
numbers = [int(x) for x in lines[0].split(',')]

boards = []
board = [{}, {}, {}, [0,0,0,0,0], [0,0,0,0,0]] # board, row, column, row_count, column_count
row = 0
for line in lines[2:]:
    if line == '\n':
        boards.append(board)
        board = [{}, {}, {}, [0,0,0,0,0], [0,0,0,0,0]]
        row = 0
        continue
    line = line.replace('  ', ' ').replace('\n', '')
    if line[0] == ' ':
        line = line[1:]
    nums = [int(x) for x in line.split(' ')]
    column = 0
    for pos in range(0, 5):
        num = nums[pos]
        board[0][num] = False
        board[1][num] = row # set the number the row matches too
        board[2][num] = column # set the number to the column matches
        
        column += 1
    row += 1
    
boards.append(board)
found = False
last_number = -1
last_board = None

num_boards = len(boards)
board_won = [False] * num_boards
for num in numbers:
    pos = 0
    for board in boards:
        if board_won[pos]:
            pos += 1
            continue
        # first see if the board has the number
        if num in board[0]:
            # has the number
            # get row pos
            row_pos, column_pos = board[1][num], board[2][num]
            board[0][num] = True
            board[3][row_pos] += 1
            board[4][column_pos] += 1
            if board[3][row_pos] == 5: #winner
                board_won[pos] = True
                num_boards -= 1
            elif board[4][column_pos] == 5:
                board_won[pos] = True
                num_boards -= 1
            if num_boards == 0:
                found = True
                last_board = board
                break
        pos += 1
    if found:
        last_number = num
        break

print(last_number)
sum = 0
for key in last_board[0]:
    if not last_board[0][key]:
        sum += key
print(sum)
print(sum*last_number)