import sys

arr = [[[0 for _ in range(51)] for _ in range(51)] for _ in range(51)]

def w(a,b,c) :
    if a <= 0 or b <= 0 or c <= 0 :
        return 1

    if arr[a][b][c] > 0:
        return arr[a][b][c]

    elif a > 20 or b > 20 or c > 20 :
        arr[a][b][c] = w(20, 20, 20)
        return arr[a][b][c]

    elif a < b and b < c :
        arr[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return arr[a][b][c]

    else :
        arr[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return arr[a][b][c]
    
while True :    
    a,b,c = map(int,sys.stdin.readline().split())
    if a==b==c==-1 :
        break
    
    print('w({}, {}, {}) = {}'.format(a,b,c,w(a,b,c)))