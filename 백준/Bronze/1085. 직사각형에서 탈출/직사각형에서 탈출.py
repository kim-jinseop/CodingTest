import sys

x,y,w,h = map(int,sys.stdin.readline().strip().split())

if x < (w-x) :
    min_x = x
else :
    min_x = (w-x)
    
if y < (h-y) :
    min_y = y
else :
    min_y = (h-y)
    
print(min(min_x,min_y))   