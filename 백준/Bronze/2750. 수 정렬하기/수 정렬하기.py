import sys
In = sys.stdin.readline

n = int(In())

arr = []
for _ in range(n) :
    arr.append(int(In()))

for i in range(n-1):
    for j in range(n-1):
        if arr[j] > arr[j+1] :
            index = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = index 
            
for i in range(n) :
    print(arr[i])
        