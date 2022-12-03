INITIAL_STATE = []
INITIAL_NOTES = []

with open('input.txt') as f:
    INITIAL_STATE = [x for x in f.readline()[15:-1]]
    next(f)

    for note in f.readlines():
        INITIAL_NOTES.append(note.replace('\n', ''))


STATE = ['.'] * 50 + INITIAL_STATE + ['.'] * 1000
first_plant = ''.join(STATE).find('#')

NOTES = {}
for note in INITIAL_NOTES:
    NOTES[note[:5]] = note[-1]


def solve(generations, STATE):
    for gen in range(generations):
        ptr = 0

        NEW_STATE = ['.'] * len(STATE)

        while ptr + 4 < len(STATE):
            act_batch = ''.join(STATE[ptr:ptr + 5])

            if act_batch in NOTES:
                NEW_STATE[ptr + 2] = NOTES[act_batch]

            ptr += 1

        STATE = NEW_STATE

    answer = 0
    after_gen_first_plant = ''.join(STATE).find('#')
    plant_shift = after_gen_first_plant - first_plant + 1  # + 1 is to make puzzle input work

    for plant_nr in STATE:
        if plant_nr == '#':
            answer += plant_shift - after_gen_first_plant

        plant_shift += 1

    return(answer)


# PART 1
print('Part 1', solve(20, STATE))
# PART 2
score199 = solve(199, STATE)
score200 = solve(200, STATE)
constantIncrease = score200 - score199
print('Part 2:', solve(200, STATE) + ((50000000000 - 200) * constantIncrease))
