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

for i, a in enumerate(l):
    state, b = a.split(' ')

    x, y, z = b.split(',')

    x1, x2 = x.split('=')[1].split('..')
    y1, y2 = y.split('=')[1].split('..')
    z1, z2 = z.split('=')[1].split('..')

    x1 = min(max(int(x1), -50), 50)
    x2 = min(max(int(x2), -50), 50)
    y1 = min(max(int(y1), -50), 50)
    y2 = min(max(int(y2), -50), 50)
    z1 = min(max(int(z1), -50), 50)
    z2 = min(max(int(z2), -50), 50)

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
