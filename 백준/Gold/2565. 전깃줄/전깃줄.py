from sys import stdin
import bisect 

n = int(stdin.readline())

line = []
for _ in range(n) :
    line.append(list(map(int,stdin.readline().split())))
line.sort()

arr = []
for i in range(len(line)) :
    if not arr :
        arr.append(line[i][1])
    else :
        index = bisect.bisect_left(arr, line[i][1])

        if index == len(arr) :
            arr.append(line[i][1])
        else :
            arr[index] = line[i][1]

print(len(line)-len(arr))
