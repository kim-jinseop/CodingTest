import sys
input = sys.stdin.readline

n = int(input())


data = [0] * 10001

for _ in range(n) :
    data[int(input())] += 1

i = 0
while True :
    if data[i] != 0 :
        print(i)
        data[i] -= 1

    else :   
        i += 1

    if i == 10001 :
        break