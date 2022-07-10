from collections import deque
from sys import stdin 

queue = deque()
n,k = map(int,stdin.readline().rstrip().split())

for i in range(1,n+1) :
    queue.append(i)

cnt = 1
result = []
while queue : 
    x = queue.popleft()

    if cnt == k :
        cnt = 1
        result.append(x)
    else :
        cnt += 1
        queue.append(x)

print('<',end='')
print(', '.join(map(str,result)),end='')
print('>')