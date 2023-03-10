from collections import deque

def dist_find(x,y,r,c) :
    return abs(x - r) + abs(y - c)
 
def solution(n, m, x, y, r, c, k):
    dist = dist_find(x,y,r,c)
    dt = [(1,0,"d"),(0,-1,"l"),(0,1,"r"),(-1,0,"u")]
    
    q = deque([(x,y,"",0)])
            
    # if (k-dist)%2 != 0 :
    #     return "impossible"
        
    
    while q :
        x,y,result,cnt = q.popleft()
        
        if (x,y) == (r,c) and (k - cnt ) % 2 == 1:
            return "impossible"
        if (x,y) == (r,c) and cnt == k:
            return result
        
        # if k==cnt :
        #     if x==r and y==c :
        #         return result
        #     else :
        #         continue
        
        for i in range(4) :
            px = dt[i][0] + x 
            py = dt[i][1] + y
            pr = dt[i][2] 

            if cnt + 1 > k-dist_find(px,py,r,c):
                continue
            
            if px <= 0 or px > n or py <= 0 or py > m: 
                continue

            q.append((px,py,result+pr,cnt+1))
            break
    
    return "impossible"

