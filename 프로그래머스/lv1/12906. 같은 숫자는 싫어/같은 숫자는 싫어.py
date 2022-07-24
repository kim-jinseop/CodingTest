from collections import deque

def solution(arr):
    answer = []
    q = deque(arr)
    answer.append(q.popleft())
    while q :
        x = q.popleft()
        if x!=answer[-1] :
            answer.append(x)
            
    return answer