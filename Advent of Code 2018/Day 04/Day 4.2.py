def parse(line):
    year, month, day, hour, minute, action = '', '', '', '', '', ''

    year = line[1:5]
    month = line[6:8]
    day = line[9:11]
    hour = line[12:14]
    minute = line[15:17]
    action = line[line.find(']') + 2:]

    year, month, day, hour, minute = map(int, (year, month, day, hour, minute))
    return (year, month, day, hour, minute, action)


# Solving task-------------------------------------------------------

records = []

# Filling up records
with open('input.txt') as f:
    for line in f:
        records.append(parse(line.replace('\n', '')))

# sorting records chronologically
records.sort()

# variables
act_guard, time_asleep = 0, 0
guards_asleep = [{} for _ in range(5000)]

# main loop
for num, record in enumerate(records):

    year, month, day, hour, minute, action = record

    # new guard begins shift
    if action.find('Guard') != -1:
        act_guard = int(action[action.find('#') + 1: action.find('begins') - 1])

    if action == 'falls asleep':  # if he falls asleep we begin to count
        time_asleep = minute

    if action == 'wakes up':
        for i in range(time_asleep, minute):  # we count occurencies of every minute
            if i in guards_asleep[act_guard]:
                guards_asleep[act_guard][i] += 1
            else:
                guards_asleep[act_guard][i] = 1


# looking for guard
biggest = 0
ans_minute = 0
ans_guard = 0

for guard, dict in enumerate(guards_asleep):
    for minn, occur in dict.items():
        if occur > biggest:
            biggest = occur
            ans_minute = minn
            ans_guard = guard

print(ans_minute * ans_guard)
