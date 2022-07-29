result = 0

def mfunc(cnt,numbers,data,target) :
    global result
    if cnt == len(numbers) :
        if data==target :
            result += 1
            return
    else :
        data -= numbers[cnt]
        cnt += 1
        mfunc(cnt,numbers,data,target)
        pfunc(cnt,numbers,data,target)

def pfunc(cnt,numbers,data,target) :
    global result
    if cnt == len(numbers) :
        if data==target :
            result += 1
            return
    else :
        data += numbers[cnt]
        cnt += 1
        mfunc(cnt,numbers,data,target)
        pfunc(cnt,numbers,data,target)
            
def solution(numbers,target):
    answer = 0
    mfunc(0,numbers, answer, target)
    pfunc(0,numbers, answer, target) 
    return result//2