a = open('clockpaperscissors.dat')
b = a.readlines()
l=int(b[0].strip())
for x in range(1,l+1):
    z = b[x].split()
    if int(z[0]) + int(z[1]) + int(z[2])>1: #hi
        print("Player 1")
    else:
        print("Player 2")

