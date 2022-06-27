import sys

n,m = map(int,sys.stdin.readline().split())

dh = []
for _ in range(n) :
    dh.append(sys.stdin.readline().strip())

ds = []
for _ in range(m) :
    ds.append(sys.stdin.readline().strip())

result = list(sorted((set(dh) & set(ds))))
print(len(result))
for i in result :
    print(i)
