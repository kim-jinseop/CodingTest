import sys

In = sys.stdin.readline

n = int(In())

data = []
for i in range(n) :
    a,b = In().split()
    data.append((int(a),b,i))
    
result = sorted(data, key= lambda x: (x[0],x[2]))

for i in range(n) :
    print(result[i][0], result[i][1])