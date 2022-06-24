import sys

In = sys.stdin.readline

n = int(In())
data = []
for i in range(n) :
    arr = In().rstrip()
    data.append(arr)

data_set = set(data)
for result in sorted(data_set, key= lambda x : (len(x), x)) :
    print(result)
