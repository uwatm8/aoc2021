import re
import math
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

p = []


def n(p, depth):
    x, ps = p
    x1, x2 = x

    #print("enter", x)

    if str(x) not in ps:
        return x, ps

    nums = re.findall('[0-9]{2}', ps)

    for number in nums:
        number = int(number)
        print(number)
        if number >= 10:
            # print("SPLIT")

            p1 = number // 2
            p2 = math.ceil(number / 2)

            ps = ps.replace(str(number), '['+str(p1)+', '+str(p2)+']')

            return x, ps

    if depth >= 4 and isinstance(x1, list):
        #print("EXPLODE 1")

        lx, rx = x1

        ls, rs = ps.split(str(x1))[:2]

        #print("AAA", x)

        if isinstance(lx, list):
            ww = eval('['+str(lx)+', '+str(rx)+']')
            print("SPECIAL 1", ww)
            x, ps = n([ww, ps], depth+1)

            return x, ps

        if isinstance(rx, list):
            ww = eval('['+str(lx)+', '+str(rx)+']')
            print("SPECIAL 2", ww)
            x, ps = n([ww, ps], depth+1)

        w = re.findall('[0-9]+', ls)
        if len(w):
            last_char_index = ls.rfind(w[-1])

            ls = ls[:last_char_index]+ls[last_char_index:].replace(
                str(w[-1]), str(int(w[-1]) + lx), 1)

        w2 = re.findall('[0-9]+', rs)

        if len(w2):
            rs = rs.replace(str(w2[0]), str(int(w2[0]) + rx), 1)

        ps = ls+'0'+rs

        return x, ps

    elif depth >= 4 and isinstance(x2, list):
        #print("EXPLODE 2")

        ls, rs = ps.split(str(x2))[:2]

        lx, rx = x2

        #print("BBB", x)
        if isinstance(lx, list):
            ww = eval('['+str(lx)+', '+str(rx)+']')
            print("SPECIAL 3", ww)
            x, ps = n([ww, ps], depth+1)

            return '@', ps

        if isinstance(rx, list):
            ww = eval('['+str(lx)+', '+str(rx)+']')
            print("SPECIAL 4", ww)
            x, ps = n([ww, ps], depth+1)

            return '@', ps

        # print(len(ps.split(str(x2))))

        # print(ps.split(ls+x2+rs)[1])
        # print("4", ls+str(x2)+rs + ps.split(ls+str(x2)+rs)[1] == ps)

       # print(ls+str(x2)+rs)

        rs += ps.split(ls+str(x2)+rs)[1]
        # print('1', ls+str(x2)+rs == ps)

        w = re.findall('[0-9]+', ls)
        if len(w):
            last_char_index = ls.rfind(w[-1])

            # print("___")
            # print(lx)
            # print("_", str(w[-1]), str(int(w[-1])))

            ls = ls[: last_char_index]+ls[last_char_index:].replace(
                str(w[-1]), str(int(w[-1]) + lx), 1)

        w2 = re.findall('[0-9]+', rs)
        if len(w2):
            rs = rs.replace(str(w2[0]), str(int(w2[0]) + rx), 1)

        ps = ls+'0'+rs

        return x, ps

    if isinstance(x1, list):
        x, ps = n([x1, ps], depth+1)

    if isinstance(x2, list):
        x, ps = n([x2, ps], depth+1)

    # print("RETURNING")
    return x, ps


a = []
for i, b in enumerate(l):
    print(i, b)
    if not len(a):
        a = eval(b)
    else:
        a = [a, eval(b)]

a = str(a)

print("____", a.replace(' ', ''))
a = str(eval(a))
p.append([eval(a), a])

newp = []

for ip in p:
    x, ps = ip
    now = ps
    previous = ''
    while ps != previous:
        _, ps = n(ip, 1)
        ip = [eval(ps), ps]

        print(ps)

        previous = now
        now = ps
