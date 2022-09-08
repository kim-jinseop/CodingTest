from sys import stdin

n, k = map(int,stdin.readline().split())

kind = []
for _ in range(n) :
    x = int(stdin.readline())
    if x <= k :
        kind.append(x)

kind.sort(reverse=True)

i = 0
result = 0
while k :
    if k >= kind[i] :
        result += k//kind[i]
        k = k%kind[i]

    else :
        i += 1

print(result)