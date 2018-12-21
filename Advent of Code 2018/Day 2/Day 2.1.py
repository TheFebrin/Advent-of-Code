from collections import Counter

answer = 1
two = 0
three = 0

with open('input.txt') as f:
    for line in f:
        C = Counter(line)

        is_two, is_three = False, False
        for i in C.values():
            if i == 2:
                is_two = True
            if i == 3:
                is_three = True

        two += is_two
        three += is_three

answer = two * three
print(answer)
