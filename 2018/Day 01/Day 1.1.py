answer = 0

with open('input.txt') as f:
    for line in f:
        answer += int(line)

print(answer)
