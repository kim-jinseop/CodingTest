import math
t = int(input())


for i in range(t) :
    x1,y1,r1,x2,y2,r2 = map(int,input().split())

    r12 = math.sqrt((x1-x2)**2 + (y1-y2)**2)

    if x1==x2 and y1==y2 and r1 == r2 :
        print(-1)
    elif r12==r1+r2 or r12==abs(r1-r2)  :
        print(1)
    elif abs(r1-r2)<r12 and r12<r1+r2 :
        print(2)
    else : 
        print(0)