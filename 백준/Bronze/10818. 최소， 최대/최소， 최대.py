n = int(input())

array = []
array = list(map(int,input().split()))

array.sort()

min = array[0]
max = array[n-1]

print(min, max)