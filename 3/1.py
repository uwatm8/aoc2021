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

for i, a in enumerate(ls):
    for i2, c in enumerate(a):
        key = c+'-'+str(i2)
        if not key in l:
            l[key] = 1
        else:
            l[key] += 1


for i in range(12):
    n0 = 0
    n1 = 0

    if('0-'+str(i) in l):
        n0 = l['0-'+str(i)]
    if('1-'+str(i) in l):
        n1 = l['1-'+str(i)]

    if n0 > n1:
        ans += '0'
    else:
        ans += '1'


bans = bin(eval(ans))
inverted = eval(bans + '^' + ('0b'+'1'*12))
print("answer: ", eval(bans) * inverted)
