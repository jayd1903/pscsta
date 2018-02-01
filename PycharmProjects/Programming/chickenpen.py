a = open("chickenpen.in")
b = a.readlines()
l = int(b[0].strip())
f= int(l**0.5)
x = 1
l = f+1 if f**2 < l else f
l += 2
print(l)
print("x"*l)
while x <= l-2:
    print("x%sx" % ("." * (l - 2)))
    x += 1
print("x"*l)