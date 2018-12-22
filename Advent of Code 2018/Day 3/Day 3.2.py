
def intersect(r1, r2):
    Ax, Ay, w1, h1 = r1[1], r1[2], r1[3], r1[4]
    Bx, By, w2, h2 = r2[1], r2[2], r2[3], r2[4]

    A2x, A2y = Ax + w1, Ay + h1
    B2x, B2y = Bx + w2, By + h2

    # Point A is top left corner, A2 is bottom right corner
    # vice versa with B

    # print(Ax, Ay, ' - ', A2x, A2y)
    # print(Bx, By, ' - ', B2x, B2y, '\n')

    if Ay >= B2y or By >= A2y:  # checking when they do not intersect
        return False

    if Bx >= A2x or Ax >= B2x:
        return False

    return True


rectangles = []

with open('input.txt') as f:
    for line in f:

        cords = line.replace('\n', '')
        index = int(cords[1: cords.find('@') - 1])
        position = cords[cords.find('@') + 1: cords.find(':')]
        size = cords[cords.find(':') + 2:]

        x_pos = int(position[:position.find(',')])
        y_pos = int(position[position.find(',') + 1:])

        width = int(size[:size.find('x')])
        height = int(size[size.find('x') + 1:])

        rectangles.append((index, x_pos, y_pos, width, height))

n = len(rectangles)
good_rectangles = [True for _ in range(len(rectangles) + 1)]

for r1 in range(n):
    for r2 in range(r1 + 1, n):

        if intersect(rectangles[r1], rectangles[r2]):
            good_rectangles[rectangles[r1][0]] = False
            good_rectangles[rectangles[r2][0]] = False


for i, rect in enumerate(good_rectangles):
    if rect and i > 0:
        print("Number : ", i)
