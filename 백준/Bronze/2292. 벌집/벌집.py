n = int(input())
start = 1
i=0 
while True :
    if start + (6 * i) >= n :
        result = i+1
        break
    else :
        start += 6*i
    i += 1 
print(result)