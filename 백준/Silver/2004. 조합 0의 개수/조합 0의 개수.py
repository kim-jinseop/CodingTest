import sys

inp = sys.stdin.readline

n,k = map(int,inp().split())

def f5(n) :
    cnt = 0
    while n >= 5 :
        cnt += n//5
        n = n//5
    return cnt
def f2(n) :
    cnt = 0
    while n >= 2 :
        cnt += n//2
        n = n//2
    return cnt

print(min(f5(n)-f5(k)-f5(n-k),f2(n)-f2(k)-f2(n-k)))