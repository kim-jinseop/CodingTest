def solution(w,h):
    a,b = w,h
    while b>0 :
        a,b = b,a%b
    print(a)
        
    answer = (w*h) - (w+h-a)
    return answer