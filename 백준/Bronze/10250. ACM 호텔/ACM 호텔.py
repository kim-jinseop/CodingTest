t = int(input())

for _ in range(t) :
    h,w,n = map(int,input().split())
    
    if n%h != 0 : 
        high = (n%h) * 100
        width = (n//h) + 1
    else :
        high = h*100            
        width = (n//h)
    
    print(high + width)