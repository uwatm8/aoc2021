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

for i, a in enumerate(l):
    words = a.split("|")[1].split(" ")

    for word in words:
        print("word", word, len(word))
        if len(word) == 2 or len(word) == 3 or len(word) == 4 or len(word) == 7:
            ans += 1

            print(i, "true", word)

    if(False):
        print(i, a)

print("answer: ", ans)
