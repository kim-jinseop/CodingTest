from sys import stdin

k, n = map(int,stdin.readline().split()) # k 가지고있는 선
lines = []
for i in range(k) :
    lines.append(int(stdin.readline()))
    
start = 1
end = max(lines)

while start<=end :
    mid = (start + end)//2
    cnt = 0

    for line in lines :
        cnt += line // mid

    if cnt >= n :
        start = mid + 1 
    elif cnt < n :
        end = mid - 1

print(end)