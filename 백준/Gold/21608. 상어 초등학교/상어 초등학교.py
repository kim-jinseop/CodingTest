from sys import stdin
from collections import defaultdict

n = int(stdin.readline())

score = {0:0, 1:1, 2:10, 3:100, 4:1000}
table = [[0]*n for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

student = defaultdict(int)
order = []
result = 0

for _ in range(n*n) : 
    info = list(map(int, stdin.readline().split()))
    student[info[0]] = info[1:]
    order.append(info[0])

def func(num) :
    box = []

    for i in range(n) :
        for j in range(n) :
            if table[i][j] == 0 :
                empty = 0
                like = 0

                for k in range(4) :
                    nx = dx[k] + i
                    ny = dy[k] + j

                    if nx < 0 or nx >= n or ny < 0 or ny >= n :
                        continue

                    if table[nx][ny] == 0 :
                        empty += 1
                    elif table[nx][ny] in student[num] :
                        like += 1 

                box.append((like,empty,i,j))

    box.sort(reverse=True, key=lambda x:(x[0],x[1]))
    table[box[0][2]][box[0][3]] = num
    
for s in order :
    func(s)


for i in range(n) :
    for j in range(n) :
        cnt = 0
        for k in range(4) :
            nx = dx[k] + i
            ny = dy[k] + j

            if nx < 0 or nx >= n or ny < 0 or ny >= n :
                continue

            elif table[nx][ny] in student[table[i][j]] :
                cnt += 1 

        result += score[cnt]

print(result)