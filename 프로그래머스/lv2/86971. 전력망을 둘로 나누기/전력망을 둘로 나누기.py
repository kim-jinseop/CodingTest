def dfs(start,visit) :
    global cnt
    visit.append(start)
    cnt += 1
    for i in box[start] :
        if i not in visit :
            dfs(i,visit)

def solution(n, wires):
    global box, cnt
    answer = int(1e9)
    
    for i in range(n) : # 끊을 부분 (index)
        box = [[] for _ in range(n+1)]
        cnt = 0
        for j in range(len(wires)) :
            if i==j :
                continue
            else :
                start, end = wires[j]
                box[start].append(end)
                box[end].append(start)
                
        dfs(1,[])        
        answer = min(answer, abs(n-cnt*2))
        
    return answer