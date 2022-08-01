from itertools import permutations
import copy

def solution(expression):
    answer = []
    
    # 연산자 경우의 수
    opers = list(permutations(['*','+','-'],3))
    
    # 식을 연산자와 숫자로 나눈다
    main_box = []
    save = ''
    for i in expression:
        if i.isdigit() :
            save += i
        else :
            main_box.append(save)
            main_box.append(i)
            save = ''
    else :
        main_box.append(save)
        
    # 전체 경우의 수    
    for oper in opers :
        # 경우의 수 중 하나
        box = copy.deepcopy(main_box)
        for o in oper :
            
            while o in box :
                center = box.index(o)
                save = str(eval(''.join(box[center-1:center+2])))
                del box[center-1:center+2]
                box.insert(center-1,save)

        answer.append(abs(int(*box)))
    return max(answer)