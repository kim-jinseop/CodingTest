from sys import stdin

n = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
dpr = [1] * n
dpl = [1] * n
result = 0

for i in range(n) :
    for l in range(i) :
        if arr[i] > arr[l] :
            dpl[i] = max(dpl[i], dpl[l] + 1) 

for i in range(n-1,-1,-1) :
    for r in range(i+1,n) :
        if arr[i] > arr[r] :
            dpr[i] = max(dpr[i], dpr[r] + 1)

for i in range(n) :
    result = max(result, dpr[i] + dpl[i] - 1)

print(result)