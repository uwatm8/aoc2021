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


def explode(x):
    n1, n2 = x

    la = n1
    ra = n2
    print("EXPLODE", n1, n2, la, ra)

    return la, ra


def n(x, depth):
    x1, x2 = x

    la, ra = 0, 0

    n1, n2 = x

    if not isinstance(x1, int):
        nx, lla, rra = n(x1, depth+1)

        nn1, nn2 = nx
        la, ra = lla, rra

        n1 = [nn1, nn2]

    if not isinstance(x2, int):
        nx, lla, rra = n(x2, depth+1)

        nn1, nn2 = nx
        la, ra = lla, rra

        n2 = [nn1, nn2]

    hasExploded = False
    if depth >= 4 and isinstance(x1, list):
        hasExploded = True
        n1, n2 = x
        la, ra = explode(n1)

        n1 = 0
        n2 += ra

        """     if depth >= 4 and isinstance(x2, list):
        hasExploded = True
        n1, n2 = x
        la, ra = explode(n1)

        n2 = 0
        n1 += ra """

    if not hasExploded:
        if isinstance(n1, int):
            n1 += la
            la = 0

        if isinstance(n1, int):
            n2 += ra
            ra = 0

    """ elif depth == 10:
        for ix in x:
            n1, n2 = n(x, depth + 1) """

    print("d", depth, "was", x1, x2, "now", n1, n2)

    return [n1, n2], la, ra


for i, a in enumerate(l):
    print("____")
    p.append(eval(a))

    newp = []

    for ip in p:
        print("final", n(ip, 1))
        # for iip in ip:
        # print(iip)

        # n(iip, 1)
        # print(newp)

print("answer: ", ans)
