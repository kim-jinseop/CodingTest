def solution(n):
    answer = []
    
    def hanoi(n,left,mid,right) :
        if n==0 :
            return 
        
        hanoi(n-1,left,right,mid)
        answer.append([left,right])
        hanoi(n-1,mid,left,right)
    
    hanoi(n,1,2,3)
    return answer