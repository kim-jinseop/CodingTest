import sys

n = list(sys.stdin.readline().strip())

arr = []
for i in range(len(n)) :
    for j in range(i,len(n)) :
        arr.append(''.join(n[i:j+1]))

print(len(set(arr)))