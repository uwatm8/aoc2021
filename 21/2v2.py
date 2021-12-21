import math
s1 = 0
s2 = 0

p1 = 4
p2 = 8

w1 = 0
w2 = 0

t = True
times = 1


def key(a, b, c, d, e):
    return str(a)+'.'+str(b)+'.'+str(c)+'.'+str(d)+'.'+str(e)


q = {}
q[key(s1, s2, p1, p2, t)] = [s1, s2, p1, p2, t, times]


def getKeys(dict):
    return [*dict]


drs = [1, 2, 3, 4]

maxd = 0
loops = 0
doubles = 0
end = 21
nw1 = 0
nw2 = 0

while len(q):
    k = getKeys(q)[0]
    a = q[k]
    del q[k]


    s1, s2, p1, p2, t, times = a
    loops += 1


    maxd = max(len(q), maxd)

    for dr in drs:
        s1, s2, p1, p2, t, times = a

        if not t:
            p1 += dr
            s1 += (p1-1) % 10 - 1
        else:
            p2 += dr
            s2 += (p2-1) % 10 - 1


        if s1 > end:
            nw1 += 1
            w1 += times
            continue

        if s2 > end:
            nw2 += 1
            w2 += times
            continue

        k = key(s1, s2, p1, p2, t)

        if k in q:
            oo = q[k]
            aa, b, c, d, e, ot = oo

            q[k] = [s1, s2, p1, p2, not t, times + ot]
            doubles += 1
        else:
            q[k] = [s1, s2, p1, p2, not t, times]


print("loops", loops)
print("doubl", doubles)
print("answer: ", w1, nw1)
print("answer: ", w2, nw2)
print("answer: ", '444356092776315')
print("answer: ", maxd)
