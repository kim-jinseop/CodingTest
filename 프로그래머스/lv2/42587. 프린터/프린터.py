from collections import deque
def solution(priorities, location):
    answer = 0
    box = []
    q= deque(priorities)
    
    while q :
        Max = max(q)
        x = q.popleft() 
        if x == Max :
            answer += 1
            if location == 0 :
                break
        else :
            q.append(x)
            
        location -= 1
        if location < 0 :
            location = len(q)-1
    
    return answer
