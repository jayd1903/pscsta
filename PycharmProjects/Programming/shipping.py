a = open('shipping.in')
b = a.readlines()
l = int(b[0].strip())
x = 0
n = []
u = 1
f = int(b[1])
while x < l:
    t = int(b[u])
    for i in range(u+1,t+2):
        n.append(b[i].strip())
    x += 1
print(n)
