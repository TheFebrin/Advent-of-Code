board = [[0 for _ in range(1000)] for _ in range(1000)]

with open('input.txt') as f:
    for line in f:

        cords = line.replace('\n', '')
        index = cords[1: cords.find('@') - 1]
        position = cords[cords.find('@') + 1: cords.find(':')]
        size = cords[cords.find(':') + 2:]

        x_pos = int(position[:position.find(',')])
        y_pos = int(position[position.find(',') + 1:])

        width = int(size[:size.find('x')])
        height = int(size[size.find('x') + 1:])

        for i in range(width):
            for j in range(height):
                board[x_pos + i][y_pos + j] += 1

answer = 0
for i in range(1000):
    for j in range(1000):
        if board[i][j] > 1:
            answer += 1

print(answer)
