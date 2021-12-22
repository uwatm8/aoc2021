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

b = ''

f = []

def key(x,y):
    return str(x)+'.'+str(y)


def va(x,y):
    if x < 0 or x >= len(f) or y < 0 or y >= len(f):
        return 0
    return f[y][x] == '#'

for i, a in enumerate(l):
    if i == 0:
        b = a
    elif i == 1:
        continue
    else:
        f.append(a)


def bva(x,y):
    index = 0
    i = 0
    for iy in range(-1,2):
        for ix in range(-1,2):
            iiy = -iy
            iix = -ix

            v = va(iix+x,iiy+y)

            if v:
                index += 2**i
            i+=1



    return b[index] == '#'



q={}


def printq(i):
    for iy in range(-i, len(f)+i):
        row = ''
        for ix in range(-i, len(f)+i):
            k = key(iy,ix)
            if k in q:
                row += '#'
            else:
                row += '.'
        print(row)     

for row in f:
    print(row)

m = 7
for i in range(50):
    ans = 0
    print("_____________")
    nf = []

    for iy in range(-m,len(f)+m):
        row = ''
        for ix in range(-m,len(f)+m):

            if bva(ix,iy):

                row += '#'
                ans += 1

            else: 
                row += '.'
        nf.append(row)

    f = nf

    ans = 0
    l = len(f)

    ll = 8
    if True:
        if i %2:
            for y in range(l):
                row = ''
                for x in range(l):
                    if x < ll or x >= l-ll-1 or y < ll or y >= l-ll-1:
                        row += '.'
                    else: 
                        row += f[y][x]

                        if f[y][x] == '#':
                            ans += 1

                f[y] = row
                print(row)
        print(ans)

    """ for row in f:
        print(row) """







""" for row in f:
    print(row) """

print(ans)
    
