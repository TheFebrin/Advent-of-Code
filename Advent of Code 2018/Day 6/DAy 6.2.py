# Warning!
# It's not the most elegant solution and it takes about 6sec to return answer
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

# for each point on board we count sum of distances to all of the given points
for i in range(SZ):
    for j in range(SZ):

        act_dist = 0

        for cord in cords:
            act_dist += abs(cord[0] - i) + abs(cord[1] - j)

        #if dist is in our desired range we mark that location
        if act_dist < 10000:
            board[i][j] = '#'

ans = 0
for arr in board:
    for a in arr:
        if a == '#':
            ans += 1

print(ans)
