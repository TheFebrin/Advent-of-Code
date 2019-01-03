from string import ascii_lowercase

s = ''
with open('input.txt') as f:
    s = f.readline()

# s = 'dabAcCaCBAcCcaDA'

# We simply replace all reactive units in polymer
s_without_reaction = ''
while s_without_reaction != s:
    s_without_reaction = s
    for char in ascii_lowercase:
        s = s.replace(char + char.upper(), '')
        s = s.replace(char.upper() + char, '')

print('Answer:  ', len(s))


# bute force counting, takes some time (about 20 sec) <<-- BAD IDEA
# go = True
# while go:
#     i = 0
#     go = False
#     d = ''

#     while i < len(s):
#         if i + 1 < len(s) and s[i] != s[i + 1] and (s[i] == s[i + 1].lower() or s[i].lower() == s[i + 1]):
#             i += 2
#             go = True
#         else:
#             d += s[i]
#             i += 1

#     s = d

# print(len(s))
# print('end')
