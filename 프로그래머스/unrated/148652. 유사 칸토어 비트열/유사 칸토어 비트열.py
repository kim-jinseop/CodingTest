# 1 => 5^0 => 1 => 1개
# 2 => 5^1 => 11011 => 1의 개수 4개
# 3 => 5^2 => 11011 11011 00000 11011 11011 => 1의 개수 4^2
# 4 => 5^3 => 16/16/0/16/16 -> 1의 개수 4^3

bit = '11011'

def solution(n, l, r):
    return func(r) - func(l-1) # [0:r] - [0:l] = [r:l]

def func(x) :
    if x <= 5 : 
        return bit[:x].count('1')

    cnt = 1
    while x//(5**(cnt+1)) :
        cnt += 1 

    share, remainder = divmod(x, 5**cnt)
    answer = share * (4**cnt)

    if share >= 3 :
        answer -= 4**cnt

    if share == 2:
        return answer
    else:
        return answer + func(remainder)