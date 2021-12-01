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
prev = 1000000

for i, a in enumerate(l):

    if int(a) > prev:
        ans = ans + 1

    prev = int(a)
    if(False):
        print(i, a)
    pass

print("answer: ", ans)
