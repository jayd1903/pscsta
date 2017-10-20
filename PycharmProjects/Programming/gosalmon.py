a = open('salmon.dat')
b = a.readlines()
l=int(b[0].strip())
for x in range(1,l+1):
    z = b[x].split()
    print(z)
    if z[0] == z[1]:
        print("PAIR")
    else:
        print("GO SALMON")




