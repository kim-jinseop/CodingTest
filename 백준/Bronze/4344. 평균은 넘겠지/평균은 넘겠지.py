t = int(input())

for _ in range(t) :
    arr = list(map(int,input().split()))
    n = arr[0]
    av = sum(arr[1:]) // n
    cnt = 0

    for i in range(n) :
        if av < arr[i+1] :
            cnt += 1
    print(f'{cnt/n*100:0.3f}%')
    

