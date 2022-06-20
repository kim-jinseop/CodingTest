n = int(input())

for i in range(n) :
    snum = i + sum(list(map(int,(str(i)))))

    if snum == n :
        print(i)
        break
else :
    print(0)
