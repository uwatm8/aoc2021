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

    if str(x) not in ps:
        print("NOT INCLUDED", depth)
        return x, ps

    nums = re.findall('[0-9]{2}', ps)

    for number in nums:
        number = int(number)
        if number > 10:

            p1 = number // 2
            p2 = math.ceil(number / 2)

            print("NUMBER SPLiT", number, p1, p2)

            ps = ps.replace(str(number), '['+str(p1)+', '+str(p2)+']')

            return x, ps

    if depth >= 4 and isinstance(x1, list):

        lx1, rx1 = x1
        ls, rs = ps.split(str(x1))

        w = re.findall('[0-9]+', ls)
        if len(w):
            last_char_index = ls.rfind(w[-1])

            ls = ls[:last_char_index]+ls[last_char_index:].replace(
                str(w[-1]), str(int(w[-1]) + lx1), 1)

        w2 = re.findall('[0-9]+', rs)

        if len(w2):
            rs = rs.replace(str(w2[0]), str(int(w2[0]) + rx1), 1)

        ps = ls+'0'+rs

        return x, ps

    elif depth >= 4 and isinstance(x2, list):

        lx1, rx1 = x2

        ls, rs = ps.split(str(x2))

        w = re.findall('[0-9]+', ls)
        if len(w):
            last_char_index = ls.rfind(w[-1])

            ls = ls[:last_char_index]+ls[last_char_index:].replace(
                str(w[-1]), str(int(w[-1]) + lx1), 1)

        w2 = re.findall('[0-9]+', rs)
        if len(w2):
            rs = rs.replace(str(w2[0]), str(int(w2[0]) + rx1), 1)

        ps = ls+'0'+rs

        return x, ps

    if isinstance(x1, list):
        x, ps = n([x1, ps], depth+1)

    if isinstance(x2, list):
        x, ps = n([x2, ps], depth+1)

    return x, ps


a = []
for i, b in enumerate(l):
    print(i, b)
    if not len(a):
        a = eval(b)
    else:
        a = [a, eval(b)]

a = str(a)

print("____")
a = str(eval(a))
p.append([eval(a), a])

newp = []

for ip in p:
    x, ps = ip
    for i in range(10):
        _, ps = n(ip, 1)
        ip = [eval(ps), ps]

        print("final", ps)
    print("final", ps)


print("answer: ", ans)
