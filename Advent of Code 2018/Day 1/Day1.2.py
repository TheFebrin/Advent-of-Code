answer = 0
S = set()

with open('input.txt') as f:
    while True:
        f.seek(0)

        for line in f:
            answer += int(line)

            if answer in S:
                print(answer)
                exit()
            S.add(answer)
