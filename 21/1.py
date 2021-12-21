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

p1 = 9
p2 = 3

s1 = 0
s2 = 0

turn = 0
d = 0

dr = 0


def id(d):
    global dr
    dr += 1
    d += 1
    d = (d-1) % 100 + 1
    return d


end = 1000
while s1 < end and s2 < end:
    if not turn % 2:
        d = id(d)
        p1 += d

        d = id(d)
        p1 += d

        d = id(d)
        p1 += d

        p1 = (p1-1) % 10 + 1

        s1 += p1

        print("1:", d, p1, s1)

    else:
        d = id(d)

        p2 += d
        d = id(d)
        p2 += d
        d = id(d)
        p2 += d

        p2 = (p2-1) % 10 + 1

        s2 += p2

        print("2:", d, p2, s2)

    turn += 1


print("answer: ", dr)
