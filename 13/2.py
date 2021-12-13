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

c = []
f = []
cDone = False

fStart = 18

if len(l) > 100:
    fStart = 866


def key(x, y):
    return str(x)+'.'+str(y)


for i, a in enumerate(l):
    if i < fStart:
        x = int(a.split(',')[0])
        y = int(a.split(',')[1])

        c.append([x, y])
    elif i > fStart:
        a.split('fold along ')[1]

        b = a.split('fold along ')[1]

        axis = b.split('=')[0]
        num = int(b.split('=')[1])

        f.append([axis, num])
        pass


print(f)

#f = f[:1]

print(f)

taken = []


for fold in f:
    axis, num = fold

    print("____c:", len(c))

    nc = []
    taken = []

    print("folding", axis, "at", num)
    if axis == 'x':
        for i, p in enumerate(c):

            x, y = p
            if x > num:
                n = [2*num-x, y]

                nx, ny = n

                k = key(nx, ny)

                if not k in taken:
                    nc.append(n)
                    taken.append(k)

            else:
                k = key(x, y)

                if not k in taken:
                    nc.append([x, y])
                    taken.append(key(x, y))

        c = nc

    if axis == 'y':
        for i, p in enumerate(c):
            x, y = p

            if y > num:
                n = [x, 2*num-y]

                #print([x, y], "becomes", n)

                nx, ny = n

                k = key(nx, ny)

                if not k in taken:
                    nc.append(n)
                    taken.append(k)

            else:
                k = key(x, y)

                if not k in taken:
                    nc.append([x, y])
                    taken.append(key(x, y))
        c = nc


for y in range(10):
    row = ''
    for x in range(50):
        if key(x, y) in taken:
            row += '#'
        else:
            row += ' '
    print(row)

print("____c:", len(c))
