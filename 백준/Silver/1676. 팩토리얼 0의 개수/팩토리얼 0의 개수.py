import math
n = int(input())

nf = math.factorial(n)

count = 0
for i in range(len(str(nf))) :
    if str(nf)[len(str(nf))-1-i] == '0' :
        count += 1
    else :
        break

print(count)