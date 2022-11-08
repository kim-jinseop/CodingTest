a = []
b = []

w,h = map(int,input().split())
for _ in range(w) :
    a.append(list(map(int,input().split())))

for _ in range(w) :
    b.append(list(map(int,input().split())))

for i in range(w) :
    for j in range(h) :
        a[i][j] += b[i][j] 

    print(*a[i])