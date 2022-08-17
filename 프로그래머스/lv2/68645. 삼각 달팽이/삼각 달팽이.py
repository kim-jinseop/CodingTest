from itertools import chain
def solution(n):
    answer = 0
    box = [[0]*i for i in range(1,n+1)]
    
    x = -1
    y = 0
    
    num = 1
    for i in range(n) :
        for j in range(i,n) :
            if i%3==0 :
                x+=1
            elif i%3==1:
                y+=1
            else :
                y-=1
                x-=1
            box[x][y] = num
            num += 1
    return list(chain(*box))