f1 = input()
f2 = input()

f1 = f1.split(' ')
a = int(f1[0])
b = int(f1[1])
c = int(f1[2])
d = int(f1[3])
f2 = f2.split(' ')
A = int(f2[0])
B = int(f2[1])
C = int(f2[2])
D = int(f2[3])

if (a == c and b == d):
    if b == ((B - D)*a  + (A*D - B*C))/(C - A):
        print(1)
    else:
        print(0)
elif (A == C and B == D):
    if B == ((b - d)*A  + (a*d - b*c))/(c - a):
        print(1)
    else:
        print(0)
else:
    try:
        X = (-a*A*D + a*B*C  + A*c*D - B*c*C + a*A*d - a*C*d - A*b*c + b*c*C)/(-A*b + A*d + b*C - C*d + a*B + c*D - B*c - a*D)
        print(1)
    except: 
        print(0)

# w = open('output2.txt', 'w+')
 
# w.write(str(result))
