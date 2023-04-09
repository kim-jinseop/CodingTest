import heapq

def solution(numbers):
    key = [(3,1),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    
    def get_len(start,end) :
        if start == end :
            return 1
        
        x1,y1 = key[int(start)]
        x2,y2 = key[int(end)]

        dx = abs(x1-x2)
        dy = abs(y1-y2)

        w3 = min(dx,dy) 
        w2 = max(dx,dy) - w3
        return w3*3 + w2*2

    q = [[0,'4','6']]
    for number in numbers : 
        visit = []
        next_q = []
        while q :
            cnt,l,r = heapq.heappop(q)
            
            if l==r :
                continue
            if (l,r) in visit :
                continue 
            
            visit.append((l,r))
            lc = get_len(l,number)
            rc = get_len(r,number)
            
            heapq.heappush(next_q, [cnt+lc, number, r])
            heapq.heappush(next_q, [cnt+rc, l, number])
            
        q = next_q
        
    return heapq.heappop(q)[0]