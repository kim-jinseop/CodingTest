from sys import stdin

n, k = map(int,stdin.readline().split())

item = [[0,0]]
for _ in range(n) :
    item.append(list(map(int,stdin.readline().split())))

value = [[0]*(k+1) for _ in range(n+1)]

for i in range(1,n+1) :
    for j in range(1,k+1) : 
        w,v = item[i]

        if j<w :
            value[i][j] = value[i-1][j]
        else :
            value[i][j] = max(value[i-1][j], value[i-1][j-w]+v)

print(value[n][k])