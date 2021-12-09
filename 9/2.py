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


def va(x, y):
    if x < 0 or x > len(l[0])-1 or y > len(l)-1 or y < 0:
        return 100000

    row = l[y]

    return int(l[y][x])


def ft(x, y, basin, used):
    global key

    if key(x, y) in used:
        return

    used[key(x, y)] = True

    u = va(x, y-1) < 9
    d = va(x, y+1) < 9
    l = va(x-1, y) < 9
    r = va(x+1, y) < 9

    if u:
        k = key(x, y-1)

        if not k in basin:
            basin.append(k)
            ft(x, y-1, basin, used)

    if d:
        k = key(x, y+1)

        if not k in basin:
            basin.append(k)
            ft(x, y+1, basin, used)

    if l:
        k = key(x-1, y)

        if not k in basin:
            basin.append(k)
            ft(x-1, y, basin, used)

    if r:
        k = key(x+1, y)

        if not k in basin:
            basin.append(k)
            ft(x+1, y, basin, used)


def iib(x, y, basins):

    key(x, y)

    for b in basins:
        if key in b:
            return True

    return False


basins = []
used = {}

for y, a in enumerate(l):
    for x, n in enumerate(a):
        n = int(n)

        if n != 9 and not iib(x, y, basins) and not key(x, y) in used:
            basins.append([key(x, y)])
            ft(x, y, basins[-1], used)


basins.sort(key=len)

print("answer: ", len(basins[-1])*len(basins[-2])*len(basins[-3]))
