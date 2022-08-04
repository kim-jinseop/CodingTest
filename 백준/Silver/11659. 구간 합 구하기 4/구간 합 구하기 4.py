from sys import stdin
In = stdin.readline
n,m = map(int,In().split())
arr = list(map(int,In().split()))

answer = []
answer.append(0)
Sum = 0
for i in arr :
    Sum += i
    answer.append(Sum)

for i in range(m) :
    start,end = map(int,In().split())
    print(answer[end]-answer[start-1])