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
ec = True

ot = 10000000000
trying = ot
#     43210987654321
num = 99919764959486
# num = 55555555595555
num = 99999765949499
num = 99919764949591
num = 99919764938488
num = 99999994927488
num = 99919764949498
num = 99977517649252
num = 99999999999999
# num = 99927599999999  # SEP

low = 11111111111111111
#     99999997999999
#     89918667696954 = 16
#     99919764949486 = 8
#     99999764949486 = 450
#     99999785949499 = 462
#     99919764949486 8
#     99919764938488 = 0
#     99919765949497 = 0

# 99919765949497 < ans < 99999765949499
# c1,c2 = 99996482349598

while trying:

    inps = str(num)

    t = []

    for c in inps:
        t.append(int(c))

    # print(t)

    c1 = t[4] - t[5] != 2 and ec
    c2 = t[10] - t[9] != 5 and ec
    #c3 = t[12] // t[11] != 2 and ec

    # print(t[4], t[5], t[4] - t[5])

    if c1:
        num -= 10**8
        continue

    if c2:
        num -= 10**3
        continue

    """ if c3:
        num -= 10
        while '0' in str(num)[11:13]:
            num -= 10
        continue """

    if '0' in inps:
        num -= 1
        continue

    if trying != ot:
        if num % 1000 == 111:
            #print("n1", num)
            num -= 100000
            num += 888
            #print("n2", num)
        else:
            num -= 1

    # print("n", num)

    trying -= 1

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

    if not (trying % 100000):
        # print(num, v['z'])
        print("after", ot-trying,  num, v)

    if v['z'] < low:
        print("LOW", num, v['z'])
        low = v['z']

    # if True or v['z'] < 1000000:
    #    print("after", ot-trying,  num, v['z'])
    if not v['z']:
        print("WIN: ", num, v)
        exit()


print("answer: ", ans)
