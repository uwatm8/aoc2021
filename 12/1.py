filepath = 'data'
dataSuffix = 1
l = []
with open(filepath+str(dataSuffix)) as fp:
    line = fp.readline()
    while line:
        l.append(line.strip())
        line = fp.readline()
na = len(l)


nn = {}

for i, a in enumerate(l):
    for j, path in enumerate(a.split('-')):
        if not path in nn:
            nn[path] = []

for i, a in enumerate(l):
    for j, path in enumerate(a.split('-')):

        if j:
            ppath = a.split('-')[j-1]

            if not ppath in nn[path]:
                nn[path].append(ppath)

            if not path in nn[ppath]:
                nn[ppath].append(path)

ccpaths = []


def explore(node, visited, cpath):
    visited = dict(visited)

    visited[node] = True
    cpath.append(node)

    if 'end' in visited:
        ccpaths.append(cpath)
    else:
        for i, path in enumerate(nn[node]):
            if path.isupper() or not path in visited:
                explore(path, visited, cpath)


queue = []

node = 'start'
visited = {}
cpath = []

explore('start', visited, cpath)

print("all paths", len(ccpaths))
