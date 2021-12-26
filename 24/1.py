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

ot = 100000000000000
trying = ot
#     43210987654321
num = 99999764949486

low = 11111111111111111
# 99999997999999
# 89918667696954 = 16
# 99919764949486 = 8
# LOW 99919764949486 8

# ans > 99919764938488

while trying:

    if trying != ot:
        num -= 10000

    trying -= 1
    inps = str(num)

    if '0' in inps:
        continue

    v = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }

    for i, a in enumerate(l):

        a = a.split(' ')

        instruction = a[0]

        # print("___")

        # print("before")

        if instruction == 'inp':
            n1 = a[1]

            v[n1] = int(inps[:1])
            inps = inps[1:]

        if instruction == 'add':
            n1, n2 = a[1], a[2]
            b = n2
            if n2 in v:
                b = v[n2]
            b = int(b)

            v[n1] = int(v[n1])+b

        if instruction == 'mul':
            n1, n2 = a[1], a[2]
            b = n2
            if n2 in v:
                b = v[n2]
            b = int(b)

            v[n1] = int(v[n1])*b

        if instruction == 'div':
            n1, n2 = a[1], a[2]
            b = n2
            if n2 in v:
                b = v[n2]
            b = int(b)

            if int(v[n1])//b < 0:
                v[n1] = (int(v[n1])//b) + 1
            else:
                v[n1] = int(v[n1])//b

        if instruction == 'mod':
            n1, n2 = a[1], a[2]
            b = n2
            if n2 in v:
                b = v[n2]
            b = int(b)

            v[n1] = int(v[n1]) % b

        if instruction == 'eql':
            n1, n2 = a[1], a[2]
            b = n2
            if n2 in v:
                b = v[n2]
            b = int(b)

            if int(v[n1]) == b:
                v[n1] = 1
            else:
                v[n1] = 0

    if not (trying) % 100000:
        print(num, v['z'])

    if v['z'] < low:
        print("LOW", num, v['z'])
        low = v['z']
    # print("after", v)
    if not v['z']:
        print("WIN: ", num, v)
        exit()


print("answer: ", ans)
