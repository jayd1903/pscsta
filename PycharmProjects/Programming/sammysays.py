a = open("sammysays.dat")
b = a.readlines()
l=int(b[0].strip())
for x in range(1,l+1):
    if b[x].find("Sammy says") == 0:
        s = b[x].replace("Sammy says", "") #
        print(s.strip())
    else:
        pass

