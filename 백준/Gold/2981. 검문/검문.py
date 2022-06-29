import sys
n = int(sys.stdin.readline())

data = []
for _ in range(n) :
    data.append(int(sys.stdin.readline()))
data.sort()

def gcd(a,b) : # 유클리드 호제법 -> 최대공약수를 빠르게 구하는 방법
    while b != 0 :
        a,b = b,a%b    
    return a

def divsor(a) :
    result = set()
    for i in range(1,int(a**0.5)+1):
        if a%i == 0 :
            result.add(i)
            result.add(a//i)

        if 1 in result :
            result.remove(1)

    return sorted(result)

x = data[1] - data[0]
for i in range(1,n-1) :
    x = gcd(x,data[i+1]-data[i])
    
print(' '.join(map(str,divsor(x))))
