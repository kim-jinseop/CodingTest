import sys 

a = int(input())
b = int(input())
c = int(input())
n = str(a*b*c)

arr = [0] * 10
for i in n :
    arr[int(i)] += 1

for i in arr :
    print(i)