Max = int(input())
n = int(input()) 
Sum = 0

for i in range(n) :
    p, c = map(int,input().split())
    Sum += (p*c)
    
if Max == Sum :
    print('Yes')
  
else : 
    print('No')