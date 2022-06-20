from itertools import combinations 

n,m = map(int,input().split())
arr = list(map(int,input().split()))

three = list(combinations(arr,3))

result = 0

for i in range(len(three)) :

    snum = sum(three[i])

    if m >= snum : 
        if result < snum :
            result = snum
        
    else :
        continue

print(result)