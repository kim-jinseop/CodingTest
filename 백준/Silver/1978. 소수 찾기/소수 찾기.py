n = int(input())
array = list(map(int,input().split()))
result = 0

for i in range(n) :
    num = array[i]
    for j in range(2,num+1) :
        if j == num :
            result += 1
            break
            
        if num % j == 0 :
            break
print(result)    