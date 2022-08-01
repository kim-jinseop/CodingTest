dx = [-1,0,1,0]
dy = [0,1,0,-1]

def func(place) :
    for i in range(5) :
        for j in range(5) :
            if place[i][j] == 'P' :
                for posi in range(4) :
                    nx = i + dx[posi]
                    ny = j + dy[posi]
                    if nx>=0 and nx<5 and ny>=0 and ny<5 :
                        if place[nx][ny] == 'P' :
                            return 0
                        
            elif place[i][j] == 'O' :
                cnt = 0 
                for posi in range(4) :
                    nx = i + dx[posi]
                    ny = j + dy[posi]
                    if nx>=0 and nx<5 and ny>=0 and ny<5 :
                        if place[nx][ny] == 'P' :
                            cnt += 1 
                            
                if cnt > 1 :
                    return 0
    return 1
                
def solution(places):
    answer = []
    for place in places :
        answer.append(func(place))              
            
    return answer