def solution(skill, skill_trees):
    answer = 0
    stack = []
    for skill_tree in skill_trees :
        tree = ''
        for i in skill_tree :
            if i in skill :
                tree += i
        
        leng = len(tree)
        if tree == skill[:leng] :
            answer += 1
            
    return answer