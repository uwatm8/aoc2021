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


def key(a, b, c):
    return str(a)+'.'+str(b)+'.'+str(c)


q = {}

volumes = []

for i, a in enumerate(l):
    state, b = a.split(' ')

    x, y, z = b.split(',')

    x1, x2 = x.split('=')[1].split('..')
    y1, y2 = y.split('=')[1].split('..')
    z1, z2 = z.split('=')[1].split('..')

    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    z1 = int(z1)
    z2 = int(z2)

    for v in volumes:
        pass

    volumes.append(state, x1, x2, y1, y2, z1, z2)

    print("iteration", i)

    if not x1 == x2 and not y1 == y2 and not z1 == z2:
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z in range(z1, z2+1):
                    k = key(x, y, z)
                    if state == 'on':
                        if not k in q:
                            q[k] = True

                            if i > 20:
                                print(k)
                    if state == 'off':
                        if k in q:
                            del q[k]

    print(len(q))


print("answer: ", ans)
