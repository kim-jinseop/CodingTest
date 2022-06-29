import math
t = int(input())

for _ in range(t) :
    x1,y1,x2,y2 = map(int,input().split())
    n = int(input())
    count = 0
    
    for i in range(n) :
        cx,cy,r = map(int,input().split())
        
        start_distance = math.sqrt((x1-cx)**2 + (y1-cy)**2)
        end_distance = math.sqrt((x2-cx)**2 + (y2-cy)**2)
        
        if (r < start_distance and r > end_distance) or (r > start_distance and r < end_distance) :                        
            count += 1 
            
    print(count)