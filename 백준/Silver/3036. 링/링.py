import sys 

n = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().strip().split()))

def gcd(a,b):
    while b!=0 :
        a,b=b,a%b
    return a

fst = data[0]
for i in range(1,n) :
    lcm = (data[0]*data[i]) // gcd(data[0],data[i])

    a = lcm//data[i]
    b = lcm//data[0]
    print(f'{a}/{b}')
