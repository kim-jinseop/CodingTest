import sys

t = int(sys.stdin.readline())

arr = [0] * 101
arr[0] = 1
arr[1] = 1
arr[2] = 1

for i in range(3,101) :
    arr[i] = arr[i-2] + arr[i-3]

for _ in range(t) :
    n = int(sys.stdin.readline())
    print(arr[n-1])
             
    
