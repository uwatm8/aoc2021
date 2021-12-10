import re
filepath = 'data'
dataSuffix = 1
l = []
with open(filepath+str(dataSuffix)) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()

ans = 0


aa = []

for i, a in enumerate(l):

    for j in range(1000):
        a = re.sub(r'\[\]', '', a)
        a = re.sub(r'\<\>', '', a)
        a = re.sub(r'\(\)', '', a)
        a = re.sub(r'\{\}', '', a)

    if a.find(')') != -1 or a.find(']') != -1 or a.find('}') != -1 or a.find('>') != -1:
        pass
    else:

        ans = 0
        for j, na in enumerate(a):
            c = a[-j-1]
            ans *= 5

            if c == '(':
                ans += 1

            elif c == '[':
                ans += 2

            elif c == '{':
                ans += 3

            elif c == '<':
                ans += 4

        if ans:
            aa.append(ans)

            ans = 0

aa.sort()
print("as", aa[len(aa)//2])
