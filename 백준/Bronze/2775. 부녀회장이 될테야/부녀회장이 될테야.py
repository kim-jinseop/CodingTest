t = int(input())

def cal(k,n) :
    apart = [[0]*n for _ in range(k+1)]
    
    for i in range(n) :
        apart[0][i] = i+1
    
    for i in range(1,k+1) :
        for j in range(n) : 
            if j==0 : 
                apart[i][j] = 1
            else :       
                apart[i][j] = apart[i][j-1] + apart[i-1][j] 
                
    return apart[k][n-1]
 
for _ in range(t) :
    k = int(input())
    n = int(input())
    
    print(cal(k,n))
    