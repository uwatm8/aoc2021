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


def valuePackage(a, s, v):
    # print("VALUE")

    num = ''
    done = False

    while not done:
        n = a[s:s+5]

        num += a[s+1:s+5]
        s += 5
        if n[0] == '0':
            done = True

    return s, b(num)


def operatorPackage(a, s, id):
    vals = []

    global tv

    i = a[s:s+1]
    s += 1

    if b(i) == 1:

        sps = a[s:s+11]
        s += 11

        for j in range(b(sps)):

            s, v, t = header(a, s)

            if b(t) == 4:
                s, num = valuePackage(a, s, v)
                vals.append(num)

            else:
                s, num = operatorPackage(a, s, t)
                vals.append(num)

    if b(i) == 0:

        l = a[s:s+15]
        s += 15

        ends = s + b(l)

        while s < ends:
            s, v, t = header(a, s)

            if b(t) == 4:
                s, num = valuePackage(a, s, v)
                vals.append(num)

            else:
                s, num = operatorPackage(a, s, t)
                vals.append(num)

    print("vals", vals)

    returnVal = 0

    id = b(id)

    if id == 0:
        for item in vals:
            returnVal += item

    if id == 1:
        for j, item in enumerate(vals):
            if not j:
                returnVal = item
            else:
                returnVal *= item

    if id == 2:
        returnVal = 100000000000
        for item in vals:
            if item < returnVal:
                returnVal = item

    if id == 3:
        returnVal = 0
        for item in vals:
            if item > returnVal:
                returnVal = item

    if id == 5:
        v1, v2 = vals
        if v1 > v2:
            returnVal = 1
        else:
            returnVal = 0

    if id == 6:
        v1, v2 = vals
        if v1 < v2:
            returnVal = 1
        else:
            returnVal = 0

    if id == 7:
        v1, v2 = vals
        if v1 == v2:
            returnVal = 1
        else:
            returnVal = 0

    print(id, "RETURN", returnVal)
    return s, returnVal


def header(a, s):
    global tv

    #print("remainder: ", a[s:])

    v = a[s:s+3]
    s += 3

    tv += b(v)

    t = a[s:s+3]
    s += 3
    return s, v, t


def parsePackage(a, s):
    fn = 0

    while s < len(a):

        s, v, t = header(a, s)

        if b(t) == 4:
            s, num = valuePackage(a, s, v)
            fn = num

        else:
            s, num = operatorPackage(a, s, t)
            fn = num

    return s


for i, a in enumerate(l):
    a = ''.join(bin(int(c, 16))[2:].zfill(4) for c in a)

    print(a)

    parsePackage(a, s)


print("answer: ", ans)
