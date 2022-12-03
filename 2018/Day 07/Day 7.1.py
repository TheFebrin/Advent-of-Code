import heapq

# It is basically topsorting

G = [[] for _ in range(100)]
degree = [0 for _ in range(100)]
all_letters = set()
Q = []
answer = []

# Filling up our graph (we will convert letters to numbers to make it easier)
# We should use priority queue, (heapq)

with open('input.txt') as f:
    for line in f:
        line = line.replace('\n', '')

        parent_node = line[5]
        child_node = line[36]

        parent_node = ord(line[5]) - 64
        child_node = ord(line[36]) - 64

        G[parent_node].append(child_node)
        degree[child_node] += 1

        all_letters.add(parent_node)
        all_letters.add(child_node)

for node in range(30):
    if degree[node] == 0 and node in all_letters:
        heapq.heappush(Q, node)

while Q:
    top = heapq.heappop(Q)

    for node in G[top]:
        degree[node] -= 1
        if degree[node] == 0:
            heapq.heappush(Q, node)

    print(chr(top + 64), end='')

print()
