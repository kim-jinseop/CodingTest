n = int(input())

data = []
rank = [1] * n
for i in range(n) :
    weight, height = map(int,input().split())
    data.append((weight, height))
    
for i, target in enumerate(data) :
    for j in range(n) :
        if target[0] < data[j][0] :
            if target[1] < data[j][1] :
                rank[i] += 1

for i in range(n) :                    
    print(rank[i])