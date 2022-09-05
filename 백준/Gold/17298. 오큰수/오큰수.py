from sys import stdin

n = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))
result = [-1] * n
stack = []

for i in range(n) :
    while len(stack) != 0 and arr[stack[-1]] < arr[i] :
        result[stack.pop()] = arr[i]      
    stack.append(i)
    
print(*result)