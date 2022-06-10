import sys

def check(num) :
    if num == 1 :
        return False
    
    for j in range(2,int(num**0.5)+1) :  
        if i % j == 0 :
            return False
    return True

data = []
for i in range(2,123456*2+1) :
    if check(i) :
        data.append(i)

while True :
    n = int(sys.stdin.readline())
    count = 0    
    
    if n == 0 :
        break
    
    for i in data :
        if n < i and (2*n) >=  i :
            count += 1
            
    print(count)    