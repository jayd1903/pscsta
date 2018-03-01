def final(num):
    z = 0
    for x in range(0,num+1):
        z += layer(x)
    return z
def layer(num):
    n = 0
    for i in range(0,num+1):
        n += i
    return n
a = open("ornaments.dat")
b = a.readlines()
l = int(b[0])
for i in range(1,l+1):
    c = (int(b[i].strip()))
    print(final(c))
