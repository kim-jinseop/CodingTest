from itertools import chain
def solution(arr):
    answer = [0,0]
    for i in arr :
        answer[0] += i.count(0)
        answer[1] += i.count(1)
    
    def func(arr) :
        x = list(chain(*arr))
        if len(x) == 1:
            return 
        if len(x)==x.count(0):
            answer[0] -= len(x) -1
            return 
        elif len(x)==x.count(1):
            answer[1] -= len(x) -1
            return 
        else :
            func([[arr[i][j] for j in range(0,len(arr)//2)]for i in range(0,len(arr)//2)])
            func([[arr[i][j] for j in range(len(arr)//2,len(arr))]for i in range(0,len(arr)//2)])
            func([[arr[i][j] for j in range(0,len(arr)//2)]for i in range(len(arr)//2,len(arr))])
            func([[arr[i][j] for j in range(len(arr)//2,len(arr))]for i in range(len(arr)//2,len(arr))])
            
    func(arr)  

    return answer