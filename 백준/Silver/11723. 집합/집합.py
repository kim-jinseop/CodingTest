import sys 

t = int(sys.stdin.readline())

s = set()
for _ in range(t) :
    data = list(sys.stdin.readline().rstrip().split())
    if len(data) == 2:
        n,m = data[0],int(data[1])
    else :
        n = data[0]
    
    
    if n == 'add' :
        s.add(m)    
    elif n == 'remove' :
        s.discard(m)
    elif n == 'check' :
        if m in s :
            print(1)
        else :
            print(0)
    elif n == 'toggle' :
        if m in s :
            s.discard(m)
        else :
            s.add(m)
    elif n == 'all' :
            s.update([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif n == 'empty' :
            s = {0}
