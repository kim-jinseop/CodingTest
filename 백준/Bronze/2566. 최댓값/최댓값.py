a = []
Max = 0
w = 1
h = 1

for _ in range(9) :
    a.append(list(map(int,input().split())))

for i in range(9) :
    for j in range(9) :
        if Max < a[i][j] :
            Max = a[i][j]
            w = j+1
            h = i+1

print(Max)
print(h,w)