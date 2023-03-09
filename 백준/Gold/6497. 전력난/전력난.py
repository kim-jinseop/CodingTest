# 신장트리 - 크루스칼 알고리즘

from sys import stdin

# 부모 찾기
def find_parents(parents, x) :
    if parents[x] != x :
        parents[x] = find_parents(parents, parents[x])
    return parents[x]

# 두 원소가 속한 집합 합치기
def union(parents, a, b):
    a = find_parents(parents, a)
    b = find_parents(parents, b)

    if a<b :
        parents[b] = a
    else :
        parents[a] = b

while True :
    m, n = map(int,stdin.readline().split())
    if m==0 and n==0 :
        break
    
    result = 0
    total = 0

    # 부모 리스트 - 자기자신으로 초기화
    parents = []
    for i in range(m) :
        parents.append(i)

    # 간선 정보 입력 받기
    edges = []
    for _ in range(n) :
        a,b,cost = map(int,stdin.readline().split())
        edges.append((cost,a,b))

    # 오름차순으로 정렬
    edges.sort()

    for edge in edges :
        cost, a, b = edge
        total += cost

        if find_parents(parents,a) != find_parents(parents,b) :
            union(parents, a, b)
            result += cost

    print(total - result) 