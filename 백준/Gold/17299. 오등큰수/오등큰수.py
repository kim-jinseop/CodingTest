import time
from sys import stdin

n = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))

answer = [-1 for _ in range(n)]

# 각 숫자의 개수 저장
d = dict()
for a in arr :
    if a in d :
        d[a] += 1
    else :
        d[a] = 1

stack = []

for i in range(n) :
    if not stack :
        stack.append(i)
        continue
    
    while stack and d[arr[stack[-1]]] < d[arr[i]] :
        x = stack.pop()
        answer[x] = arr[i] 
    
    stack.append(i)
    
print(*answer)