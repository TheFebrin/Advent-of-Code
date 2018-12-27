import heapq

G = [[] for _ in range(100)]
degree = [0 for _ in range(100)]
all_letters = set()
Q = []
time = 0

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

worker_task = [0 for _ in range(5)]
time_left = [0 for _ in range(5)]
act_workers_working = 0
done = []

while True:
    # print(time)
    tasks = []
    time += 1

    for _ in range(5):
        if Q:
            tasks.append(heapq.heappop(Q))

    worker_index = 0
    for task in tasks:
        while worker_task[worker_index] != 0:
            worker_index += 1

            if worker_index == 5:
                heapq.heappush(Q, task)
                break

        if worker_index == 5:
            continue

        worker_task[worker_index] = task
        time_left[worker_index] = task + 60
        act_workers_working += 1

    if act_workers_working == 0:
        break

    for worker in range(5):
        if time_left[worker] > 0:
            time_left[worker] -= 1

        if time_left[worker] == 0 and worker_task[worker] != 0:
            task_finished = worker_task[worker]
            done.append(task_finished)
            worker_task[worker] = 0
            act_workers_working -= 1

            for w in G[task_finished]:
                degree[w] -= 1
                if degree[w] == 0:
                    heapq.heappush(Q, w)

# print(*[chr(x + 64) for x in done])
print(time - 1)
