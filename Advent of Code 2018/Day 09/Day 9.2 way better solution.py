# Complexity warning! It can take to 20 sec to run

board = {
    'current': 0,
    'next': None,
    'prev': None
}
board['next'] = board
board['prev'] = board

player_count = 476
last_marble = 7143100
scores = [0] * player_count
player = -1

for i in range(1, last_marble + 1):
    player = (player + 1) % len(scores)

    if i % 23 == 0:
        scores[player] = scores[player] + i
        for j in range(7):
            board = board['prev']
        scores[player] = scores[player] + board['current']
        prv = board['prev']
        nxt = board['next']
        prv['next'] = nxt
        nxt['prev'] = prv
        board = nxt
    else:
        prev = board['next']
        nxt = prev['next']
        board = {
            'current': i,
            'next': nxt,
            'prev': prev
        }
        prev['next'] = board
        nxt['prev'] = board

print(max(scores))
