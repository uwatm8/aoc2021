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

ss = 5

s = 0


def b(x):
    return int(bin(eval('0b'+x)), 2)


tv = 0


def valuePackage(a, s):

    num = ''
    done = False

    while not done:
        n = a[s:s+5]

        num += a[s+1:s+5]
        s += 5
        if n[0] == '0':
            done = True

    return s, num


def operatorPackage(a, s):
    global tv

    i = a[s:s+1]
    s += 1

    if b(i) == 1:

        sps = a[s:s+11]
        s += 11

        for j in range(b(sps)):

            s, v, t = header(a, s)

            if b(t) == 4:
                s, num = valuePackage(a, s)

            else:
                s = operatorPackage(a, s)

    if b(i) == 0:

        l = a[s:s+15]
        s += 15

        ends = s + b(l)

        while s < ends:
            s, v, t = header(a, s)

            if b(t) == 4:
                s, num = valuePackage(a, s)

            else:
                s = operatorPackage(a, s)

    return s


def header(a, s):
    global tv

    v = a[s:s+3]
    s += 3

    tv += b(v)

    print("tv", tv)

    t = a[s:s+3]
    s += 3
    return s, v, t


def parsePackage(a, s):
    while s < len(a):

        s, v, t = header(a, s)

        if b(t) == 4:
            s, num = valuePackage(a, s)

        else:
            s = operatorPackage(a, s)

    return s


for i, a in enumerate(l):
    a = ''.join(bin(int(c, 16))[2:].zfill(4) for c in a)

    parsePackage(a, s)


print("answer: ", ans)
