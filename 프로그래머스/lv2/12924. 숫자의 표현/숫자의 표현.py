# def solution(n):
#     answer = 0
#     arr = list(range(1,n+1))
    
#     l = 0
#     r = 0
#     save = 0
#     while r<n :
#         if save < n :
#             save += arr[r]
#             r += 1
#         elif save == n :
#             answer +=1
#             save -= arr[l]
#             l += 1
#         else :
#             save -= arr[l]
#             l += 1
            
#     return answer+1


def solution(n):
    answer = 0
    for i in range(1, n + 1):
        s = 0
        while s < n:
            s += i
            i += 1
        if s == n:
            answer += 1
            
    return answer
