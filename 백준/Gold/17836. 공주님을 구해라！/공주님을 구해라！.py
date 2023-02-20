import sys
from collections import deque

INF = int(1e9)

n,m,t = map(int,sys.stdin.readline().split(' '))
arr = [list(map(int,sys.stdin.readline().split(' '))) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
visit[0][0] = 1
q = deque([[0,0,0]])

# 동남서북
dx = [1,0,-1,0] 
dy = [0,-1,0,1]
answer = INF
gram = 0

while(q) :
    x,y,time = q.popleft()

    if arr[y][x] == 2 :
        gram = [x,y,time]

    if time > t or x==m-1 and y==n-1 :
        answer = time
        break
    else : 
        for i in range(4) :
            px = x + dx[i]
            py = y + dy[i]

            if px >= 0 and py >= 0 and px < m and py < n and visit[py][px] == 0 and arr[py][px] != 1:
                visit[py][px] = 1
                q.append([px,py,time+1])

if gram :
    gx, gy, gt = gram
    answer = min(gt+m-gx+n-gy-2, answer)

if answer > t :
    print("Fail")
else :
    print(answer)
