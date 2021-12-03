filepath = 'data'
dataSuffix = 1
ls = []
with open(filepath+str(dataSuffix)) as fp:
    line = fp.readline()
    while line:
        ls.append(line.strip())
        line = fp.readline()
na = len(ls)

ols = ls

ans = "0b"

l = {}


prefix = ""
n1 = 0
n0 = 0

for j in range(len(ls[0])):
    n1 = 0
    n0 = 0

    a0 = []
    a1 = []

    for a in ls:
        if a.startswith(prefix+'0'):
            n0 += 1
            a0.append(a)
        else:
            n1 += 1
            a1.append(a)

    if n1 >= n0:
        prefix += '1'
        ls = a1
    else:
        prefix += '0'
        ls = a0

print(prefix)

f1 = prefix

ls = ols

prefix = ""

for j in range(len(ls[0])):
    n1 = 0
    n0 = 0

    a0 = []
    a1 = []

    for a in ls:
        if a.startswith(prefix+'0'):
            n0 += 1
            a0.append(a)
        else:
            n1 += 1
            a1.append(a)

    if len(ls) != 1:
        if n1 < n0:
            prefix += '1'
            ls = a1
        else:
            prefix += '0'
            ls = a0
    else:
        prefix += ls[0][j]

    print(ls, n0, n1)

print(prefix)

f2 = prefix

print("answer: ", f1, f2)
