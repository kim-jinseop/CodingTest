from sys import stdin
MAX = int(1e9)
n = int(stdin.readline())
data = [0] * 1000001
data[0] = MAX
data[1] = 0
data[2] = 1

cnt = 0
for i in range(2,n+1) :
    if i%3==0 :
        save1 = i//3
    else :
        save1 = 0

    if i%2==0 :
        save2 = i//2
    else :
        save2 = 0

    data[i] = min(data[save1],data[save2],data[i-1]) + 1
        
print(data[n])