def solution(dirs):    
    d = {'U':(-1,0), 'R':(0,1), 'D':(1,0), 'L':(0,-1)}
    visit = set()
    
    x = 0
    y = 0
    for i in dirs :
        dx,dy = d[i]

        if x+dx < -5 or x+dx > 5 or y+dy < -5 or y+dy > 5 :
            continue
        else :
            visit.add((x, y, x+dx, y+dy)) 
            visit.discard((x+dx, y+dy, x, y))
            x += dx
            y += dy
            
    answer = len(visit)
    return answer