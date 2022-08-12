from collections import deque
def solution(n, words):
    answer = [0,0]
    q = deque(words)

    d = {}
    for i in range(1,n+1) :
        d[i] = 0

    box = [q.popleft()]
    chk = 1
    d[chk] += 1
    while q :
        x = q.popleft()
        chk += 1
        if chk>n :
            chk = 1
        d[chk] += 1
        
        
        if box[-1][-1] == x[0] and not x in box :
            box.append(x)
        else :
            answer[0] = chk
            answer[1] = d[chk]
            break
            
    return answer