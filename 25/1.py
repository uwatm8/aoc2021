import copy
filepath = 'data'
dataSuffix = 1
l = []
with open(filepath+str(dataSuffix)) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()
ny = len(l)
nx = len(l[0])

print(ny, nx)

ans = 0
r = []


def va(x, y, r):

    return r[y % (ny)][x % (nx)]


def sv(x, y, val, arr):

    arr[y % (ny)][x % (nx)] = val


for i, a in enumerate(l):
    r.append([c for c in a])


for row in r:
    print(row)


moving = True

nr = copy.deepcopy(r)


def printBoard(x):
    print('_______')

    for row in x:
        rw = ''
        for c in row:
            rw += c
        print(rw)


while moving:
    ans += 1

    nr = copy.deepcopy(r)

    for y in range(ny):
        for x in range(nx):
            if va(x, y, r) == '>':
                rv = va(x+1, y, r)
                if rv == '.':
                    sv(x+1, y, '>', nr)
                    sv(x, y, '.', nr)

    mr = copy.deepcopy(nr)

    for y in range(ny):
        for x in range(nx):
            if va(x, y, mr) == 'v':
                uv = va(x, y+1, mr)
                if uv == '.':
                    sv(x, y+1, 'v', nr)
                    sv(x, y, '.', nr)

    if r == nr or ans > 40000:
        moving = False

    r = nr

    print(ans)
    printBoard(r)

printBoard(r)


print("answer: ", ans)
