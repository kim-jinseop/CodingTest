import math
w,h,x,y,p = map(int,input().split())
r = h // 2
count = 0

for _ in range(p) :
    px,py = map(int,input().split())
    
    l_circle = math.sqrt((px-x)**2 + (py-(y+r))**2)
    r_circle = math.sqrt((px-(x+w))**2 + (py-(y+r))**2)
    
    if l_circle <= r or r_circle <= r or ((x<=px<=x+w) and (y<=py<=y+h)) :
        count += 1

print(count)