import sys
input = sys.stdin.readline

n, c = list(map(int, input().split()))
arr = []
for i in range(n) :
    arr.append(int(input()))

arr.sort() # 이분탐색 조건

gap_min = 1
gap_max = arr[-1] - arr[0]
result = 0

while(gap_max>=gap_min) :
    mid = (gap_min + gap_max) // 2 
    cnt = 1

    last_position = arr[0]

    for i in range(1, n) :
        distance = arr[i] - last_position
        if distance >= mid:
            cnt += 1
            last_position = arr[i]
            
    if cnt >= c :
        gap_min = mid+1
        result = mid 
    elif cnt < c :
        gap_max = mid-1

print(result)