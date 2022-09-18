from sys import stdin

n, m = map(int,stdin.readline().split()) # k 가지고있는 선
trees = list(map(int,stdin.readline().split()))

start = 1
end = sum(trees)

while start<=end :
    mid = (start + end)//2
    s = 0

    for tree in trees :
        if tree > mid :
            s += tree - mid

    if s >= m :
        start = mid + 1 
    elif s < m :
        end = mid - 1

print(end)