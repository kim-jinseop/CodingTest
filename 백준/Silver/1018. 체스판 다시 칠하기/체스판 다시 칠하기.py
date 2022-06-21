n,m = map(int,input().split()) # n:행 m:열

data = [input() for _ in range(n)]
result = []

for i in range(n-7) : # 8행 자르기
    for j in range(m-7) : # 8열 자르기
        index1 = 0
        index2 = 0
        for a in range(i,i+8) :
            for b in range(j,j+8) :
                if (a+b) % 2 == 0 : 
                    if data[a][b] != 'W':
                        index1 += 1
                    if data[a][b] != 'B':
                        index2 += 1
                else : 
                    if data[a][b] != 'B':
                        index1 += 1
                    if data[a][b] != 'W':
                        index2 += 1

        result.append(min(index1, index2))

print(min(result))

