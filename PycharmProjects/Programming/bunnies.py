a = open("bunnies.in")
b = a.readlines()
l=int(b[0].strip())
def fibbonaci(num):
    k = []
    for i in range(0,num):
        k.insert(0,i)
for x in range(1,l+1):
    fibbonaci(b[x].strip())