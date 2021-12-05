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
out = {}


def addAt(x, y):
    key = str(x)+'.'+str(y)
    if not key in out:
        out[key] = 0
    out[key] += 1


for i, a in enumerate(l):
    xx, yy = a.split(" -> ")
    x1 = int(xx.split(",")[0])
    y1 = int(xx.split(",")[1])
    x2 = int(yy.split(",")[0])
    y2 = int(yy.split(",")[1])

    if x1 == x2:
        sign = 1
        if y1 > y2:
            sign = -1

        for y in range(y1, y2+sign, sign):
            addAt(x1, y)

    elif y1 == y2:

        sign = 1
        if x1 > x2:
            sign = -1

        for x in range(x1, x2+sign, sign):
            addAt(x, y1)

    if(False):
        print(i, a)

for i in out:
    if out[i] > 1:
        ans += 1


print("answer: ", ans)
