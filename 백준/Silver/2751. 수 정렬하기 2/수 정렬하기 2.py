import sys

n = int(sys.stdin.readline())

data = [0] * 2000001
for _ in range(n) :
    data[int(sys.stdin.readline())+1000000] = 1

for i in range(2000001) :
    if data[i] == 1 :
        print(i-1000000)

