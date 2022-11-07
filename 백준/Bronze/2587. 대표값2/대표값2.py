import sys

data = list(map(int,sys.stdin.read().split()))
data.sort()

print(sum(data)//len(data))
print(data[len(data)//2])