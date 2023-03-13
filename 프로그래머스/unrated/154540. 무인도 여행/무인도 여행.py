from collections import deque

def solution(maps):
    answer = []
    
    col_len = len(maps) 
    arr_len = len(maps[0])
    
    visit = [[0]*arr_len for _ in range(col_len)]
    
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    q = deque()
    
    def func(x,y,total) :
        q.append((x,y)) 
        while q :
            x,y = q.popleft()
            for i in range(4) :
                nx = dx[i] + x
                ny = dy[i] + y

                if nx<0 or nx>= col_len or ny<0 or ny>=arr_len or maps[nx][ny] == "X":
                    continue
                
                if visit[nx][ny] == 0 :
                    visit[nx][ny] = 1
                    total += int(maps[nx][ny])
                    q.append((nx,ny))
                    
        answer.append(total)

    for i in range(col_len) :
        for j in range(arr_len) :
            if visit[i][j] == 0 and maps[i][j] != "X" :
                visit[i][j] = 1
                total = int(maps[i][j])
                func(i,j,total)
    
    if not answer :
        answer.append(-1)
        
    return sorted(answer)