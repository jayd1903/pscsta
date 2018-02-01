a = open("drought.dat")
b = a.readlines()
l = int(b[0].strip())
for x in range(1,l+1):
    z = b[x].split()
    average = float(z[0])
    sum_one = 0
    sum_two = 0
    for i in range(1,13):
        sum_one += float(z[i])
    for i in range(13,25):
        sum_two += float(z[i])
    if sum_one > (average*2) and sum_two > (average*2):
        print("drought over")
    elif sum_one >= average and sum_two >= average:
        print("improving")
    else:
        print("continuing")
