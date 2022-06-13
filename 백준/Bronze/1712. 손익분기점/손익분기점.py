a,b,c = map(int,input().split())

result = 0

if b >= c :
    print(-1)
else :
    result = int(a / (c-b)) + 1
    print(result)