# def solution(numbers):
#     answer = ''   
#     position = [1000,100,10,1]
#     p = 0
#     while p < 4 :
#         box = [[] for _ in range(10)]
        
#         for number in numbers :
#             num = (number//position[p])%10
#             box[num].append(number)

#         index = 0
#         for i in box[::-1]:
#             for j in i[::-1] :
#                 numbers[index] = j
#                 index += 1
        
#         p += 1
#         print(box)
#     for i in numbers :
#         if i!=0 :
#             answer += str(i)
            
#     if answer=='' :
#         answer += '0'

#     return answer

def solution(numbers):
    str_numbers = sorted(list(map(str, numbers)), reverse=True, key = lambda x:x*3)
    return str(int("".join(str_numbers)))
