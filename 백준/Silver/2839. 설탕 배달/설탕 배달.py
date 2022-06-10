n = int(input()) # 만들 숫자
num = [3,5]      # 가지고 있는 숫자

d = [5001] * (n+1)
d[0] = 0

for i in num :
    for j in range(i, n+1) :
        d[j] = min(d[j-i]+1,d[j])

result = d[n]
if result == 5001 :
    print(-1)
else :    
    print(result)