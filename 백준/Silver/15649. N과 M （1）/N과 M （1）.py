import sys
import itertools

inp = sys.stdin.readline
n,m = map(int,inp().split())

arr = [i for i in range(1,n+1)]
for i in itertools.permutations(arr,m) :
    print(' '.join(map(str,i)))