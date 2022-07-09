from sys import stdin

n = int(stdin.readline())

r, g, b = map(int,stdin.readline().split())
box1 = r
box2 = g
box3 = b

for i in range(n-1) :
    r, g, b = map(int,stdin.readline().split())

    temp1 = box1
    temp2 = box2
    temp3 = box3

    box1 = min(temp2, temp3) + r
    box2 = min(temp1, temp3) + g
    box3 = min(temp1, temp2) + b

print(min(box1,box2,box3))