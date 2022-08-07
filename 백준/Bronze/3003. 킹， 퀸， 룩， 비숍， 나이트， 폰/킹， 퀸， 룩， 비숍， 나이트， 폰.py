arr = list(map(int,input().split()))
box = [1,1,2,2,2,8]

for i in range(len(box)) :
    print(box[i] - arr[i],end=' ')