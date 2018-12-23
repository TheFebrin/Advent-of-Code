from string import ascii_lowercase

s = ''
with open('input.txt') as f:
    s = f.readline()

# s = 'dabAcCaCBAcCcaDA'

# first lets make strings without every type of unit

s = s.replace('\n', '')
polymers = []
for char in ascii_lowercase:
    tmp_s = s.replace(char, '')
    tmp_s = tmp_s.replace(char.upper(), '')
    polymers.append(tmp_s)

# check which polimer is the best
# it takes about 10 sec (let know if you have better idea)
best = 1e10
for poli in polymers:
    poli_without_reaction = ''
    while poli_without_reaction != poli:
        poli_without_reaction = poli
        for char in ascii_lowercase:
            poli = poli.replace(char + char.upper(), '')
            poli = poli.replace(char.upper() + char, '')
    best = min(best, len(poli))

print('Answer:  ', best)
