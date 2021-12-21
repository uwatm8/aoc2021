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

p1 = 0
p2 = 0


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


end = 21
while len(configs):
    #print("configs", configs)
    if not len(configs) % 3000:
        print("configs", len(configs))
        print(configs[:1])
    config = configs.pop(0)
    s1, s2, p1, p2, modturn, times = config

    if not modturn:

        """ if s1 > end:
            w1 += times
            continue """

        for dr in drs:
            s1_, s2_, p1_, p2_, modturn_, times_ = config
            p1_ += dr
            p1_ = (p1_-1) % 10 + 1

            s1 += p1_

            if s1 > end:
                w1 += times
                continue

            addConfig(s1, s2, p1, p2, not modturn, times)

    if modturn:
        """ if s2 > end:
            w2 += times

            continue """

        for dr in drs:
            s1, s2, p1, p2, modturn, times = config
            p2 += dr
            p2 = (p2-1) % 10 + 1

            s2 += p2_

            if s2 > end:
                w2 += times
                continue

            addConfig(s1, s2, p1, p2, not modturn, times)


print("answer: ", w1, w2)
