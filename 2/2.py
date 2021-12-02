filepath = 'data'
dataSuffix = 1

l = []
with open(filepath+str(dataSuffix)) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

dy = 0
dx = 0
aim = 0

for i, a2 in enumerate(l):
    dir = a2.split(" ")[0]
    dist = int(a2.split(" ")[1])

    if dir == 'forward':
        dy += dist
        dx += dist * aim

    if dir == 'down':
        aim += dist

    if dir == 'up':
        aim -= dist

print("answer: ", dy, dx, dy*dx)
