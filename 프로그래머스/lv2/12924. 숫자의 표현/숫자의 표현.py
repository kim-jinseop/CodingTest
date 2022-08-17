def solution(n):
    answer = 0
    arr = list(range(1,n+1))
    
    l = 0
    r = 0
    save = 0
    while r<n :
        if save < n :
            save += arr[r]
            r += 1
        elif save == n :
            answer +=1
            save -= arr[l]
            l += 1
        else :
            save -= arr[l]
            l += 1
            
    return answer+1