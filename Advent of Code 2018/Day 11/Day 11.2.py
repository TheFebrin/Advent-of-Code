# Takes about 10 sec to run

PUZZLE_SERIAL_NUMBER = 2568
n = 300


def count_power_level(serial_number, x, y):
    rack_ID = x + 10
    power_level_start = rack_ID * y
    power_level_start += serial_number
    power_level_start *= rack_ID
    digit = str(power_level_start)[-3]
    return int(digit) - 5


GRID = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        GRID[i][j] = count_power_level(PUZZLE_SERIAL_NUMBER, i, j)


def count_square(x, y, n):
    whole_square = GRID[x + n - 1][y + n - 1]
    left_sq = 0
    right_sq = 0
    bottom_sq = 0

    if x > 0:
        left_sq = GRID[x - 1][y + n - 1]

    if y > 0:
        right_sq = GRID[x + n - 1][y - 1]

    if x > 0 and y > 0:
        bottom_sq = GRID[x - 1][y - 1]

    return whole_square - left_sq - right_sq + bottom_sq


# we create prefix sum 2D array
for i in range(n):
    for j in range(1, n):
        GRID[i][j] += GRID[i][j - 1]

for i in range(1, n):
    for j in range(n):
        GRID[i][j] += GRID[i - 1][j]


largest_power_square = 0
size = 0
x, y = 0, 0

for k in range(300):
    for i in range(n - k + 1):
        for j in range(n - k + 1):
            act_square = count_square(i, j, k)
            if act_square > largest_power_square:
                largest_power_square = act_square
                x = i
                y = j
                size = k

print(largest_power_square)
print('X: {}, Y: {}, size: {}'.format(x, y, size))
