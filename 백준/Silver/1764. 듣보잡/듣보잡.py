import sys

n,m = map(int,sys.stdin.readline().split())

data = sys.stdin.read().splitlines()
dh = set(data[:n])
ds = set(data[n:])

result = sorted(list(dh&ds))
print(len(result))
for i in result :
    print(i)
