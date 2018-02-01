a = open('determined1.dat')
b = a.readlines()
l = int(b[0].strip())
for x in range(1, (2 * l) + 1, 2):
    line1 = b[x].split()
    line2=b[x+1].split()
    print((int(line1[0].strip())*int(line2[1].strip())) - (int(line1[1].strip())*int(line2[0].strip())))

