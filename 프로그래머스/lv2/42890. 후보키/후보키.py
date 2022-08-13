# from itertools import combinations

# def solution(relation):
#     answer = 0
#     num = [i for i in range(len(relation))]
#     print(num)
#     arr = list(zip(*relation))
    
#     for i in range(1,len(arr)+1) :
#         combination = list(combinations(num,i))
        
#         for combi in combination :
#             print(combi)    
        
#     return answer

from itertools import combinations

def solution(relation):
    n = len(relation)
    df = list(zip(*relation)) ## 배열을 90도 회전시켜 dataframe형식으로 만들기
    result = []
    for i in range(1,len(df)+1):
        comb = list(combinations(range(len(df)),i)) ## 각 열들을 조합하는 조합 구하기
        for c in comb:
            if len(set('.'.join(x) for x in zip(*[df[idx] for idx in c]))) == n: ## 합친 열들이 유일성을 만족하는지
                for r in result : 
                    if r.issubset(set(c)) : break ## 최소성을 만족하는지 판별
                else: result.append(set(c)) ## for-else구문은 for구문이 다 실행되면 else로 넘어가게 됩니다.
    return len(result)
