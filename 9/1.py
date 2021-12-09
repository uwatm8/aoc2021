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


def va(x, y):
    if x < 0 or x > len(l[0])-1 or y > len(l)-1 or y < 0:
        return 100000

    row = l[y]

    return int(l[y][x])


for i, a in enumerate(l):
    for j, n in enumerate(a):
        n = int(n)

        if n < va(j+1, i) and n < va(j-1, i) and n < va(j, i+1) and n < va(j, i-1):
            ans += n+1


print("answer: ", ans)
