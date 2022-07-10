from sys import stdin

n = int(stdin.readline())

result = []
for _ in range(n) :
    x = int(stdin.readline())

    if x==0 :
        result.pop()
    else :
        result.append(x)

print(sum(result))