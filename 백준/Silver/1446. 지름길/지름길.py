from sys import stdin

INF = int(1e9)
n, leng = map(int,stdin.readline().split())
data = [list(map(int,stdin.readline().split())) for _ in range(n)]
data.sort()

arr = [i for i in range(leng+1)]

for i in range(n) :
    if data[i][1] > leng :
        continue

    arr[data[i][1]] = min(arr[data[i][0]]+data[i][2], arr[data[i][1]])
    for j in range(data[i][1] + 1, leng+1) :
        arr[j] = min(arr[j-1] + 1, arr[j])

print(arr[leng])
