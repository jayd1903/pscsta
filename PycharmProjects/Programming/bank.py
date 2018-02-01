# h is the current command
# i is the string you are modifying
# data values is for multiple data strings, not needed
a = open("bank.dat")
b = a.readlines()
l = int(b[0].strip())
k = int(b[l+1].strip())
data_values = []
for x in range(1,l+1):
    data_values.append(b[x].strip())
for i in data_values:
    for x in range(l+2,l+k+2):
        h = b[x].split()
        if h[0] == "SEARCH":
            print(str(int(str(data_values[0].find(str(h[2]),int(h[1]))))+1))
        elif h[0] == "DELETE":
            m = int(h[1])
            n = int(h[2])
            print(i[:m-1]+i[m+n-1:])
        elif h[0] == "REPLACE":
            n = h[1]
            c = h[2]
            v = list(i)
            v[int(n)-1] = c[0]
            print("".join(v))
        elif h[0] == "INSERT":
            n = int(h[1])
            s = str(h[2])
            print(i[:n-1] + s + " " + i[n-1:])

