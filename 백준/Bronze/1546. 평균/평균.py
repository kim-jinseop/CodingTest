import sys

n = int(sys.stdin.readline())
box = list(map(int,sys.stdin.readline().split()))
Max = max(box)

for i in range(len(box)) :
    box[i] = (box[i]/Max)*100

print(round(sum(box)/n,2))