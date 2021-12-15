import random
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


def key(x, y):
    return str(x)+'.'+str(y)


e = []
m = []


for i, a in enumerate(l):
    for j, c in enumerate(a):
        c = int(c)

        if not j:
            e.append([])

        e[i].append(c)

hl, wl = len(l), len(l[0])

for i in range(hl):
    m.append([])
    m.append([])
    m.append([])
    m.append([])
    m.append([])

for ix in range(5):
    for iy in range(5):
        for x in range(wl):
            for y in range(hl):
                add = ix+iy

                nx = x + wl*ix
                ny = y + hl*iy

                val = e[y][x] + add

                while val > 9:
                    val -= 9

                if val == 0:
                    val = 1

                m[ny].append(val)


h, w = len(m), len(m[0])

minScore = 1000000


def valAt(x, y):
    if x >= 0 and y >= 0 and x < w and y < h:
        return m[y][x]

    return 10


dangerTo = {'0.0': 0}


def n(x, y):

    vals = [[valAt(x+1, y), x+1, y], [valAt(x, y+1), x, y+1],
            [valAt(x-1, y), x-1, y], [valAt(x, y-1), x, y-1]]

    cv = []
    for v in vals:
        if v[0] != 10:
            cv.append(v)

    return sorted(cv)


q = []
qe = {}

ns = n(0, 0)

for neighbour in ns:
    q.append(neighbour)

while len(q):
    closest = q[0]
    del q[0]

    danger, x, y = closest

    if key(x, y) in qe:
        del qe[key(x, y)]

    if not key(x, y) in dangerTo:
        dangerTo[key(x, y)] = danger

    ns = n(x, y)

    for neighbour in ns:
        danger, nx, ny = neighbour

        if key(nx, ny) not in dangerTo:

            if not key(nx, ny) in qe:
                q.append([danger + dangerTo[key(x, y)], nx, ny])
                qe[key(nx, ny)] = True

        q = sorted(q)


print("answer: ", dangerTo[key(499, 499)])
