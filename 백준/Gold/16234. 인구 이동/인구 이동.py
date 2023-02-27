from sys import stdin
from collections import deque

N,L,R = map(int,stdin.readline().split())

arr = []
for i in range(N) :
    arr.append(list(map(int,stdin.readline().split())))
          
visit = [[0]*N for _ in range(N)]
answer = 0
flag = 0
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y) :
    global total 
    q = deque()
    q.append((x,y))

    while q :
        x,y = q.popleft()
        union.append((x,y))
        total += arr[y][x]
        visit[y][x] = 1

        for i in range(4) :
            px = dx[i] + x
            py = dy[i] + y

            if 0<=px<N and 0<=py<N and visit[py][px]==0 and L<=abs(arr[y][x] - arr[py][px])<=R:
                q.append((px,py))
                visit[py][px] = 1
               
while True :
    for i in range(N) :
        for j in range(N) :
            if visit[i][j] == 0 :
                union = []
                total = 0

                bfs(j,i)

                if len(union) > 1 :
                    total = total//len(union)
                    for x,y in union :
                        arr[y][x] = total

                    flag = 1

    if flag :
        answer += 1
        flag = 0
        visit = [[0]*N for _ in range(N)]
    else :
        print(answer)
        break