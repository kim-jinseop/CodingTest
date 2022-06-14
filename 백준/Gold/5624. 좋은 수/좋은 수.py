n = int(input())
arr = list(map(int,input().split()))
data = [0] * 400001
result = 0

for i in range(n) :
    for j in range(i) :
        if data[arr[i]-arr[j]+200000] :
            result += 1
            break   
    for j in range(i+1) :
        data[arr[i]+arr[j]+200000] = 1

print(result)