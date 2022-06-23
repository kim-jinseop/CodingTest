import sys

In = sys.stdin.readline

n = int(In())
data = []
for i in range(n) :
    x,y = map(int,In().split())
    data.append((x,y))

for result in sorted(data, key=lambda x : (x[0], x[1])) :
    print(result[0], result[1])