
def solution(operations):
    q = []
    for i in operations :
        if i[0]=='I' :
            q.append(int(i[2:]))
        elif i[0]=='D' :
            if q :
                if i[2]=='-' :
                    q.sort()                
                    q.pop(0)
                else :
                    q.sort(reverse=True)
                    q.pop(0)
    
    if q :
        q.sort()
        answer = [q.pop(-1),q.pop(0)]
    else :
        answer = [0,0]    
    return answer 