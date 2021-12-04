import re
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

numbers = []
for a in l[0].split(','):
    numbers.append(int(a))


board = []


for i, a in enumerate(l):
    if not i or len(a) < 4:
        continue

    bi = (i-2) // 6
    bii = (i-2) % 6

    if len(board) < bi + 1:
        board.append([])

    board[bi].append([])

    for num in re.split(' +', a):
        board[bi][bii].append(num)

pickedN = []


for i, n in enumerate(numbers):
    pickedN.append(n)
    if i < 5:
        continue

    for b in board:
        for j in range(5):
            colHit = []
            rowHit = []

            for k in range(5):

                h = int(b[j][k])
                if h in pickedN:
                    rowHit.append(h)

                v = int(b[k][j])
                if v in pickedN:
                    colHit.append(v)

            if(len(rowHit) == 5 or len(colHit) == 5):
                sum = 0
                for x in range(5):
                    for y in range(5):
                        if not int(b[x][y]) in pickedN:
                            sum += int(b[x][y])

                print("BINGO", sum * pickedN[-1])
                exit()
