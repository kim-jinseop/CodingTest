t = int(input())

for _ in range(t) :
    array = []
    r, s = input().split()
    r = int(r)
    
    for i in s :
        array.append(i*r)

    print(''.join(array))     