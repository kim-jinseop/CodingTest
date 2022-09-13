from sys import stdin

n = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
x = int(stdin.readline())

result = 0
arr.sort()

start = 0
end = n-1

while start < end :
    if arr[start] + arr[end] == x :
        result += 1
        start += 1

    elif arr[start] + arr[end] > x :
        end -= 1

    elif arr[start] + arr[end] < x :
        start += 1

print(result)