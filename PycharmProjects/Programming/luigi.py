a = open("powertoluigi.dat")
b = a.readlines()
l = int(b[0])
for x in range(1, l+1):
    c = b[x].split()
    for y in range(0, len(c)):
        c[y] = c[y].replace("Mario", "Luigi")
    print(c)
