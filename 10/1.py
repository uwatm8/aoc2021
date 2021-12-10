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


for i, a in enumerate(l):

    for j in range(10000):
        a = re.sub(r'\[\]', '', a)
        a = re.sub(r'\<\>', '', a)
        a = re.sub(r'\(\)', '', a)
        a = re.sub(r'\{\}', '', a)

    for c in a:
        if c.find(')') != -1:
            ans += 3
            print(')', a)
            break

        elif c.find(']') != -1:
            ans += 57
            print(']', a)
            break

        elif c.find('}') != -1:
            ans += 1197
            print('}', a)
            break

        elif c.find('>') != -1:
            ans += 25137
            print('>', a)
            break


print("answer: ", ans)
