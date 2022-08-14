from collections import deque
def solution(s):
    if len(s) % 2 != 0 :
        return False

    q = deque(s) 
    stack = []
    
    while q :
        x = q.popleft()
        
        if x == '(' :
            stack.append(x)
            
        elif x == ')' and stack : 
            stack.pop()
            
        else :      
            return False
            
    return False if stack else True