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
p = 100000
n1 = 0
n2 = 0
n3 = 0


for i, a2 in enumerate(l):
    a = a2.split(" ")[0]

    n3 = int(n2)
    n2 = int(n1)
    n1 = int(a)
    if n1+n2+n3 > p and i > 2:
        ans = ans + 1

    p = n1+n2+n3
    pass

print("answer: ", ans)
