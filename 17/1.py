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

x = 0
y = 0

vx, vy = 0, 0

x1 = 0
x2 = 0
y1 = 0
y2 = 0

for i, a in enumerate(l):
    b = a.split('target area: x=')[1]

    bx, by = b.split(', y=')

    x1, x2 = bx.split("..")
    y1, y2 = by.split("..")

    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    print(x1, x2, y1, y2)


triesX = x2
triesY = 10000
steps = 1000

maxy = 0

avgX = (x1+x2)/2


vx0 = avgX * math.ceil(avgX)

print("vx0", vx0)

for ix in range(triesX):
    for iy in range(triesY):

        x = 0
        y = 0
        vx = ix
        vy = iy
        maxyRun = 0
        for s in range(steps):
            if x1 <= x <= x2:
                if y1 <= y <= y2:
                    # print("DONE", s, -(tries/2) + ix, -(tries/2) + iy, maxy)
                    if maxyRun > maxy:
                        print("NEW MAX", maxyRun)
                        maxy = maxyRun

            x += vx
            y += vy

            if y > maxyRun:
                maxyRun = y

            if vx > 0:
                vx -= 1

            if vx < 0:
                vx += 1

            vy -= 1

            if vx == 0 and x1 > x or y < y1:
                break
