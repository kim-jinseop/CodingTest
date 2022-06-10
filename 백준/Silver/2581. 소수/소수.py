n = int(input())
m = int(input())

data = []
result = 0
min = 0

for i in range(n,m+1) :
    for j in range(2,i+1) :
        if j == i :
            data.append(i)
            break
            
        if i % j == 0 :
            break
        
data.sort()

if data :
    print(sum(data))
    print(data[0])
else :
    print(-1)    