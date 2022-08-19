from collections import deque

def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    Max = (sum1 + sum(q2))//2
    
    while q1 and q2 :
        if sum1 < Max :
            x = q2.popleft()
            q1.append(x)
            sum1 += x

        elif sum1 > Max  :
            x = q1.popleft()
            sum1 -= x

        else :
            return answer
        
        answer += 1
        
    else :
        return -1