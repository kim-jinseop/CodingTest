import sys

box = [0] * 1000001
box[0] = 1
box[1] = 2
for i in range(2,1000000) :
    box[i] = (box[i-1] + box[i-2])%15746    

n = int(sys.stdin.readline())
print(box[n-1])