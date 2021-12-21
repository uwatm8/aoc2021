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

p1 = 4
p2 = 8


drs = [1, 2, 3]


def key(s1, s2, p1, p2, turn):
    return str(s1)+'.'+str(s2)+'.'+str(p1)+'.'+str(p2)+'.'+str(turn)


start = [0, 0, p1, p2, False, 1]
configs = [start]
qe = {}
qe[key(0, 0, p1, p2, False)] = 1

w1, w2 = 0, 0


def addConfig(s1, s2, p1, p2, modturn, times):
    k = key(s1, s2, p1, p2, modturn)
    if not k in qe:
        qe[k] = times
        configs.append([s1, s2, p1, p2, modturn, times])
    else:
        ot = qe[k]
        del qe[k]
        configs.append([s1, s2, p1, p2, modturn, times+ot])
        qe[k] = ot + times


maxd = 0
end = 21
loops = 0
while len(configs):
    loops += 1
    config = configs.pop(0)
    a, b, c, d, modturn, times = config.copy()
    del qe[key]

    maxd = max(len(configs), maxd)

    if not modturn:
        for dr in drs:
            s1, s2, p1, p2, modturn_, times_ = config.copy()
            p1 += dr
            p1 = (p1-1) % 10 + 1

            s1 += p1

            if s1 > end:
                w1 += times
            else:
                addConfig(s1, s2, p1, p2, not modturn, times)

    if modturn:
        for dr in drs:
            s1, s2, p1, p2, modturn_, times_ = config.copy()
            p2 += dr
            p2 = (p2-1) % 10 + 1

            s2 += p2

            if s2 > end:
                w2 += times
            else:
                addConfig(s1, s2, p1, p2, not modturn, times)

for q in qe:
    print(q, qe[q])

print("loops", loops)
print("qe", len(qe))
print("answer: ", w1)
print("answer: ", w2)
print("answer: ", '444356092776315')
print("answer: ", maxd)
