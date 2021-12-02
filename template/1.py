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

for i, a in enumerate(l):
    if(False):
        print(i, a)

print("answer: ", ans)
