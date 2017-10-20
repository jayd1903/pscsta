a = open("redlight.dat")
b = a.readlines()
l = int(b[0])
for x in range(1, l+1):
    c = b[x].split()
    print(str(float(c[0])* float(c[1])))

