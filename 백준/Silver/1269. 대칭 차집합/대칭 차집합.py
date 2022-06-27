import sys

a,b = map(int,sys.stdin.readline().split())
A = set(list(map(int,sys.stdin.readline().split())))
B = set(list(map(int,sys.stdin.readline().split())))

result = (A^B)
print(len(result))