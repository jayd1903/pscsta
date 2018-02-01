a = open("histonum.dat")
b = a.readlines()
l = len(b)
h = {}
for x in range(0,l):
    z = b[x].strip()
    c = len(z)
    for i in range(0,c):
        if z[i] in h.keys():
            h[z[i]]+=1
        else:
            h[z[i]] = 1
    for v in range(1,10):
        if str(v) in h.keys():
            print(h[str(v)])
        else:
            pass
