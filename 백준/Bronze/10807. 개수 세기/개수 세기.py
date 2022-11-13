n = int(input())
l = list(map(int,input().split()))
target = int(input())
result = 0

for i in l :
    if target == i :
        result += 1 
        
print(result)