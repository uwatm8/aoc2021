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


def va(x, y):
    if x < 0 or x > len(vs[0])-1 or y > len(vs)-1 or y < 0:
        return -1

    row = vs[y]

    return int(vs[y][x])


vs = []
flashes = []


def increase(x, y):
    global vs

    if x >= 0 and x <= len(vs[0])-1 and y <= len(vs)-1 and y >= 0:
        vs[y][x] += 1


def ft(x, y):
    global key
    global ans
    global vs

    increase(x, y)

    v = va(x, y)
    if v > 9:
        flashes.append([x, y])
        vs[y][x] = 0
        ans += 1
        for nx in range(-1, 2):
            for ny in range(-1, 2):
                if not [x+nx, y+ny] in flashes:
                    ft(x+nx, y+ny)


for y, a in enumerate(l):
    for x, n in enumerate(a):
        n = int(n)

        if not x:
            vs.append([])
        vs[y].append(n)

for j in range(100):

    noct = len(vs)*len(vs[0])

    for f in flashes:
        vs[f[1]][f[0]] = 0

    flashes = []

    for y, a in enumerate(l):
        for x, n in enumerate(a):
            ft(x, y)


print("answer: ", ans)
