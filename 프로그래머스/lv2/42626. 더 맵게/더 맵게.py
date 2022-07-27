import heapq

def solution(scoville, K):
    answer = 0
    cnt = 0
    heapq.heapify(scoville)
    
    while scoville :
        if scoville[0] < K :
            if len(scoville) == 1 :
                answer = -1
                break
            
            f = heapq.heappop(scoville)
            s = heapq.heappop(scoville)           
            heapq.heappush(scoville, f+(s*2))
            cnt += 1
        else :
            answer = cnt 
            break  
    
    return answer