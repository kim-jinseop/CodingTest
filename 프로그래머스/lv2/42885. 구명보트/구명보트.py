# from bisect import bisect_right
# def solution(people, limit):
#     answer = 0
#     people.sort()
    
#     while people :
#         r = people.pop() 
#         x = limit - r
        
#         index = bisect_right(people,x)
            
#         if index :
#             people.pop(index-1)

#         answer += 1       
#     return answer

from collections import deque
from bisect import bisect_right
def solution(people, limit):
    answer = 0
    people.sort()
    q = deque(people)
    
    while q :
        r = q.pop() 
        x = limit - r
        
        if q :
            if x >= q[0] :
                q.popleft()

        answer += 1       
    return answer