from sys import stdin
from collections import deque

n = int(stdin.readline())
arr = [list(map(int,stdin.readline().split())) for _ in range(n)]

level = 2
start_x, start_y = 0,0

for i in range(n) :
    for j in range(n) :
        if arr[i][j] == 9 :
            start_x , start_y = j,i
            arr[i][j]  = 0

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def bfs() :
    dist = [[-1] * n for _ in range(n)]
    q = deque([(start_y,start_x)])     
    dist[start_y][start_x] = 0
    
    while q :
        y,x = q.popleft()
        for i in range(4) :
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny and ny <= n-1 and 0 <= nx and nx <= n-1 :
                if arr[ny][nx] <= level and dist[ny][nx] == -1  :
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny,nx))
    return dist

def find(dist) :
    y, x = 0,0 # 먹을 수 있는 좌표
    min_dist = 10000 # 최단 거리
    for i in range(n) :
        for j in range(n) :
            if arr[i][j] < level and dist[i][j] != -1 and 1 <= arr[i][j]:
                if dist[i][j] < min_dist :
                    min_dist = dist[i][j]
                    y,x = i,j

    if min_dist == 10000 :
        return None
    else :
        return y,x,min_dist

result = 0
eat = 0
while True :
    a = find(bfs())

    if a == None :
        print(result)
        break
    else :
        start_y = a[0]
        start_x = a[1]
        result += a[2]

        arr[start_y][start_x] = 0
        eat += 1

        if eat == level :
            eat = 0 
            level += 1