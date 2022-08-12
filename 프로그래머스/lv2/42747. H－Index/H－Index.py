from bisect import bisect_left
def solution(citations):
    answer = 0
    citations.sort()
    
    for h in range(len(citations),0,-1) :
        index = bisect_left(citations,h)
        
        if h <= len(citations[index:]) and len(citations[:index]) < h :
            answer = h
            break
        
    return answer