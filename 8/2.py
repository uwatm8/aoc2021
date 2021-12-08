filepath = 'data'
dataSuffix = 1
l = []
with open(filepath+str(dataSuffix)) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()
na = len(l)

tans = 0
ans = 0


for i, a in enumerate(l):
    tw = a.split("|")[0].split(" ")
    words = a.split("|")[1].split(" ")

    pru, prd = [], []
    pm = []
    plu = []

    u = ""
    m = ""
    d = ""
    ru = ""
    dw = ""
    lu = ""
    ld = ""

    for word in tw:
        if len(word) == 2:
            pru = [word[0], word[1]]
            prd = [word[0], word[1]]
            break

    for word in tw:
        if len(word) == 3:
            for letter in word:
                if not letter in pru:
                    u = letter
                    break

    for word in tw:
        if len(word) == 4:
            for letter in word:
                if not letter in pru:
                    plu.append(letter)
                    pm.append(letter)

    socc = []
    for word in tw:
        if len(word) == 6:
            socc.append(word)

    """ print("plu", plu)
    print("pru", pru) """

    ans = 0
    for k, word in enumerate(words):
        j = 4-k

        if len(word) == 5:
            nr = 0
            nlu = 0
            done = 0
            for letter in word:
                # if letter in plu and not letter in pru:
                # is 5
                if letter in plu:
                    nlu += 1

                if letter in pru:
                    nr += 1

            if nr == 1 and nlu == 2:
                ans += 5 * (10**j)

            else:
                if nr == 1:
                    # is 2
                    ans += 2 * 10**j
                    #print("2", j)
                else:
                    # is 3
                    #print("3", j)

                    ans += 3 * 10**j

        if len(word) == 6:
            nm = 0
            nr = 0
            for letter in word:
                if letter in pru:
                    nr += 1
                if letter in pm:
                    nm += 1

            if nm == 1:
                # is 0
                ans += 0 * 10**j
            else:

                if nr == 2:
                    ans += 9 * 10**j
                else:
                    ans += 6 * 10**j

        if len(word) == 2:
            ans += 1 * 10**j

        if len(word) == 3:
            ans += 7 * 10**j

        if len(word) == 4:
            ans += 4 * 10**j

        if len(word) == 7:
            ans += 8 * 10**j

    tans += ans
print("answer: ", tans)
