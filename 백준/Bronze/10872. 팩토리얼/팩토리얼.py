import sys

n = int(sys.stdin.readline())
fac = 1

for i in range(1,n+1) :
    fac = fac * i

print(fac)