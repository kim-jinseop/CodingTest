import sys
inp = sys.stdin.readline

t = int(inp())

for _ in range(t) :
    n = int(inp())
    category_data = []
    dic = {}
    result = 1

    for i in range(n) :
        x, category = inp().split()

        if category in category_data :
            dic[category] += 1      

        else :
            category_data.append(category)
            dic[category] = 1 

    for j in dic.values() :
        result *= j+1
    print(result - 1)
