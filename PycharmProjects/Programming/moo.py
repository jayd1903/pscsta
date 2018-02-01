a = open("cowspeak.in")
b = a.readlines()
l = int(b[0].strip())
for x in range(1,l+1):
    m=b[x].split()
    qq =[]
    for i in m:
        num_m = 0
        num_o = 0
        second_num = 0
        for k in i:
            if k.upper() == "M":
                num_m += 1
            else:
                num_o += 1
        j = hex(num_o)
        s = hex(num_m)
        u = str(s) + str(j)[2:]
        q = int(u,16)
        qq.append(chr(q))
    print(''.join(qq))