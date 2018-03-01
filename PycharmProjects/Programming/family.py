def IfRelate(current, destination,visited):
    print(current,destination)
    if current not in d:
        return "not related"
    if destination in d[current]:
        return "related"
    else:
        for h in d[current]:
            if h in visited:
                continue
            visited[h] = 1
            if IfRelate(h, destination, visited) == "related":
                return "related"
        return "not related"
a = open("family.dat")
b = a.readlines()
c = int(b[0])
d = {}
e = int(b[c+1])
for i in range(1,c+1):
    f = b[i].strip().split()
    if f[0] in d:
        d[f[0]].append(f[2])
    else:
        d[f[0]] = [f[2]]
    if f[2] in d:
        d[f[2]].append(f[0])
    else:
        d[f[2]] = [f[0]]
for x in range(c+2,c+e+2):
    k = b[x].strip().split()
    visited = {}
    print(k[0], k[1])
    print(IfRelate(k[0],k[1],visited))