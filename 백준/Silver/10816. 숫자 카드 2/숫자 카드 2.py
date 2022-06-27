import sys
from collections import Counter

n = int(sys.stdin.readline())
card = list(sys.stdin.readline().strip().split())
C_card = Counter(card)

m = int(sys.stdin.readline())
chk = list(sys.stdin.readline().strip().split())

result = []
for i in chk :
    result.append(C_card[i])
    
print(' '.join(map(str,result)))