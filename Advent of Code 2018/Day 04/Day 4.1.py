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
guards_whole_time_asleep = [0 for _ in range(5000)]


# main loop
for num, record in enumerate(records):

    year, month, day, hour, minute, action = record

    # new guard begins shift
    if action.find('Guard') != -1:
        act_guard = int(action[action.find('#') + 1: action.find('begins') - 1])

    if action == 'falls asleep':  # if he falls asleep we begin to count
        time_asleep = minute

    if action == 'wakes up':
        guards_whole_time_asleep[act_guard] += minute - time_asleep

        for i in range(time_asleep, minute):  # we count occurencies of every minute
            if i in guards_asleep[act_guard]:
                guards_asleep[act_guard][i] += 1
            else:
                guards_asleep[act_guard][i] = 1


# looking for guard who slept the most

most_minutes = 0
min_of_our_guard = set()
ans_guard = 0

for s in range(len(guards_asleep)):
    if len(guards_asleep[s]) > 0:
        if guards_whole_time_asleep[s] > most_minutes:
            most_minutes = guards_whole_time_asleep[s]
            min_of_our_guard = guards_asleep[s]
            ans_guard = s

print("Guard who slept the most: ", ans_guard, ' slept: ', most_minutes)
print("Answer is : ")

biggest_occur = 0
ans = 0

# we look for minute that occured the most

for minute, occ in min_of_our_guard.items():
    if occ > biggest_occur:
        biggest_occur = occ
        ans = minute

print(ans * ans_guard)
