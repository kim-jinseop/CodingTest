import sys
In = sys.stdin.readline

n = int(In())
data = list(map(int,In().split()))
data_sort = sorted(set(data))
data_dict = {a:b for b,a in enumerate(data_sort)}

for i in data :
    print(data_dict[i], end=' ')