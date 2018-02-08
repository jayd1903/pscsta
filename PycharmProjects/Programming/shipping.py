a = open('shipping.in')
b = a.readlines()
l = len(b)
x = 0
u = 1
for x in range(0,int(b[0])):
    n = []
    total = 0
    t = int(b[u].strip())
    u += 1
    for i in range(0,t):
        n.append(b[u])
        u += 1
    for items in n:
        k = int(items.split()[1])
        q = float(items.split()[2])
        total += k*q
    print(total)