from sys import stdin
from collections import deque

n, k = map(int,stdin.readline().split())
arr = [-1] * 100001
q = deque()
q.append((0,n))

while q :
    time, target = q.popleft()

    if arr[target] != -1 :
        continue

    arr[target] = time

    if arr[k] != -1 :
        print(arr[k])
        break

    if target*2 < 100001 :
        q.append((time, target*2))

    if target > 0 :
        q.append((time+1, target-1))

    if target < 100000 :
        q.append((time+1, target+1))  
