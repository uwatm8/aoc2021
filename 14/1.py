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


for i in range(10):
    replaces = []
    for r in b:
        f, t = r
        m = re.finditer(f, start)

        indexes = [(m.start(0), m.end(0))
                   for m in re.finditer('(?<='+f[0]+')'+f[1], start)]

        for index in indexes:
            begin, end = index

            if f in start:
                replaces.append([begin-1, end, f, f[0]+t+f[1]])

    for j, r in enumerate(sorted(replaces)):
        begin, end, f, t = r

        start = start[:begin+j] + t + start[end+j:]


most = 0
least = 100000


count = {}

for c in start:

    if not c in count:
        count[c] = 1
    else:
        count[c] += 1

print(count)
