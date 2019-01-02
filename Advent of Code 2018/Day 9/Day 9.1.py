examples = []

with open('input.txt') as f:
    for line in f:
        examples.append(line[:-1])


def solve(example):
    # lets make our marble circle
    marbles = [0, 1]
    last_pos = 1

    number_of_players = int(example[:3])
    number_of_marbles = int(example[34:39])
    player_score = [0 for _ in range(number_of_players + 1)]
    act_size = 2
    act_player = 1

    for marble in range(2, number_of_marbles + 1):
        act_player += 1
        if act_player > number_of_players:
            act_player = 1

        if marble % 23 == 0:  # magic shit happens
            player_score[act_player] += marble
            last_pos -= 7

            if last_pos < 0:
                last_pos += act_size

            player_score[act_player] += marbles[last_pos]
            del marbles[last_pos]
            act_size -= 1

        else:
            last_pos += 1
            last_pos %= act_size

            last_pos += 1
            marbles.insert(last_pos, marble)
            act_size += 1

        # print(marbles)
    # print(player_score)
    print("Players: {}, marbles: {}".format(number_of_players, number_of_marbles))
    print('Best score using my algo was ---> {} \n'.format(max(player_score)))


# solve(examples[0])
for example in examples:
    print(example)
    solve(example)
