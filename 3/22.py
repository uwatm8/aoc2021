filepath = 'data'
dataSuffix = 1
ls = []
with open(filepath+str(dataSuffix)) as fp:
    line = fp.readline()
    while line:
        ls.append(line.strip())
        line = fp.readline()
na = len(ls)

ans = "0b"

l = {}


prefix = ""

for i, a in enumerate(ls):

    for i2, c in enumerate(a):
        key = c+'-'+str(i2)

        if not key in l:
            l[key] = 1
            print(l)

        else:
            l[key] += 1
            print(l)

    n0 = 0
    n1 = 0

    if('0-'+str(i) in l):
        n0 = l['0-'+str(i)]

    if('1-'+str(i) in l):
        n1 = l['1-'+str(i)]

    newl = []

    if n1 >= n0:
        prefix += "1"
    else:
        prefix += "0"

    for a2 in l:
        if(a.startswith(prefix)):
            newl.append(a)

    a = newl

for i in range(12):
    n0 = 0
    n1 = 0

    if('0-'+str(i) in l):
        n0 = l['0-'+str(i)]

    if('1-'+str(i) in l):
        n1 = l['1-'+str(i)]

    print(n0, n1)

    if n0 > n1:
        ans += '0'
    else:
        ans += '1'


print("answer: ", ans)