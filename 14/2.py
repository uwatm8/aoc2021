import re
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

start = ""

b = []


for i, a in enumerate(l):
    if i == 0:
        start = a

    if i > 1:

        f, t = a.split(' -> ')

        b.append([f, t])

sa = {}


def addSA(key, n):
    if not key in sa:
        sa[key] = n
    else:
        sa[key] += n


def removeSA(key):
    sa.pop(key, None)


for i in range(len(start)-1):
    sub = start[i:i+2]
    addSA(sub, 1)


for i in range(40):
    additions = []
    for r in b:
        f, t = r

        osa = dict(sa)

        for item in osa:

            if item == f:
                ic = item[:]

                after = ic.replace(f, f[0]+t+f[1])
                sub1 = after[1:]
                sub2 = after[:-1]

                timesExisting = sa[item]

                additions.append([sub1, timesExisting])
                additions.append([sub2, timesExisting])
                removeSA(item)

    for add in additions:
        key, n = add

        addSA(key, n)


most = 0
least = 100000000000000


count = {}


for s in sa:
    key = s[0]
    if not key in count:
        count[key] = 0
    count[key] += sa[s]

count[start[-1:]] += 1

for c in count:
    val = count[c]
    print(val)
    if val > most:
        most = val

    if val < least:
        least = val


print(count)
print("count", most-least)
