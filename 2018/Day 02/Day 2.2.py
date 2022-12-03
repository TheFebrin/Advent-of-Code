from collections import Counter

IDs = []
ans1, ans2 = '', ''

with open('input.txt') as f:
    for line in f:
        IDs.append(line.replace('\n', ''))

for box1 in IDs:
    for box2 in IDs:
        if box1 == box2:
            continue

        diff = 0
        for i in range(len(box1)):
            if box1[i] != box2[i]:
                diff += 1

        if diff == 1:
            ans1, ans2 = box1, box2


for i in range(len(ans1)):
    if ans1[i] != ans2[i]:
        print(ans1[:i] + ans1[i + 1:])
        exit()
