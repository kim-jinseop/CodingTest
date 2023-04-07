from sys import stdin
from collections import deque 

answer = int(1e9)
n, m, k = map(int,stdin.readline().split())
map = [list(map(int,stdin.readline().rstrip())) for _ in range(n)]
visit = [[[0]*m for _ in range(n)] for _ in range(k+1)]

dx = [1,0,0,-1]
dy = [0,1,-1,0]

q = deque()
q.append([0,0,k,1])
visit[k][0][0] = 1

while q :
    x,y,k,cnt = q.popleft()
    
    if x==n-1 and y==m-1 :
        answer = min(answer, cnt)

    for i in range(4) :
        nx = dx[i] + x
        ny = dy[i] + y

        if nx<0 or ny<0 or nx>=n or ny>=m or visit[k][nx][ny] == 1 :
            continue
        else :
            visit[k][nx][ny] = 1

            if map[nx][ny] == 0 :
                q.append([nx,ny,k,cnt+1])
            elif k : 
                q.append([nx,ny,k-1,cnt+1])

print(answer if answer!=int(1e9) else -1)