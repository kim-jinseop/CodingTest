from sys import stdin
from itertools import permutations 

n,m = map(int,stdin.readline().split())
table = [list(map(int,stdin.readline().split())) for _ in range(n)]
visit = [[0]*m for _ in range(n)]
result = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
per = list(permutations([0,1,2,3],3))

def dfs(x,y,cnt,total) :
    global result 
    if cnt==4 :
        result = max(result, total)
        return

    for i in range(4) :
        nx = dx[i] + x
        ny = dy[i] + y

        if 0<=nx<n and 0<=ny<m and visit[nx][ny]==0:
            visit[nx][ny] = 1
            dfs(nx,ny,cnt+1,total + table[nx][ny])
            visit[nx][ny] = 0

def func(x,y) :
    global result 

    for arr in per :
        three = 3
        total = table[x][y]
        
        for i in arr :
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=nx<n and 0<=ny<m :
                three -= 1
                total += table[nx][ny]

        if three==0 :
            result = max(result, total)

for i in range(n) :
    for j in range(m) :
        visit[i][j] = 1
        dfs(i,j,1,table[i][j])
        visit[i][j] = 0

        func(i,j)

print(result)