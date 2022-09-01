n = int(input())
box = list(map(int,input().split()))
box = sorted(box)

m = int(input())
arr = list(map(int,input().split()))

for i in arr :
    start = 0
    end = len(box) - 1 

    while start<=end :
        mid = (start + end) // 2

        if i < box[mid] :
            end = mid-1
        elif i == box[mid] :
            print(1)
            break
        else :
            start = mid+1

    else :
        print(0)