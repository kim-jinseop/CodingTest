def solution(n):
    answer = 0
    table = [0] * n
    
    def dfs(chk) :
        nonlocal answer
        if chk==n :
            answer += 1
            return
            
        for i in range(n) :
            table[chk] = i

            for j in range(chk) :
                if table[chk]==table[j] or abs(chk-j)==abs(table[chk]-table[j]) :
                    break
            else :
                dfs(chk + 1)
    
    dfs(0)
    return answer