from sys import stdin
import copy

n, m = map(int,stdin.readline().rstrip().split())
arr = [list(map(int,stdin.readline().split())) for _ in range(n)]
arr_copy = [[0]*m for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,-1,0,1]

result = 0

def situation(y,x) :
    for i in range(4) :
        nx = x+dx[i]
        ny = y+dy[i]

        if 0 > ny or ny > n-1 or 0 > nx or nx > m-1 :
            continue
        else :
            if arr_copy[ny][nx] == 0 :
                arr_copy[ny][nx] = 2
                situation(ny,nx)

def cal() :
    cnt = 0

    for part in arr_copy :
        cnt += part.count(0)

    return cnt

def func(cnt) :
    global result

    if cnt == 3 :
        for i in range(n):
            for j in range(m):
                arr_copy[i][j] = arr[i][j]

        for y in range(n) :
            for x in range(m) : 
                if arr_copy[y][x] == 2 :
                    situation(y,x)
                    
        result = max(result,cal())
        return 

    for y in range(n) :
        for x in range(m) :
            if arr[y][x] == 0 :
                arr[y][x] = 1
                func(cnt+1)
                arr[y][x] = 0

func(0)
print(result)