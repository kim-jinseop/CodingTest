n, m = map(int,input().split())

def isP(num) :
    if num == 1 :
        return False
    
    for j in range(2,int(num**0.5)+1) :  
        if i % j == 0 :
            return False
    return True
        
        
for i in range(n,m+1) :
    if isP(i) :
        print(i)
    
        
     