import sys

def func(num) :
    a = num//2
    b = a
    while a>0 :
        if a in prime_data and b in prime_data :
            print(a,b)
            break
        else :
            a -= 1
            b += 1

t = int(sys.stdin.readline()) # 테스크 케이스 개수 T

data = [0] * 10001 # 에라토스테네스의 체
prime_data = []
for i in range(2,10001) :
    if data[i]==0 :
        prime_data.append(i)
        for j in range(i,10001,i) :
            data[j] = 1

for i in range(t) :
    n = int(sys.stdin.readline())
    result = func(n)