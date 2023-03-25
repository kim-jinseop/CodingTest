from sys import stdin
n,m,l = map(int,stdin.readline().split())
arr = list(map(int,stdin.readline().split())) + [l] + [0]
arr.sort()

start = 1
end = l
answer = 0
while start <= end :
    cnt = 0 
    mid = (start+end)//2

    for i in range(1,len(arr)) :
        if (arr[i]-arr[i-1]) > mid :
            cnt += (arr[i]-arr[i-1]-1)//mid

    if cnt > m :
        start = mid + 1
    else :
        end = mid - 1
        answer = mid
print(answer)