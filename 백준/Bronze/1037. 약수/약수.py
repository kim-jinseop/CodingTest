n = int(input())
arr = list(map(int,input().split()))

if n!=1:
    print(max(arr)*min(arr))
else :
    print(arr[0]**2)
    