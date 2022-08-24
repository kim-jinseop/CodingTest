import sys

box = []
for i in sys.stdin :
    box.append(int(i)%42)
    
print(len(set(box)))