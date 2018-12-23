# Warning!
# It's not the most elegant solution and it takes about 10sec to return answer
# *Open for better ideas

cords = []
SZ = 400  # size of the board
board = [['.' for _ in range(SZ)] for _ in range(SZ)]

# reading input
with open('input.txt') as f:
    index = 0
    for line in f:
        line = line.replace('\n', '')
        x = int(line[:line.find(',')])
        y = int(line[line.find(',') + 2:])

        cords.append((x, y, index))
        index += 1

# puting points on board
for cord in cords:
    board[cord[0]][cord[1]] = chr(cord[2] + 65)

# for each point on board we look for nearest point
for i in range(SZ):
    for j in range(SZ):

        if(board[i][j] != '.'):
            continue

        dist = set()
        two_smallest_dists = []

        for cord in cords:
            act_dist = abs(cord[0] - i) + abs(cord[1] - j)
            dist.add(act_dist)
            two_smallest_dists.append((act_dist, cord[2]))

        two_smallest_dists.sort()

        # if there are no two same smallest distances we put the closest point
        if two_smallest_dists[0][0] != two_smallest_dists[1][0]:
            board[i][j] = str(two_smallest_dists[0][1])


# for b in board:
#     print(b)

# we look for infinite ones
bad_points = set()
for i in range(SZ):
    bad_points.add(board[i][0])
    bad_points.add(board[0][i])
    bad_points.add(board[SZ - 1][i])
    bad_points.add(board[i][SZ - 1])

# now we count finite ones
count = {}

for i in range(1, SZ):
    for j in range(1, SZ):
        if board[i][j] not in bad_points:
            if board[i][j] in count:
                count[board[i][j]] += 1
            else:
                count[board[i][j]] = 1

# we print biggest number of locations closest to some point + this point
print('Largest area: ', max(count.values()) + 1)
