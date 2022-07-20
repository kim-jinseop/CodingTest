def solution(phone_number):
    leng = len(phone_number)
    part = phone_number[leng-4:leng]
    answer = ('*' * (leng-4)) + part
    return answer