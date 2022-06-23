import sys

In = sys.stdin.readline

n = int(In())
data = list(map(int,str(n)))
data.sort(reverse=True)

data = list(map(str,data))
print(''.join(data))