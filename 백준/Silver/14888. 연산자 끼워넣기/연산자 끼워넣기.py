import sys
import itertools

inp = sys.stdin.readline

n = int(inp())
data = list(inp().split())
operations_data = list(inp().split())
operations = ['+','-','*','/']
operations_ang = []
MIN = int(1e9)
MAX = -int(1e9)

for i,j in enumerate(operations_data) :
    for _ in range(int(j)) :
        operations_ang.append(operations[i])

operations_ang = set(itertools.permutations(operations_ang,n-1))

save = []
for oper_parts in operations_ang :
    calbox = []
    for i in range(n) :
        calbox.append(data[i])

        if len(calbox) == 3 :
            cal = int(eval(''.join(calbox)))
            calbox = [str(cal)]

        if i!=(n-1) : calbox.append(oper_parts[i])

    result = int(eval(''.join(calbox)))
    MIN = min(result, MIN)
    MAX = max(result, MAX)

print(MAX)
print(MIN)