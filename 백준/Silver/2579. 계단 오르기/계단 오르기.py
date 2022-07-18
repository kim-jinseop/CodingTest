from sys import stdin

n = int(stdin.readline())
arr = [0] + [int(stdin.readline()) for _ in range(n)]
box = [0] * (n+1)

box[1] = arr[1]

if n>1 :
    box[2] = arr[1] + arr[2]
    for i in range(3,n+1) :
        box[i] = max(box[i-3]+arr[i-1],box[i-2]) + arr[i]

print(box[n])