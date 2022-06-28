import sys

x = []
y = []
for i in range(3) :
    a,b = map(int,sys.stdin.readline().strip().split())
    x.append(a)
    y.append(b)
    
if x[0] == x[1] :
    print(x[2],end=' ')
else :
    print(x[0] + x[1] - x[2],end=' ')
    
if y[0] == y[1] :
    print(y[2],end=' ')
else :
    print(y[0] + y[1] - y[2],end=' ')    