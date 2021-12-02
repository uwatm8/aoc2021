from typing import Match


filepath = 'data'

dataSuffix = 1

l = []

with open(filepath+str(dataSuffix)) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

na = len(l)

ans = 0
prev = 1000000

dy = 0
dx = 0

for i, a2 in enumerate(l):
    dir = a2.split(" ")[0]
    dist = int(a2.split(" ")[1])

    if dir == 'forward':
        dy = dy + dist

    if dir == 'down':
        dx = dx + dist

    if dir == 'up':
        dx = dx - dist

    if(False):
        print(i, a)

print("answer: ", dy*dx)
