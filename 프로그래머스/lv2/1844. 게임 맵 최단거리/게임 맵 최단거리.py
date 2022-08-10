from collections import deque
import copy

q = deque()
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(x,y,maps) :
    q.append((x,y))
    while q :
        x,y = q.popleft()
        
        for i in range(4) :
            nx = dx[i] + x
            ny = dy[i] + y
            
            if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]) :
                continue 

            if maps[nx][ny] == 0 :
                continue 
            
            if maps[nx][ny] == 1 :
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx,ny))
                                 
    return maps[len(maps)-1][len(maps[0])-1]

def solution(maps):
    answer = bfs(0,0,maps) 
    return answer if answer!=1 else -1