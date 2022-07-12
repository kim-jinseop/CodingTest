import sys 

n = list(map(int,sys.stdin.read().split()))
print(max(n))
print(n.index(max(n))+1)