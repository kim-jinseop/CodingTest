from sys import stdin

n = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
remove_node = int(stdin.readline())

def dfs(arr, remove_node) :
    arr[remove_node] = -2
    for node in range(n) :
        if remove_node == arr[node] :
            dfs(arr,node)

dfs(arr,remove_node)

result = 0
for node in range(n) :
    if arr[node] != -2 and node not in arr :
        result += 1

print(result)