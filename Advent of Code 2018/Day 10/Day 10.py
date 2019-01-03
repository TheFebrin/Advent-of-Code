import matplotlib.pyplot as plt
import numpy as np
import re

with open('input.txt') as f:

    lines = f.readlines()
    lines = [[int(i) for i in re.findall(r'-?\d+', l)] for l in lines]

data = np.array(lines, dtype=np.float32)
p = data[:, :2]
v = data[:, 2:]

px = p[:, 0]
vx = v[:, 0]

mu = np.mean(px)
ev = np.mean(vx)
t = np.mean((mu - px) / (vx - ev))

t = int(round(t))

print('Number of seconds needed: {}'.format(t))


plt.plot(*(p + t * v).T, ls='', marker='o', color='b')
plt.gca().invert_yaxis()
plt.axis('equal')
plt.show()
