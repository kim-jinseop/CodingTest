from sys import stdin
from collections import deque

n, m = map(int,stdin.readline().split())
tgt = list(map(int,stdin.readline().split()))
arr = list(range(1,n+1))
q = deque(arr)
result = 0

while tgt :
    if q[0] == tgt[0] :
        q.popleft()
        tgt.pop(0)

    else :
        if (len(q)//2) < q.index(tgt[0]) :
            q.appendleft(q.pop())
        else :
            q.append(q.popleft())

        result += 1

print(result)