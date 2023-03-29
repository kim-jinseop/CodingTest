from sys import stdin

def gcd(a,b) :
    while b>0 :
        a,b = b,a%b
    return a

n = int(stdin.readline())

M = 0
minb = 0
bb = 0
g = 0

for _ in range(n) :
    a, b = map(int,stdin.readline().split())
    if a+bb < 0 :
        minb = max(minb, b) 
        M = b - bb - a
        g = gcd(M,g)

        if g <= minb:
            g = -1
            break

    elif b - a != bb :
        g = -1
        break

    bb = b

print(g if g else 1)