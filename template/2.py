filepath = 'data'

dataSuffix = 1

l = []

with open(filepath+str(dataSuffix)) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()
nls = len(l)


ans = 0

for a in l:
    pass;
    
for i in range(nls):
    pass



print("answer: ", ans)
