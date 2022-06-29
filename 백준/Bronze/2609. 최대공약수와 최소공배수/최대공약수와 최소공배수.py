a,b = map(int,input().split())

def gcd(a,b) :
    if a<b :
        a,b = b,a
    
    if a%b != 0 :
        c = a%b
        return gcd(b,c)
    else :
        return b

print(gcd(a,b))
print((a*b)//gcd(a,b))