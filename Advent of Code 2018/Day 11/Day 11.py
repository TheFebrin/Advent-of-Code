PUZZLE_SERIAL_NUMBER = 2568


def count_power_level(serial_number, x, y):
    rack_ID = x + 10
    power_level_start = rack_ID * y
    power_level_start += serial_number
    power_level_start *= rack_ID
    digit = str(power_level_start)[-3]
    return int(digit) - 5


GRID = [[0 for _ in range(300)] for _ in range(300)]
for i in range(0, 300):
    for j in range(0, 300):
        GRID[i][j] = count_power_level(PUZZLE_SERIAL_NUMBER, i, j)


def find_3_x_3(x, y):
    ans = 0
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            ans += GRID[i][j]
    return ans


largest_power_square = 0
x, y = 0, 0
for i in range(0, 298):
    for j in range(0, 298):
        f = find_3_x_3(i, j)
        if f > largest_power_square:
            largest_power_square = f
            x = i
            y = j

print(largest_power_square)
print('X: {}, Y: {}'.format(x, y))
